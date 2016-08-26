# In The Name Of God
# ========================================
# [] File Name : cli.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import cmd
import os.path
import pprint

from pykaa.rest.app import KaaRestApplication, KaaRestApplicationError
from pykaa.rest.sdk import KaaRestSDKProfile
from pykaa.rest.config import T1820RestConfig, T1820RestConfigError
from pykaa.domain.sdk import SDKProfileTargetPlatform

try:
    import termcolor
except ImportError:
    termcolor = None


class KaaCLICmd(cmd.Cmd):
    def __init__(self):
        super(KaaCLICmd, self).__init__()
        self.firewall = None
        self.config_name = "Not Loaded"
        self.address = "127.0.0.1:8080"
        self.admin_pass = "admin123"
        self.admin_user = "admin"
        self.dev_user = "devuser"
        self.dev_pass = "devuser123"
        self.intro = """
{0:*^80}
{1:=^80}
Kaa.py version 0.1, Copyright (C) 2015 Parham Alvani (parham.alvani@gmail.com)
Kaa.py comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
""".format("Welcome",
           " CLI program for Kaa Administration which "
           "is written by Parham Alvani ")

    def preloop(self):
        prompt = "Kaa Administration CLI [] >"
        if termcolor:
            prompt = termcolor.colored(prompt, color="red", attrs=['bold'])
        server = input("{} Please enter 18.20 ip address: ".format(prompt))
        try:
            config = T1820RestConfig(server).get_last_configuration()
        except T1820RestConfigError as e:
            pprint.pprint("*** REST error: {}".format(e), width=80)
            return
        self.address = config.kaa_ip + ":" + str(config.kaa_port)
        self.admin_user = config.kaa_admin_user
        self.admin_pass = config.kaa_admin_password
        self.dev_user = config.kaa_developer_user
        self.dev_pass = config.kaa_developer_password
        self.config_name = config.name

    def do_get_all_applications(self, line: str):
        kra = KaaRestApplication(self.address, self.dev_user, self.dev_pass)
        try:
            apps = kra.get_all_applications()
        except KaaRestApplicationError as e:
            pprint.pprint("*** REST error: {}".format(e), width=80)
            return
        for app in apps:
            print(app)

    @staticmethod
    def help_get_all_applications():
        command = "get_all_applications"
        if termcolor:
            command = termcolor.colored(command, color='green', attrs=['bold'])
        print(command)
        print("Get all Kaa applications registered in the server")

    def do_get_application_by_name(self, line: str):
        kra = KaaRestApplication(self.address, self.dev_user, self.dev_pass)
        try:
            apps = kra.get_all_applications()
        except KaaRestApplicationError as e:
            pprint.pprint("*** REST error: {}".format(e), width=80)
            return

        for app in apps:
            if app.name == line:
                break
        else:
            print("*** Invalid application name: {}".format(line))
            return
        print(app)

    def do_get_application_by_token(self, line: str):
        kra = KaaRestApplication(self.address, self.dev_user, self.dev_pass)
        try:
            app = kra.get_application_by_token(line)
        except KaaRestApplicationError as e:
            pprint.pprint("*** REST error: {}".format(e), width=80)
            return
        print(app)

    def do_get_all_sdk_profiles(self, line: str):
        try:
            application_token = line
        except TypeError as e:
            print("*** Invalid number: {}".format(str(e)))
            return
        krsp = KaaRestSDKProfile(self.address, self.dev_user, self.dev_pass)
        sdks = krsp.get_all_sdk_profiles(application_token)
        for sdk in sdks:
            print(sdk)

    def do_generate_endpoint_sdk(self, line: str):
        kra = KaaRestApplication(self.address, self.dev_user, self.dev_pass)
        apps = kra.get_all_applications()
        for app in apps:
            if app.name == line:
                break
        else:
            print("*** Invalid application name: {}".format(line))
            return
        krsp = KaaRestSDKProfile(self.address, self.dev_user, self.dev_pass)
        sdks = krsp.get_all_sdk_profiles(app.application_token)
        for sdk in sdks:
            print("[{0}] {1}: {2} {3} {4} {5}".format(sdk.id, sdk.name,
                                                      sdk.configuration_schema_version,
                                                      sdk.log_schema_version,
                                                      sdk.notification_schema_version,
                                                      sdk.profile_schema_version))
        sdk_id = input("Please enter your target sdk id: ")
        for sdk in sdks:
            if sdk.id == sdk_id:
                break
        else:
            print("*** Invalid SDK ID: {}".format(sdk_id))
            return
        path = input("Please enter path for saving generated sdk: ")
        path = os.path.join(path,
                            "{0}-c{1}-l{2}-n{3}-p{4}.tar.gz".format(sdk.name,
                                                                    sdk.configuration_schema_version,
                                                                    sdk.log_schema_version,
                                                                    sdk.notification_schema_version,
                                                                    sdk.profile_schema_version))
        krsp.generate_endpoint_sdk(sdk_id, SDKProfileTargetPlatform.c, path)

    @property
    def prompt(self):
        prompt = "Kaa Administration CLI [{}] > ".format(self.config_name)
        if termcolor:
            prompt = termcolor.colored(prompt, color="red", attrs=['bold'])
        return prompt

    def do_quit(self, line):
        print("Thank you for using Kaa Administration CLI")
        return True

    do_EOF = do_quit

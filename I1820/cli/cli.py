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

from ..pykaa.rest.app import KaaRestApplication, KaaRestApplicationError
from ..pykaa.rest.sdk import KaaRestSDKProfile
from ..pykaa.domain.sdk import SDKProfileTargetPlatform

from ..conf.config import cfg

try:
    import termcolor
except ImportError:
    termcolor = None


class I1820CLICmd(cmd.Cmd):
    def __init__(self):
        super(I1820CLICmd, self).__init__()
        self.admin_user = cfg.kaa_user_admin
        self.admin_pass = cfg.kaa_passwd_admin
        self.dev_user = cfg.kaa_user_developer
        self.dev_pass = cfg.kaa_passwd_developer
        self.address = cfg.kaa_host + ":" + cfg.kaa_port
        self.intro = """
{0:*^80}
{1:=^80}
18.20 version 1.0, Copyright (C) 2015 Parham Alvani (parham.alvani@gmail.com)
18.20 comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
""".format("Welcome",
           " CLI program for Kaa Administration which "
           "is written by Parham Alvani ")

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
            print("[{0}] {1}: {2} {3} {4} {5}".
                  format(sdk.id, sdk.name,
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
                            "{0}-c{1}-l{2}-n{3}-p{4}.tar.gz".
                            format(sdk.name,
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

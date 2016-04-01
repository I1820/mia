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
from pykaa.domain.sdk import SDKProfileTargetPlatform

try:
    import termcolor
except ImportError:
    termcolor = None


class KaaCLICmd(cmd.Cmd):
    def __init__(self):
        super(KaaCLICmd, self).__init__()
        self.firewall = None
        self.adminpass = "admin123"
        self.adminuser = "admin"
        self.devuser = "devuser"
        self.devpass = "devuser123"
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
        server = input("{} Please enter pykaa ip address: ".format(prompt))
        port = input("{} Please enter pykaa port: ".format(prompt))
        self.address = server + ":" + port
        self.devuser = input(
            "{} Please enter pykaa tenant developer username: ".format(prompt))
        self.devpass = input(
            "{} Please enter pykaa tenant developer password: ".format(prompt))
        self.adminuser = input(
            "{} Please enter pykaa tenant administrator username: ".format(
                prompt))
        self.adminpass = input(
            "{} Please enter pykaa tenant administrator password: ".format(
                prompt))

    def do_get_all_applications(self, line: str):
        kra = KaaRestApplication(self.address, self.devuser, self.devpass)
        try:
            apps = kra.get_all_applications()
        except KaaRestApplicationError as e:
            pprint.pprint(str(e), width=80)
            return
        for app in apps:
            print(app)

    def do_get_all_sdk_profiles(self, line: str):
        try:
            application_id = int(line)
        except TypeError as e:
            print("*** Invalid number: {}".format(str(e)))
            return
        krsp = KaaRestSDKProfile(self.address, self.devuser, self.devpass)
        sdks = krsp.get_all_sdk_profiles(application_id)
        for sdk in sdks:
            print(sdk)

    def do_generate_endpoint_sdk(self, line: str):
        kra = KaaRestApplication(self.address, self.devuser, self.devpass)
        apps = kra.get_all_applications()
        for app in apps:
            if app.name == line:
                break
        else:
            print("*** Invalid application name: {}".format(line))
            return
        krsp = KaaRestSDKProfile(self.address, self.devuser, self.devpass)
        sdks = krsp.get_all_sdk_profiles(app.id)
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
        prompt = "Kaa Administration CLI [{}] > "
        if termcolor:
            prompt = termcolor.colored(prompt, color="red", attrs=['bold'])
        return prompt

    def do_quit(self, line):
        print("Thank you for using Kaa Administration CLI")
        return True

    do_EOF = do_quit

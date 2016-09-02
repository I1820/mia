# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .cli import I1820CLICmd


def main():
    try:
        I1820CLICmd().cmdloop()
    except KeyboardInterrupt:
        quit(0)

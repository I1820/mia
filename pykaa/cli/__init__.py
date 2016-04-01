# In The Name Of God
# ========================================
# [] File Name : __init__.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from pykaa.cli.cli import KaaCLICmd


def main():
    try:
        KaaCLICmd().cmdloop()
    except KeyboardInterrupt:
        quit(0)

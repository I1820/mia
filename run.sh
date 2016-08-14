#!/bin/sh
# In The Name Of God
# ========================================
# [] File Name : run.sh
#
# [] Creation Date : 18-03-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
python3 setup.py develop -u
python3 setup.py develop
./bin/kaa.py

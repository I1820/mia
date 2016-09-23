#!/bin/sh
# In The Name Of God
# ========================================
# [] File Name : up-running.sh
#
# [] Creation Date : 01-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# [] Created By : Iman Tabrizian (tabrizian@outlook.com)
# =======================================
docker build -t aolab/i1820 .
docker run -d -p 8080:8080 --name="I1820" aolab/i1820

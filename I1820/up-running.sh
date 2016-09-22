#!/bin/sh
# In The Name Of God
# ========================================
# [] File Name : up-running.sh
#
# [] Creation Date : 01-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
docker build --force-rm -t aolab/i1820 .
docker run -p 8080:8080 --name="I1820" aolab/i1820
docker rm "I1820"

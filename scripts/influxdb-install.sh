#!/bin/bash
# In The Name Of God
# ========================================
# [] File Name : influxdb-install.sh
#
# [] Creation Date : 05-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
curl -sL https://repos.influxdata.com/influxdb.key | apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | tee /etc/apt/sources.list.d/influxdb.list
apt-get update && apt-get install influxdb
service influxdb start

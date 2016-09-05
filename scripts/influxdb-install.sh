#!/bin/bash
# In The Name Of God
# ========================================
# [] File Name : influxdb-install.sh
#
# [] Creation Date : 05-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update && sudo apt-get install influxdb
sudo service influxdb start

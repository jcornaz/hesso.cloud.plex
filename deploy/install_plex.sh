#!/usr/bin/env bash

apt-get update
apt-get upgrade
apt-get install curl -y

curl http://shell.ninthgate.se/packages/shell-ninthgate-se-keyring.key | sudo apt-key add -
echo "deb http://www.deb-multimedia.org wheezy main non-free" | tee -a /etc/apt/sources.list.d/deb-multimedia.list
echo "deb http://shell.ninthgate.se/packages/debian wheezy main" | tee -a /etc/apt/sources.list.d/plex.list

apt-get update
apt-get install deb-multimedia-keyring -y
apt-get install plexmediaserver -y
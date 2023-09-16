#!/bin/bash

echo "y" | sudo apt-get update
echo "y" | sudo apt-get upgrade
echo "y" | sudo apt-get install python3-pip libpq-dev postgresql postgresql-contrib nginx
echo "y" | sudo apt install python3.10-venv
echo "y" | sudo apt-get install openjdk-11-jre
echo "y" | sudo apt-get update
echo "y" | sudo apt-get upgrade
echo "y" | wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

echo "y" | sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
echo "y" | sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5BA31D57EF5975CA
echo "y" | sudo apt-get update
echo "y" | sudo apt-get install jenkins
echo "y" | sudo apt upgrade





echo "creating python env"

if [ -d "env" ] 
then
    echo "Python virtual environment exists." 
else
    python3 -m venv env
fi

source env/bin/activate

echo "upgrade pip"
python3 -m pip install --upgrade pip

pip3 install -r requirements.txt

if [ -d "media" ] 
then
    echo "media folder exists." 
else
    mkdir media
    sudo chmod -R 777 media
fi

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

echo "user is : $USER"

sudo chmod -R 777 logs


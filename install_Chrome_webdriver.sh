#!/bin/bash

sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4;
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip;
unzip chromedriver_linux64.zip;
rm chromedriver_linux64.zip;
sudo mv chromedriver /usr/bin/chromedriver;
sudo chown root:root /usr/bin/chromedriver;
sudo chmod +x /usr/bin/chromedriver;

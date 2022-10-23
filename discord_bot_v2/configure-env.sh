#!/bin/bash
#install python
sudo yum install gcc openssl-devel bzip2-devel libffi-devel
cd /opt 
sudo wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
sudo tar xzf Python-3.9.6.tgz
cd Python-3.9.6 
sudo ./configure --enable-optimizations 
sudo make altinstall
sudo rm -f /opt/Python-3.9.6.tgz
# set up test/build env
cd -
pip3 install pipenv
pipenv shell --python 3.9
pip3 install -r requirements.txt
wget https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz
tar -xvf ffmpeg-master-latest-linux64-gpl.tar.xz
sudo mv ffmpeg-master-latest-linux64-gpl/bin/* /usr/local/bin/
python3 -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
rm -rf ffmpeg-master-latest-linux64-gpl

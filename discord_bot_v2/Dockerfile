FROM ubuntu
LABEL version="3.0" \
      usage="discord bot build"
WORKDIR /app
COPY . .
# install python3.9
RUN apt update && apt install -y tzdata wget software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.9 pip
# set timezone
ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# install bot dependencies
RUN pip3 install -r requirements.txt
# install static ffmpeg build
RUN wget https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz
RUN tar -xvf ffmpeg-master-latest-linux64-gpl.tar.xz
RUN mv ffmpeg-master-latest-linux64-gpl/bin/* /usr/local/bin/
# install yt-dlp
RUN python3 -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
# clean up time
RUN rm -rf ffmpeg-master-latest-linux64-gpl
CMD python3 bot.py

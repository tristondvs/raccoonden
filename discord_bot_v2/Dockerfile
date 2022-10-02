FROM ubuntu
LABEL version="2.1" \
      usage="discord bot"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt update && apt install -y tzdata
ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt install -y python3 pip ffmpeg
RUN pip install -r requirements.txt
COPY . .
CMD python3 bot.py

FROM python:3.8.10 
LABEL version="2.0" \
      usage="discord bot"
      notable_update="utilizing nextcord instead of discord.py"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python bot.py

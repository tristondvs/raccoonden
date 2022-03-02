FROM python:3.8.10 
LABEL version="1.0" \
      usage="discord bot"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python bot.py

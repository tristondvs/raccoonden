FROM quoinedev/python3.7-pandas-alpine
LABEL version="1.0" \
      usage="twitch chatbot"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install pipenv
RUN pipenv --python 3.7
RUN pipenv install twitchio
COPY . .
CMD pipenv run python bot.py

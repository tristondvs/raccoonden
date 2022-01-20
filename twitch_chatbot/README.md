This project contains a small python script that acts as a twitch channel bot. I later placed it within a docker container.

The script utilizes variables that are within a `.env` file in the working directory. It has been excluded from git due to the sensitive information it contains.


For my own posterity:
To test the bot locally outside of the container for small changes before building:
```
pipenv run python bot.py
```



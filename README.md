## 📜 | Information
A Discord ChatBot made with Discord.py and pandorabots its very configurable and easy to self host. this bot was based of jagroshs frost bot which is now very outdated due to the discord.py rewrite ive also greatly improved upon most of the bot.

The bot was made with Discord.py 1.3.3 and you'll also need aiohttp 3.6.2 to get it running those are the bots only two dependencies. 

i made this bot for my discord server to replace myself.

## 🔧 | Setup

1) get a bot token from [here](https://discord.com/developers/applications) and then place it in the config file.

2) get a bot ID from [PandoraBots](https://pandorabots.com/botmaster/en/mostactive) pick a bot from there click on it and on the url you should see a part thats like botid=b0dafd24ee35a477 copy the part after the equal sign and put it in the config file by default chomsky is the bot id in the config file but you can change it to any bot.

3) fill out the rest of the config file. most of the variables have comments that explain what they do so its a simple process.

4) you can run the bot with the bat file but that only works on windows or on linuxyou can make your own sh file or run it with pm2.

## 📌 | known issues

- the bot wont have a response if you have a question mark anywhere in your message because of that i made it remove all question marks from the raw input to avoid this error from happening until i can fix it.
   
- the bot will sometimes give responses with unequal amount of leading spaces ive tried to get rid of it using several methods non of them seem to fix it for some reason. (this could vary from bot to bot)

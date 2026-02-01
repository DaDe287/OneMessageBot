# OneMessageBot
**pyTelegramBot** project. Answers all messages with prepareted text from file (nothing more)
### Use it if you need to relocate users to another telegram Bot for eg

Launch (Ubuntu/Debian):

```bash
cd /home
git clone https://github.com/DaDe287/OneMessageBot.git
cd OneMessageBot

bash <(curl -Ls https://raw.githubusercontent.com/DaDe287/AutoDocker/main/install-docker.sh) # Docker instalation

nano message.txt # Input your auto-message

cp .env.example .env # Edit .env (required)
 
docker compose up -d --build

```

-----------
`pyTelegramBotAPI`, `Docker-Compose`, `AsyncTeleBot` 

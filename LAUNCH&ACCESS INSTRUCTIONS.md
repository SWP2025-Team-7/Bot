You can access and test the deployed bot directly via Telegram:
[@SWP2025_team7_bot](https://t.me/SWP2025_team7_bot)
1. **Clone the repository**
   ```bash
   git clone https://github.com/SWP2025-Team-7/Bot.git
   cd Bot
   ```
2. **Create .env file**
  Use the .env.template as a base:
  
  ```bash
  cp .env.template .env
  ```

  Then open .env and insert your Telegram bot token:
  ```
  BOT_TOKEN=your_bot_token_here
  ```
3. **Start the bot**
  ```bash
  docker-compose up --build
  ```

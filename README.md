# Discord Text Classification Bot 
![harms bot](https://github.com/user-attachments/assets/2e82487e-b933-476f-b0d5-b5dca1916f89)

This Discord bot utilizes the Google Gemini Pro API to analyze the content of messages and classify them as "Neutral/Acceptable", "Hate Speech", or "Offensive/Vulgar". It provides a basic moderation tool for Discord servers by flagging messages that fall outside the "Neutral/Acceptable" category.

## Features

* **Real-time Message Classification:** The bot analyzes every message sent in the server.
* **Gemini Pro Integration:** Leverages the powerful Google Gemini Pro model for text analysis.
* **Classification Feedback:** Notifies the channel when a message is classified as "Hate Speech" or "Offensive/Vulgar".
* **Extensible Moderation:** Provides a foundation for implementing more advanced moderation features.
* **Easy Setup:** Uses environment variables for sensitive data like API keys and bot tokens.

## Prerequisites

Before running the bot, ensure you have the following:

1.  **Python 3.6+:** Python is required to run the bot.
2.  **Discord Bot Token:** You'll need to create a Discord bot and obtain its token from the Discord Developer Portal.
3.  **Google Gemini API Key:** You'll need an API key from Google AI Studio to access the Gemini Pro model.
4.  **Required Python Libraries:** Install the necessary libraries using pip:

    ```bash
    pip install discord.py google-generativeai python-dotenv
    ```

## Setup

1.  **Obtain API Keys and Tokens:**
    * Create a Discord bot application on the Discord Developer Portal and get the bot token.
    * Obtain a Google Gemini API key from Google AI Studio.
2.  **Set Environment Variables:**
    * Create a `.env` file in the same directory as your Python script.
    * Add your Discord bot token and Google Gemini API key to the `.env` file:

        ```
        DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
        GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
        ```

        **Important:** Never share your API keys or bot tokens publicly.
3.  **Invite the Bot to Your Server:**
    * Use the OAuth2 URL generator on the Discord Developer Portal to create an invite link for your bot.
    * Invite the bot to your Discord server.
4.  **Run the Bot:**
    * Navigate to the directory containing your Python script and `.env` file.
    * Run the script using Python:

        ```bash
        python your_bot_script_name.py
        ```
        (replace your_bot_script_name.py with the python filename)

## Disclaimer

This bot provides a basic moderation tool. The accuracy of the classification depends on the capabilities of the old data that this model has been trained on. Expectting state of the art classification accuracy, from this model= is simply foolish.

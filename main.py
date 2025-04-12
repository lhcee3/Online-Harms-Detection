import discord
from discord.ext import commands
import google.generativeai as genai
import os

# Configure your Gemini API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Configure the model for text analysis
model = genai.GenerativeModel('gemini-pro') # Using gemini-pro which is available on free tier

# Discord Bot Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def classify_text(text):
    """Classifies the nature of the text as Neutral, Hate Speech, or Offensive/Vulgar."""
    prompt = f"""
    Analyze the following text and classify its nature. Respond with only one of the following options:
    Neutral/Acceptable
    Hate Speech
    Offensive/Vulgar
    Text: {text}
    """
    try:
        response = model.generate_content(prompt)
        classification = response.text.strip()
        return classification
    except Exception as e:
        print(f"Error during Gemini API call: {e}")
        return "Error in classification"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    classification = classify_text(message.content)
    if classification != "Neutral/Acceptable":
      await message.channel.send(f"Warning: This message was classified as {classification}.")
      # You can implement further actions here, e.g., deleting the message
      # await message.delete()

    await bot.process_commands(message)

# Run the bot
bot.run(DISCORD_TOKEN)

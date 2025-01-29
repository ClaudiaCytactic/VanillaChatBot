from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Check if the key is loaded correctly
print(os.getenv("OPENAI_API_KEY"))

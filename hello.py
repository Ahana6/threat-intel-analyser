from dotenv import load_dotenv
import os

load_dotenv()
print("VirusTotal key loaded:", os.getenv("VT_API_KEY") is not None)
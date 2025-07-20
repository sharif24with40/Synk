import os
from dotenv import load_dotenv
import wolframalpha

load_dotenv()  

API_KEY = os.getenv("WOLFRAM_API_KEY")
client = wolframalpha.Client(API_KEY) 

def ask_wolframalpha(question):
    try:
        res = client.query(question)
        if res.success:
            return next(res.results).text
        else:
            return "No results found."
    except Exception as e:
        return f"Error: {str(e)}"

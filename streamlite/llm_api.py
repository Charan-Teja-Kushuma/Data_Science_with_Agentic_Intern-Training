"""
1.what is an API
2.APi Request
3.APi Response
4.LLM API Workflow 
5.API KEy
6.Model selection
7.ENV 
8.SDK ( Python , JS, Go)
Error Handling 


"""

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in environment variables. Please set it in your .env file.")


#api client (python SDk)
#send prompt
#reveice response
#print the response
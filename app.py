from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app and API
app = Flask(__name__)
api = Api(app)

# Initialize model and parser
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)
parser = StrOutputParser()

# Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

chain = prompt_template | model | parser

class Translate(Resource):
    def post(self):
        try:
            postedData = request.get_json()
            language = postedData.get("language")
            text = postedData.get("text")

            if not language or not text:
                ret={
                    "status": 400,
                    "msg": "Missing 'language' or 'text' in request body"
                }
                return jsonify(ret)

            result = chain.invoke({"language": language, "text": text})

            ret={
                "status": 200,
                "translation": result,
                "msg": "Translation successful"
            }
            return jsonify(ret)
        
        except Exception as e:
            ret={
                "status": 500,
                "msg": str(e)
            }
            return jsonify(ret)
        
api.add_resource(Translate, '/tran')

if __name__ == "__main__":
    app.run(debug=True)

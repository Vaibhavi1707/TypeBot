from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import text_Chatbot


app=Flask(__name__)
user=''
bot=''
chat=[]

class Chat:
	def __init__(self,user,bot):
		self.you=user
		self.bot=bot

@app.route('/')	
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def accept():
	you=request.form['type_something']
	processed_text=you.lower()
	bot=text_Chatbot.run(processed_text)
	talk=Chat(processed_text,bot)
	chat.append(talk);
	return render_template('index.html',chat=chat)


if __name__=="__main__":
	app.run(host='127.0.0.1',port='7000',debug=True)

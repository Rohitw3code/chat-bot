import random as rd
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

def BoldReply(msg):
    message = str(msg).lower().strip()
    if message in ["hii", "hai" , "hi", "hello", "greetings", "sup", "what's up", "hey"]:
        return rd.choice(["Hello 👋", "👋 Hi there, how can I help?"])
    elif message in ["thanks", "thank you", "thanks for helping me", "nice","great","that's great"]:
        return rd.choice(["You are welcome! 🥰", "Happy to help! 🥰", "My pleasure 🥰"])
    elif message in ["awesome","that is good to hear","good","beautiful","cute"]:
        return rd.choice(["Thanks","Thanks :)"])
    elif message in ["how are you doing?","how are you doing"]:
        return rd.choice(["I am doing great!"])
    elif message in ["ok","ook","okay","ok bye","okk","see you"]:
        return "ok"
    elif "account" in message:
        return  "visit https://www.anz.com.au/personal/ to know more about how to open an account"
    elif "insurance" in message:
        return  "We provide Business insurance and Personal insurance , to know more visit https://www.anz.com.au/business/insurance/"
    elif "welcome" in message:
        return ":)"
    elif "thanks" in message:
        return rd.choice(["You are welcome! 🥰", "Happy to help! 🥰", "My pleasure 🥰"])
    elif "industrie" in message:
        return "<i>We understand that every industry has different needs requiring specific banking solutions. Our team of dedicated business bankers can help your business achieve your goals and we also have specialists across a number of industries.</i>\n" \
               "visit : https://www.anz.com.au/business/industries/"
    elif "credit" in message:
        return "Choose the credit card that's a good fit for you\n With ten cards to choose from, it’s easy to find a card to suit your lifestyle and goals.\n" \
               "visit to know more https://www.anz.com.au/personal/credit-cards/ \n" \
               "<b>Business credit cards<b/>\n visit : https://www.anz.com.au/business/credit-cards/"
    elif "payment" in message or "merchant" in message:
        return "<i>Every day is pay day with our great range of payment services.\n Our EFTPOS machines will help smooth the payment experience for your customers.</i>" \
               "\n visit to know more https://www.anz.com.au/business/merchants-payments/"
    elif "loan" in message:
        return "we provide personal, Home and Business loan visit the following link to know more \n <b>Personal Loan :</b>  https://www.anz.com.au/personal/ \n <b>Home Loan :</b> https://www.anz.com.au/personal/home-loans/ \n <b>Business Loan </b> : https://www.anz.com.au/business/loans-finance/"
    elif message is None or message == "":
        return rd.choice(["Sorry, can't understand you 😅", "😅 Please give me more info", "😅 Not sure I understand"])
    elif "name" in message:
        return "My name is <b>Capgemini</b> , How can i Help you?"
    elif "who are you" in message or "work" in message:
        return "I am your ANZ enquiry chatbot capgmini 😀 , you can ask me anything related ANZ banking"
    elif "ok " in message or " ok" in message:
        return "ok"
    else:
        return "Sorry , i can't understand you 😥😕😞"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    reply  = BoldReply(userText)
    return reply


if __name__ == "__main__":
    app.run(debug=True)

'''
python -m spacy download en_core_web_sm

chatterbot\tagging.py 

Replace self.nlp = spacy.load(self.language.ISO_639_1.lower()) with

if self.language.ISO_639_1.lower() == 'en':
    self.nlp = spacy.load('en_core_web_sm')
else:
    self.nlp = spacy.load(self.language.ISO_639_1.lower())

'''

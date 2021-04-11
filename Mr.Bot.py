from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if "hi" or "hello" in incoming_msg:
        # To return a greeting
        reply = "Hello!"
        msg.body(reply)
        responded = True
    
    if "how are you" in incoming_msg:
        # To return a greeting msg
        reply = "I'm fine, and you?"
        msg.body(reply)
        responded = True
    
    if "fine" in incoming_msg:
        # To return a greeting msg
        reply = "Oh great!"
        msg.body(reply)
        responded = True
    
    if "bye" in incoming_msg:
        # To return a greeting msg
        reply = "Ok Byeee! See you soon"
        msg.body(reply)
        responded = True
    
    if "who are you" in incoming_msg:
        # To return a info msg
        reply = "I'm Mr.Bot, a WhatsApp chat bot!"
        msg.body(reply)
        responded = True

    if "who created you" in incoming_msg:
        # To return a info msg
        reply = "I'm created by my master, Crispin!"
        msg.body(reply)
        responded = True
    
    if "thanks" or "thank you" in incoming_msg:
        # To return a greeting msg
        reply = "Cool!"
        msg.body(reply)
        responded = True

    if "quote" in incoming_msg:
        # To return a quote
        r = requests.get("https://api.quotable.io/random")
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = "I could not retrieve a quote at this time, sorry!"
        msg.body(quote)
        responded = True

    if "cat" in incoming_msg:
        # To return a cat pics
        msg.media("https://cataas.com/cat")
        responded = True

    if "fact" or "facts" in incoming_msg:
        # To return a fact about cats
        r = requests.get("https://meowfacts.herokuapp.com")
        if r.status_code == 200:
            data = r.json()
            fact = f'{data["data"]}'
        else:
            fact = "I could not retrieve a fact at this time, sorry!"
        msg.body(fact)
        responded = True

    if "joke" in incoming_msg:
        # To return a joke
        r = requests.get("https://v2.jokeapi.dev/joke/Any")
        if r.status_code == 200:
            data = r.json()
            joke = f'{data["setup"]} ({data["delivery"]})'
        else:
            joke = "I could not retrieve a joke at this time, sorry!"
        msg.body(joke)
        responded = True

    if "trump saying" in incoming_msg:
        # To return a trump saying
        r = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
        if r.status_code == 200:
            data = r.json()
            trump_saying = f'{data["message"]}'
        else:
            trump_saying = "I could not reterive a trump saying at this time, sorry!"
        msg.body(trump_saying)
        responded = True
    
    if not responded:
        reply_1 = "I only respond to messages with the following commands, sorry!"
        reply_2 = "hi, hello, how are you, fine, bye, thanks, who are you, who created you, quote, cat, fact, joke, trump saying"
        reply_3 = "No worries, my master is working out on developing me..."
        msg.body(reply_1)
        msg.body(reply_2)
        msg.body(reply_3)
    return str(resp)


if __name__ == "__main__":
    app.run()
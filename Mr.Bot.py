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

    if "command" in incoming_msg:
        # To return with the command list
        reply = "The commands are as follows,\n Hi, How are you, Fine, Nice, Bye, Thanks, Who are you, Who created you, Quote, Cat, Fact, Joke, Trump's Saying.\n Thank you!"
        msg.body(reply)
        responded = True

    if "hi" in incoming_msg:
        # To return a greeting msg
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

    if "nic" in incoming_msg:
        # To return a reply msg
        reply = "Cool!"
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
        reply = "I'm a bot developed by my master, Crispin!"
        msg.body(reply)
        responded = True
    
    if "thanks" in incoming_msg:
        # To return a greeting msg
        reply = "Welcome!"
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

    if "cat img" in incoming_msg:
        # To return a cat pics
        msg.media("https://cataas.com/cat")
        responded = True

    if "fact" in incoming_msg:
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

    if "trump's saying" in incoming_msg:
        # To return a trump's saying
        r = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
        if r.status_code == 200:
            data = r.json()
            trump_saying = f'{data["message"]}'
        else:
            trump_saying = "I could not reterive a trump saying at this time, sorry!"
        msg.body(trump_saying)
        responded = True
    
    if "meme" in incoming_msg:
        # To return a random meme
        r = requests.get("https://meme-api.herokuapp.com/gimme")
        if r.status_code == 200:
            data = r.json()
            meme = f'{data["url"]}'
        else:
            meme = "I could'nt reterive a meme at this time, sorry!"
        msg.media(meme)
        responded = True

    if "bored" in incoming_msg:
        # To return an idea
        r = requests.get("https://www.boredapi.com/api/activity")
        if r.status_code == 200:
            data = r.json()
            idea = f'{data["activity"]}'
        else:
            idea = "I could'nt reterive an idea at this time, sorry!"
        msg.body(idea)
        responded = True

    if not responded:
        reply = "Sorry! I only respond to messages with the following commands...\n\n****Hi, How are you, Fine, Nice, Bye, Thanks, Who are you, Who created you, Quote, Cat, Fact, Joke, Trump's Saying****\n\nNo worries, my master is working on developing me to make me a super cool chat bot...\n\nThank you!"
        msg.body(reply)
    return str(resp)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
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

    if not responded:
        msg.body("I only know about famous quotes, cats and facts, sorry!")
    return str(resp)


if __name__ == "__main__":
    app.run()
from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse, Dial

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()

    # CHANGE THIS to your real Twilio work number
    caller_id = "+19099705700"

    # Create the Dial object and force caller ID to your Twilio number
    dial = Dial(timeout=20, callerId=caller_id)

    # List the phones you want to ring
    dial.number("+19097810829")   # Person 1
    dial.number("+19094377512")   # Person 2
    # Add more if needed...

    response.append(dial)
    return Response(str(response), mimetype="text/xml")

@app.route("/sms", methods=["POST"])
def sms():
    response = VoiceResponse()

    # This returns a simple reply message
    # (We can change this to anything you want)
    response.message("Thanks for texting us! We will respond shortly.")

    return Response(str(response), mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

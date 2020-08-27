import twilio.rest as twilio
import azure.functions as func
import os
import ldclient

ACCOUNT_SID = os.environ['account_SID']
AUTH_TOKEN = os.environ['auth_token']
TWIL_NUMBER = os.environ['twilio_phone']
MY_PHONE_NUMBER = os.environ['hayley_phone']
CLIENT = twilio.Client(ACCOUNT_SID, AUTH_TOKEN)

def send_reminder_text():
    message = CLIENT.messages.create(
        to=MY_PHONE_NUMBER, 
        from_=TWIL_NUMBER,
        body="Time to update your flags for the workday! Respond with 'wfhinfo' for instructions.")


def send_message(outgoing_message, send_to, send_from):
    message = CLIENT.messages.create(
        body=outgoing_message, from_=send_from, to=send_to,
    )
    return func.HttpResponse(
        "Thank you for using Hayley's WFH app", status_code=200
    )
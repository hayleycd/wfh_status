import datetime
import logging

import azure.functions as func
import __app__.my_twilio_funcs as twilio_funcs

def main(twilioTimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    twilio_funcs.send_reminder_text()
    logging.info('Python timer trigger function ran at %s', utc_timestamp)

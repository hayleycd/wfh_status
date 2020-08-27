import logging
import os
import requests

import azure.functions as func
import __app__.my_twilio_funcs as twilio_funcs
import __app__.launch_dark as ld_common


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Get phone information
    send_to = req.params["From"]
    send_from = req.params["To"]
    incoming_message = req.params["Body"].lower().strip()

    if incoming_message == "flags":
        message = ld_common.get_flag_keys()
    
    elif incoming_message == "wfhinfo":
        message = """
        To see a list of flag keys text: flags
        
        To turn off a flag, text the flag key followed by "!" ex: dog-fed!
        
        To turn on a flag, text the flag key ex: dog-fed
        
        To see this message again text: wfhinfo
        
        To see my WFH status, send any other message"""

    elif incoming_message in ld_common.flag_keys:
        ld_common.turn_on_flag(incoming_message)
        message = "You have turned " + incoming_message + " ON"
    
    elif incoming_message[-1] == "!" and (incoming_message[:-1] in ld_common.flag_keys):
        key = incoming_message[:-1]
        ld_common.turn_off_flag(key)
        message = "You have turned " + key + " OFF"

    else:
        # Get flag info
        message = ld_common.get_flag_info_via_text()

        # Send message
    
    twilio_funcs.send_message(message, send_to, send_from)
    
    # Return Status
    return func.HttpResponse(
        "Thank you for using Hayley's WFH App. Text wfhinfo for details.", status_code=200
    )
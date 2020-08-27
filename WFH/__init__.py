import logging
import os

import azure.functions as func
import ldclient
import jinja2
import __app__.launch_dark as ld_common

#Authorize Launch Darkly
ldclient.set_sdk_key(os.environ['LDKey'])

#Flags
flag_keys = ld_common.flag_keys

#Set up Templating Engine
loader = jinja2.FileSystemLoader('./WFH')
env = jinja2.Environment(
    loader=loader,
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)
template = env.get_template('home.html')

def launch_darkly(flag_keys):
    flag_status = {}
    for key in flag_keys:
        flag_status[key] = ldclient.get().variation(key, {"key": "user@test.com"}, False)
    return flag_status


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('processed request for home funciton')
    logging.info('checking LaunchDarkly flags')
    flag_dict = launch_darkly(flag_keys)
    return func.HttpResponse(body=template.render(flags = flag_dict), headers={"Content-Type": "text/html; charset=utf-8"})
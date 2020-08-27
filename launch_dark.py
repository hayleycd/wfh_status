import os
import json
import requests

LD_API_KEY = os.environ['ld_AUTH']

flag_keys = [
    "do-not-disturb",
    "dog-walked",
    "dog-fed",
    "interview",
    "recording",
    "dog-walked",
    "hearing-aids",
    "run-complete",
]

def get_flag_info_via_text():
    response = request_flag_info()

    response_flag_list = json.loads(response.text)["items"]
    message = ""
    for item in response_flag_list:
        if item["environments"]["production"]["on"]:
            message = message + item["description"] + ": YES\n"
        else:
            message = message + item["description"] + ": NO\n"
    
    return message

def get_flag_keys():
    response = request_flag_info()
    flags = json.loads(response.text)["items"]
    message = ""
    for flag in flags:
        message = message + flag["key"] + "\n"

    return message

def turn_on_flag(key):
    url="https://app.launchdarkly.com/api/v2/flags/default/" + key
    headers = {
        "ld-api-version": "beta",
        "authorization": LD_API_KEY,
    }
    patch = [{ "op": "replace", "path": "environments/production/on", "value": True}]
    requests.patch(url, json=patch, headers=headers)

def turn_off_flag(key):
    url="https://app.launchdarkly.com/api/v2/flags/default/" + key
    headers = {
        "ld-api-version": "beta",
        "authorization": LD_API_KEY,
    }
    patch = [{ "op": "replace", "path": "environments/production/on", "value": False}]
    requests.patch(url, json=patch, headers=headers)


def request_flag_info():
    url = "https://app.launchdarkly.com/api/v2/flags/default"
    querystring = {"env":"production","limit":"100","offset":"0","summary":"true"}

    headers = {
        "ld-api-version": "beta",
        "authorization": LD_API_KEY
    }
    
    return requests.request("GET", url, headers=headers, params=querystring)
"""[summary]
"""

import requests
import logging
import datetime
import sys
import os
import getpass

def get_username():
    username = input("What is your name")
    return username

def get_password():
    password = getpass.getpass("Please enter your password")
    return password

def get_host_and_port():
    host = input("Please enter the ip of the host or its hostname: ")
    port = input("Please enter the port number of the host: ")
    return host, port

def get_token(localhost, port, USERNAME, PASSWORD):
    url = f"http://{localhost}:{port}/api/v1/ticket"

    payload = {
        "username": f"{USERNAME}",
        "password": f"{PASSWORD}"
    }
    headers = {"Content-Type": "application/json"}
    try:
        logging.info("Trying to get the response from the server.... stand by")
        response = requests.request("POST", url, json=payload, headers=headers)
    except Exception as error:
        logging.error(f"Houston, we have a problem {error}")
    else:
        logging.info("Successfully got a response from the server")
        return response['response']["serviceTicket"]

def network_devicces(apikey):
    url = "http://localhost:58000/api/v1/network-device"

    payload = ""
    headers = {"X-Auth-Token": f"{apikey}"}

    response = requests.request("GET", url, data=payload, headers=headers)

    print(response.text)

def main():
    host, port = get_host_and_port()
    username = get_username()
    password = get_password()
    Token = get_token(host, port, username, password)
    network_devicces(Token)

if __name__=="__main__":
    main()
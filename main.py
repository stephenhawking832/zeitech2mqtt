import requests
import paho.mqtt.client as mqtt
# create Hosts class to store the mqtt broker and the zeitech hosts
class Hosts:
    def __init__(self, url):
        host = url
# create Channels class to store channel info
class Channels:
    def __init__(self, mqtttopic, state):
        self.topic = mqtttopic
        self.payload = state

def get_channel_info(host):
    # get the channel info from the zeitech api
    response = requests.get(f"http://{host}/ch.cgi")
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to get channel info: {response.status_code}")

def parse_zeitech_info(channel_string):    
# parse the channel info and return a list of Channels objects
    channel_list = channel_string.splitlines()


def find_the_equal_sign(channel_list):
    for channel in channel_list:
        equal_place = channel.find("=")
        return equal_place


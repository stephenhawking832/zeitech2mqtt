import requests
import publishtopic as pub
import parsechannelinfo as ch
# create Hosts class to store the mqtt broker and the zeitech hosts
class Hosts:
    def __init__(self, url):
        host = url
# create Channels class to store channel info
class Channels:
    topic = "zeitech/channels/commend/"
    def __init__(self, state):
        self.payload = state

def get_channel_info(host):
    # get the channel info from the zeitech api
    response = requests.get(f"http://{host}/ch.cgi")
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to get channel info: {response.status_code}")



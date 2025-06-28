import requests
import parsechannelinfo as ch
import time
# create Hosts class to store the mqtt broker and the zeitech hosts
class Hosts:
    def __init__(self, url):
        host = url


def get_channel_info(host):
    # get the channel info from the zeitech api
    response = requests.get(f"http://{host}/ch.cgi?ivr=0&maingroups=1")
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to get channel info: {response.status_code}")
i = 0
while i < 15:
  test = get_channel_info("192.168.1.33")
  print(ch.parse(test))
  i += 1
  time.sleep(1)

import requests
import paho.mqtt.client as mqtt
# create Hosts class to store the mqtt broker and the zeitech hosts
class Hosts:
    def __init__(self, url):
        host = url
# create Channels class to store channel info
class Channels:
    def __init__(self, mqtttopic, payload_off, payload_on):
        self.topic = mqtttopic
        self.on = payload_on
        self.off = payload_off




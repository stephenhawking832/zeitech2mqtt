def parse(channel_string):    
# parse the channel info and return a list of Channels objects
    channel_list = channel_string.splitlines()


def equal_sign(list):
#Finds the index of the first occurrence of the equal sign '=' in the first element of the given list.
    for channel in list:
        equal_place = channel.find("=")
        return equal_place
def parse(channel_string):    
# parse the channel info and return a list of Channels objects
    channel_list = channel_string.splitlines()
    return channel_list

def equal_sign(list):
#Finds the index of the first occurrence of the equal sign '=' in the first element of the given list.
    equal_places = []
    for channel in list:
        equal_places.append(channel.find("="))
    return equal_places
def channels_dict(equal_place_list, ch_info_list):
    dict = {}
    i = 0
    for info in ch_info_list:
        channel_number = info[0:equal_place_list[i]]
        channel_state = info[equal_place_list[i]+1:]
        dict[f"c{channel_number}"] = channel_state
        i += 1
    return dict






ch_list = parse('1=2\n12=0\n3=1\n11=0\n5=22')
place = equal_sign(ch_list)

ch_dict = channels_dict(place, ch_list)
print(ch_dict)

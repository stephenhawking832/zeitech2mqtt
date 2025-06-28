def parse(channel_string):
# parse the channel info and return a list of Channels objects
  channel_list = channel_string.splitlines()
  equal_places = []
  channel_dict = {}
  i = 0
  for channel in channel_list:
     equal_places.append(channel.find("="))
  for info in channel_list:
     channel_number = info[0:equal_places[i]]
     channel_state = info[equal_places[i]+1:]
     channel_dict[f"c{channel_number}"] = channel_state
     i += 1
  return channel_dict

ch_dict = parse('1=2\n12=0\n3=1\n11=0\n5=22')

print(ch_dict)

#parse the channel info to dict
def parse(channel_string: 'str'):
#parse the string to list line by line
  channel_list = channel_string.splitlines()
#objects define
  equal_places = []
  channel_dict = {}
  i = 0
#get from in each list itame th equel sign place
  for channel in channel_list:
     equal_places.append(channel.find("="))
#convert from list to dict
  for info in channel_list:
     channel_number = info[0:equal_places[i]]
     channel_state = info[equal_places[i]+1:]
     channel_dict[f"c{channel_number}"] = channel_state
     i += 1
  return channel_dict

ch_dict = parse('1=2\n12=0\n3=1\n11=0\n5=22')

print(ch_dict)

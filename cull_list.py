from slacker import Slacker
import arrow

# grab api key
f = open('config', 'r')
apikey = f.read()

# grab all channel details
slack = Slacker(apikey)
channel_all = slack.channels.list()
channel_time = dict()

# create dict (channel id as key)
# containing channel name and timestamp of most recent post
for i in channel_all.body['channels']:
    if i['is_archived'] is False:
        try:
            last_post = arrow.get(slack.channels.history(i['id'], count=1).body['messages'][0]['ts'])
            channel_name = i['name']
            try:
                channel_creator = slack.users.info(i['creator']).body['user']['name']
            # handle users that no longer exit
            except:
                channel_creator = None
            channel_time[i['id']] = [channel_name, channel_creator, last_post]
        # handle empty channels
        except:
            channel_name = i['name']
            try:
                channel_creator = slack.users.info(i['creator']).body['user']['name']
            # handle users that no longer exit
            except:
                channel_creator = 'none'
            channel_time[i['id']] = [channel_name, channel_creator, None]

# function for returning full list of unarchived channels with date of last post and creator name
# do i even need this?
# def full_channels():

# function for returning channels inactive for x months (defaults to 3)
def old_channels(channels, age=3):
    cull_channels = []
    for i  in channels:
        if channels[i][2] is not None:
            if channels[i][2] < arrow.utcnow().replace(months=-age):
                cull_channels.append(channels[i])
    return(cull_channels)

# function for returning empty channels
def empty_channels(channels):
    cull_channels = []
    for i in channels:
        if channels[i][2] is None:
            cull_channels.append(channels[i])
    return(cull_channels)

# function for returning channels inactive for x months (defaults to 3) AND empty channels
#def dead_channels(channels, months=3):
#    cull_channels = dict()
 
from slacker import Slacker
import arrow
#grab api key
f = open('config', 'r')
apikey = f.read()

#grab all channel details
slack = Slacker(apikey)
channel_all = slack.channels.list()
channel_time = dict()

# create dict (channel id as key)
# containing channel name and timestamp of most recent post
for i in channel_all.body['channels']:
    if i['is_archived'] is False:
        try:
            channel_time[i['id']] = [i['name'], arrow.get(slack.channels.history(i['id'], count=1).body['messages'][0]['ts'])]
#handle empty channels    
        except:
            channel_time[i['id']] = [i['name'], 'none']

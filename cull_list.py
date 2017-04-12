from slacker import Slacker

f = open('config', 'r')
apikey = f.read()

slack = Slacker(apikey)
channel_all = slack.channels.list()
channel_time = dict()

for i in channel_all.body['channels']:
    try:
        channel_time[i['id']] = [i['name'],
            slack.channels.history(i['id'], count=1).body['messages'][0]['ts']]
    except:
        channel_time[i['id']] = [i['name'], 'none']

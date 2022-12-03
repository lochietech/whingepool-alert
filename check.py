#!/usr/bin/python3 -u

from discord_webhook import DiscordWebhook
import json
import urllib.request
import time


## Whirlpool Details ##
api_key="<API KEY>>"
forum_id="<FORUM ID>"
thread_id="<THREAD ID>"
thread_name="<THREAD NAME>"
discord_webhook="<DISCORD HOOK>"

last_post = "never"

while True:
    
    time.sleep(300) #Interval to check

    with urllib.request.urlopen("https://whirlpool.net.au/api/?key="+api_key+"&get=threads&forumids="+forum_id+"&output=json") as url:
        data = json.load(url)
        threads = data["THREADS"]
        for x in threads:
            values = x.values()
            if thread_id in values:
                date=list(x.values())
                check_post=date[8]

    if last_post == check_post:
 #       print("No new posts")
        same = True

    else:
 #       print(check_post)
        webhook = DiscordWebhook(url=discord_webhook, content=("New Post in __"+ thread_name +"__ https://forums.whirlpool.net.au/thread/"+thread_id+"&p=-1#bottom"))
        response = webhook.execute()
        last_post = check_post

import requests
from os import listdir
from subprocess import run
from random import shuffle
import config

# Create copy file from remote server to our dir
response = requests.get(config.m3u_path)
data = response.text.split('\n')
with open('/home/snowman/temp_file.txt','w+') as f:
    for line in data:
        if 'http' in line:
            f.write(line+'\n')
        else:
            pass
#---
run(['rm', '/home/snowman/temp_files.txt'])
# Open a dirs with ads
ads = listdir(ads_path)
shuffle(ads)
#---

# Mix video with ads as: Video - Ads..
with open('/home/snowman/temp_file.txt','r') as f, open(end_file,'w+') as f2:
    data = f.readlines()
    shuffle(data)
    f2.write('#EXTM3U\n\n')
    i=0
    for line in data:
        f2.write('\n#EXTINF:-1\n'+str(line))
        try:
            f2.write('\n#EXTINF:-1\n'+ads_path+str(ads[i])+'\n')
        except IndexError:
            i=0
            f2.write('\n#EXTINF:-1\n'+ads_path+str(ads[i])+'\n')
        i+=1
run(['rm', '/home/snowman/temp_files.txt'])

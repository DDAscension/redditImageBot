import praw
import requests
from tqdm import tqdm
import itertools
import os.path
import urllib

subName = 'earthporn'

outputDir= 'c:/temp/earthporn/'

r = praw.Reddit("Pretty pictures")
sub = r.get_subreddit(subName)

for submission in itertools.islice(sub.get_top_from_week(), 10):
        if (submission.url[-4:].lower() == '.jpg'):
            filename = outputDir + subName + ' ' + str(submission.id) + '.jpg'
            if not os.path.isfile(filename):
                print("downloading " + submission.url)
                urllib.request.urlretrieve(submission.url, filename)

                #response = requests.get(submission.url, stream=True)
                #with open(filename, "wb") as handle:
                #    for data in tqdm(response.iter_content()):
                #        handle.write(data)
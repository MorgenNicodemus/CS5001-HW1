#Morgen Nicodemus
#HW6
import xml.etree.ElementTree as ET
import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import urllib
import requests
import re
from googleapiclient.discovery import build
import base64
import io
import os
import PIL
from PIL import Image
from urllib.request import urlopen

f = open('key.txt')
info = list(f)
key = info[0].rstrip('\n')
service = build('vision', 'v1', developerKey=key)

analyzer = SentimentIntensityAnalyzer()

def getDesc(photo):
    for desc in photo.iter('description'):
        return desc.text

def getUrl(photo):
    for url in photo.iter('url'):
            return url.text

def label_image(path=None, URL=None, max_results=5):
    if URL is not None:
        image_content = base64.b64encode(urllib.request.urlopen(URL).read())
    else:
        image_content = base64.b64encode(open(path, 'rb').read())
    service_request = service.images().annotate(body={
        'requests': [{
            'image': {
                'content': image_content.decode('UTF-8')
            },
            'features': [{
                'type':'LABEL_DETECTION',
                'maxResults': max_results
            }]
        }]
    })
    labels = service_request.execute()['responses'][0]['labelAnnotations']
    return labels

def main():
    tree = ET.parse('photosPASCAL.xml')
    root = tree.getroot()
    
    x = 0   
    for photo in root.iter('photo'):
        if x == 12:
            break
        desc = getDesc(photo)
        if desc is None:
            continue
        if analyzer.polarity_scores(desc)['compound'] == 0.0:
            continue
        url = getUrl(photo)
        
        try:
            response = urllib.request.urlopen(url).read()
        except:
            pass
            #print("Retrieving webpage failed")

        try:
            source = str(response, 'utf-8')
            result = re.search('<meta property="og:image" content="https://live\.staticflickr\.com/.*',source)
            test = result.group(0)
            image = test[35:-23]
   
        except:
            pass
            #print("Failed to retrieve image url")

        try:
            labels = label_image(URL=image,max_results=10)
            image_avg = 0
            counter = 0
            for label in labels:
                image_avg = image_avg + analyzer.polarity_scores(label['description'])['compound']
                counter += 1
                
            image_avg = image_avg / counter
            if image_avg == 0.0:
                continue
            
        except:
            pass
            #print("Failed to process image with Google Vision")
        print(desc)
        for label in labels:
            print ('[{0:3.0f}%]: {1}'.format(label['score']*100, label['description']))
        print("Description score: ",analyzer.polarity_scores(desc)['compound']," Image score: ",image_avg,"\n")
        x += 1

if __name__ == '__main__':
    main()
    

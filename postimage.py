import requests
import config
import json

def postInstagramQuote(image_location_1):

    post_url = 'https://graph.facebook.com/v13.0/{}/media'.format(config.ig_user_id)
    
    username = ''
    
    six_dots = '\n . ' * 6 + '\n'
    hashtags = '#funnymemes #memes #meme #funny #memesdaily #comedy #lol #humor #dankmemes #funnyvideos #lmao #love #fun #jokes #follow #instagram #tiktok #explore #hilarious #instagood #haha #dank #dailymemes #edgymemes #funnyshit #memestagram #lmfao #laugh'
    
    payload = {
    'image_url': image_location_1,
    'caption': 'Follow @' + username + ' for more!'+ six_dots + hashtags,
    'access_token': config.user_access_token,
    }
    
    r = requests.post(post_url, data=payload)
    
    print(r.text)
    
    result = json.loads(r.text)

    if 'id' in result:
        creation_id = result['id']
        
        second_url = 'https://graph.facebook.com/v13.0/{}/media_publish'.format(config.ig_user_id)
        second_payload = {
        'creation_id': creation_id,
        'access_token': config.user_access_token
        }
        
        r = requests.post(second_url, data=second_payload)
        print('--------Just posted to instagram--------')
        print(r.text)
        
    else:
        print('Error!')

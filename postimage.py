import requests
import config
import json

def postInstagramQuote(image_location_1):

    post_url = 'https://graph.facebook.com/v13.0/{}/media'.format(config.ig_user_id)
    
    username = ''
    
    six_dots = '\n . ' * 6 + '\n'
    with open('hashtags') as file:
        hashtag_list = list(set(file.read().split('\n')))
    hashtags_chosen = random.choices(hashtag_list, k=30)
    hashtags = ' '.join(str(item) for item in hashtags_chosen)
    
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

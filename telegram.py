import datetime
import json
import os
import requests
from s3_bucket import upload_to_bucket


TOKEN = os.environ.get('TELEGRAMAPI')


def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


def tel_parse_get_message(message):
    print("message-->", message)

    try:
        g_chat_id = message['message']['chat']['id']
        g_file_id = message['message']['photo'][-1]['file_id']
        g_update_id = message['update_id']
        caption = ''
        date = message['message']['date']
        date = datetime.datetime.utcfromtimestamp(date)
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        try:
            caption = message['message']['caption']
            print(caption)
        except:
            caption = 'notfound'

        return g_file_id, g_chat_id, g_update_id, caption, date
    # except:
    except Exception as e:
        print(e)
        g_file_id = "notfound"
        g_chat_id = "notfound"
        g_update_id = "notfound"
        caption = "notfound"
        date = "notfound"
        return g_file_id, g_chat_id, g_update_id, caption, date


def tel_upload_file(file_id):
    url = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}'
    a = requests.post(url)
    json_resp = json.loads(a.content)
    print("a-->", a)
    print("json_resp-->", json_resp)
    file_pathh = json_resp['result']['file_path']

    url_1 = f'https://api.telegram.org/file/bot{TOKEN}/{file_pathh}'
    b = requests.get(url_1)
    file_content = b.content
    file_result = "/tmp/"+json_resp['result']['file_path']
    try:
        os.system('mkdir /tmp/photos')
    except Exception as e:
        print(e)
    try:
        with open(file_result, "wb") as f:
            f.write(file_content)
    except Exception as e:
        print(e)
    bucket_name = os.environ.get('BUCKET_NAME')
    get_file_name = json_resp['result']['file_path']
    get_file_name = get_file_name.split('/')
    get_file_name = get_file_name[1]
    upload_to_bucket(bucket_name, file_result, get_file_name)
    return get_file_name

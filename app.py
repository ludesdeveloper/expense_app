import os
import re
from telegram import tel_parse_get_message, tel_send_message, tel_upload_file, parse_message
from textract import extract_text
from s3_bucket import upload_to_bucket
from dynamodb import insert_expense, range_expense
from flask import Flask, jsonify, make_response, request, Response


app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


@app.route('/telegram_receipt_reader', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        get_file_name = ''
        msg = request.get_json()
        try:
            file_id, chat_id, update_id, caption, date = tel_parse_get_message(
                msg)
            if file_id != 'notfound':
                get_file_name = tel_upload_file(file_id)
                bucket_name = os.environ.get('BUCKET_NAME')
                search_key = 'total'
                kvs, get_value = extract_text(
                    bucket_name, get_file_name, search_key)
                tel_send_message(chat_id, kvs)
                tel_send_message(chat_id, get_value)
                try:
                    insert_expense(
                        str(update_id), get_value[1][0], caption, date)
                except Exception as e:
                    print(e)
            else:
                chat_id, txt = parse_message(msg)
                if txt == "hi":
                    tel_send_message(chat_id, "Hello!!")
                elif "range" in txt:
                    get_range = txt.split(' ')
                    get_today_expense = range_expense(
                        get_range[1], get_range[2])
                    tel_send_message(chat_id, get_today_expense)

        except Exception as e:
            print(e)
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"

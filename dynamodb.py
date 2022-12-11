import datetime
import os
import boto3
from boto3.dynamodb.conditions import Key, Attr

EXPENSE_TABLE = os.environ['EXPENSE_TABLE']


def insert_expense(expense_id, total, source, date):
    dynamodb_client = boto3.client('dynamodb')
    dynamodb_client.put_item(
        TableName=EXPENSE_TABLE, Item={
            'expenseId': {'S': expense_id}, 'total': {'S': total}, 'source': {'S': source}, 'date': {'S': date}}
    )


def today_expense():
    today = datetime.datetime.today() + datetime.timedelta(hours=7)
    nextday = datetime.datetime.today() + datetime.timedelta(hours=7) + \
        datetime.timedelta(days=1)
    today = today.strftime('%Y-%m-%d')
    nextday = nextday.strftime('%Y-%m-%d')
    print('debug date')
    print(today)
    print(nextday)
    print('debug date')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(EXPENSE_TABLE)
    response = table.scan(FilterExpression=Attr(
        'date').between(f'{today} 00:00:00', f'{nextday} 00:00:00'))
    data = response['Items']
    return data

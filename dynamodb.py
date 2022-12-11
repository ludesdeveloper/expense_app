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


def range_expense():
    start = datetime.datetime.today() + datetime.timedelta(hours=7)
    end = datetime.datetime.today() + datetime.timedelta(hours=7) + \
        datetime.timedelta(days=1)
    start = start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(EXPENSE_TABLE)
    response = table.scan(FilterExpression=Attr(
        'date').between(f'{start} 00:00:00', f'{end} 00:00:00'))
    data = response['Items']
    return data

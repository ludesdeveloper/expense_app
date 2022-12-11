import os
import boto3

EXPENSE_TABLE = os.environ['EXPENSE_TABLE']


def insert_expense(expense_id, total, source, date):
    dynamodb_client = boto3.client('dynamodb')

    dynamodb_client.put_item(
        TableName=EXPENSE_TABLE, Item={
            'expenseId': {'S': expense_id}, 'total': {'S': total}, 'source': {'S': source}, 'date': {'S': date}}
    )

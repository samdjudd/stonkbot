#python3.6.9
import discord
import boto3
import json
import re

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$'):
            if 
            to_add = int(re.sub("\$", "", message.content, 1))
            
            print(to_add)
            gainz = update_profit(to_add)
            msg = 'Total profits: ${}'.format(gainz)
            await client.send_message(message.channel, msg)
            
def update_profit(to_add, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('ProfitCounter')
    response = table.get_item(Key={"Name": "Profits"})
    old_number = (response['Item']['Money'])
    print(old_number)
    new_number = old_number + to_add
    response2 = table.update_item(
            Key={"Name": "Profits"},
            UpdateExpression="set Money = :t",
            ExpressionAttributeValues={
                ':t': new_number,
            },
            ReturnValues="UPDATED_NEW"
    )
    return new_number


client = MyClient()
client.run('NzE4NTI2Mjg0MDgyMzE1MzU0.XtqKfQ.a4sp_KAiam0mi6tnTTP3unf5wKI')
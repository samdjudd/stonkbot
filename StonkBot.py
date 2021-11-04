import discord
import boto3
import json
import re


class MyClient(discord.Client):
    async def on_ready(self):
        # Initializes the user
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # Runs when message is received from Discord server
        if message.author == client.user:
            return

        if message.content.startswith('$'):
            # message starts with '$' followed by numerical value
            to_add = int(re.sub("\$", "", message.content, 1))
            gainz = update_profit(to_add)
            msg = 'Total profits: ${}'.format(gainz)
            await message.channel.send(msg)
            
def update_profit(to_add, dynamodb=None):
    # updates the database with new total
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ProfitCounter')
    response = table.get_item(Key={"Name": "Profits"})
    old_number = (response['Item']['Money'])
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

if __name__ == "__main__":
    client = MyClient()
    # prd bot -> client.run($PRD_KEY)
    # dev bot
    client.run($DEV_KEY)

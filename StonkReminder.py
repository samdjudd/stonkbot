import discord


class Reminder(discord.Client):

    async def on_ready(self):
            msg = "@everyone Please dont forget to report your daily gains in this channel!"
            # dev -> channel = client.get_channel(718526699469406222)
            channel = client.get_channel(715502711759699998)
            await channel.send(msg)


if __name__ == "__main__":
    client = Reminder()
    client.run($PRD_KEY)
    # dev bot -> client.run($DEV_KEY)

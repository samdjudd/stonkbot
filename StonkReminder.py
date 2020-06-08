import discord


class Reminder(discord.Client):

    async def on_ready(self):
            msg = "@everyone Please dont forget to report your daily gains in the #profit-counter channel!"
            channel = client.get_channel(718526699469406222)
            await channel.send(msg)


if __name__ == "__main__":
    client = Reminder()
    # prd bot -> client.run('NzE4NTI2Mjg0MDgyMzE1MzU0.XtqKfQ.a4sp_KAiam0mi6tnTTP3unf5wKI')
    # dev bot
    client.run('NzE4NjI0ODk3NDg3NjAxNzM2.Xtrl1A.bUXZaHQCT4hOcEx788-Pgue8TUM')
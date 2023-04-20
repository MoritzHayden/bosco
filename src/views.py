import discord

class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        website_button = discord.ui.Button(label="Bosco Website", url="https://boscobot.dev/", style=discord.ButtonStyle.success)
        invite_button = discord.ui.Button(label="Invite to Server", url="https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147568704&scope=bot", style=discord.ButtonStyle.primary)
        self.add_item(website_button)
        self.add_item(invite_button)

import discord


class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(discord.ui.Button(label="Website",
                                        url="https://boscobot.dev/"))
        self.add_item(discord.ui.Button(label="Invite to Server",
                                        url="https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147568704&scope=bot"))

import discord
from config import BOSCO_WEBSITE_TEXT, BOSCO_WEBSITE_URL, BOSCO_INVITE_TEXT, BOSCO_INVITE_URL


class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(discord.ui.Button(label=BOSCO_WEBSITE_TEXT,
                                        url=BOSCO_WEBSITE_URL))
        self.add_item(discord.ui.Button(label=BOSCO_INVITE_TEXT,
                                        url=BOSCO_INVITE_URL))

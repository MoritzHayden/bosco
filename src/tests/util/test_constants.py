from util.constants import (
    BOSCO_USER_AGENT,
    BOSCO_WEBSITE_TEXT,
    BOSCO_WEBSITE_URL,
    BOSCO_INVITE_TEXT,
    BOSCO_INVITE_URL,
    ERROR_RESPONSE_TEXT
)


class TestConstants:
    def test_user_agent(self):
        assert isinstance(BOSCO_USER_AGENT, str)
        assert BOSCO_USER_AGENT == 'discord:dev.boscobot'

    def test_website_text(self):
        assert isinstance(BOSCO_WEBSITE_TEXT, str)
        assert BOSCO_WEBSITE_TEXT == 'Website'

    def test_website_url(self):
        assert isinstance(BOSCO_WEBSITE_URL, str)
        assert BOSCO_WEBSITE_URL == 'https://boscobot.dev/'

    def test_invite_text(self):
        assert isinstance(BOSCO_INVITE_TEXT, str)
        assert BOSCO_INVITE_TEXT == 'Invite to Server'

    def test_invite_url(self):
        assert isinstance(BOSCO_INVITE_URL, str)
        assert BOSCO_INVITE_URL.startswith('https://')
        assert 'client_id=' in BOSCO_INVITE_URL
        assert 'permissions=' in BOSCO_INVITE_URL
        assert 'scope=' in BOSCO_INVITE_URL

    def test_error_response_text(self):
        assert isinstance(ERROR_RESPONSE_TEXT, str)
        assert ERROR_RESPONSE_TEXT == 'Oops, something went wrong! Please try again later.'

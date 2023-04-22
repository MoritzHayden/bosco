# Bosco

<div align="center">

  <a href="https://github.com/MoritzHayden/bosco" target="_self">
    <img src="./src/img/avatar.png" width="30%" alt="Bosco Bot Logo" />
  </a>

  &nbsp;

  [![Platform](https://img.shields.io/badge/platform-discord-purple.svg)](https://discord.com)
  [![Language](https://img.shields.io/badge/language-python-yellow.svg)](https://www.python.org)
  [![License](https://img.shields.io/github/license/MoritzHayden/bosco?color=darkred)](https://github.com/MoritzHayden/bosco/blob/main/LICENSE)

  [![Issues](https://img.shields.io/github/issues/MoritzHayden/bosco?color=red)](https://github.com/MoritzHayden/bosco/issues)
  [![Pull Requests](https://img.shields.io/github/issues-pr/MoritzHayden/bosco?color=green)](https://github.com/MoritzHayden/bosco/pulls)
  [![Stars](https://img.shields.io/github/stars/MoritzHayden/bosco?color=blue)](https://github.com/MoritzHayden/bosco)

  [![Invite](./src/img/invite-button.svg)](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147568704&scope=bot)

</div>

---

## Table of Contents

- [About](#about)
- [Usage](#usage)
  - [/ping](#ping)
  - [/deep-dive](#deep-dive)
  - [/rock-and-stone](#rock-and-stone)
  - [/trivia](#trivia)
  - [/invite](#invite)
  - [/help](#help)
- [Local Development](#local-development)
  - [Registration](#registration)
  - [Configuration](#configuration)
  - [Installation](#installation)
  - [Execution](#execution)
- [Dependencies](#dependencies)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Special Thanks](#special-thanks)
- [Disclaimer](#disclaimer)
- [Legal](#legal)

## About

Bosco is a free, open-source Discord bot and companion for Deep Rock Galactic players. It can fetch weekly Deep Dives, provide random DRG trivia, and more!

## Usage

Once Bosco has been [invited](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147568704&scope=bot) to your server, it supports the following [slash commands](https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ):

### /ping

- Description: Ping Bosco and get latency.
- Options: None
- Syntax:
  ```text
  /ping
  ```

### /deep-dive

- Description: Get weekly Deep Dive details.
- Options:
  - `type`: An optional enum indicating which Deep Dive to fetch details for (enum values: `ALL`, `DEEP_DIVE`, `ELITE_DEEP_DIVE`, default: `ALL`).
- Syntax:
  ```text
  /deep-dive type=ELITE_DEEP_DIVE
  ```

### /rock-and-stone

- Description: You already know what this does.
- Options: None
- Syntax:
  ```text
  /rock-and-stone
  ```

### /trivia

- Description: Get a random piece of DRG trivia.
- Options: None
- Syntax:
  ```text
  /trivia
  ```

### /invite

- Description: Invite Bosco to your server.
- Options: None
- Syntax:
  ```text
  /invite
  ```

### /help

- Description: View the command list and helpful links.
- Options: None
- Syntax:
  ```text
  /help
  ```

## Local Development

In order to run Bosco locally, you will need to configure your environment variables.

### Registration

In order for Bosco to interact with the services it depends on (Discord and Reddit), you will need to register for each of these services and obtain your tokens/secrets:

1. Discord
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Copy your bot token.
2. Reddit
   - Create a new [Reddit application](https://www.reddit.com/prefs/apps) and register it for access to the [Reddit API](https://www.reddit.com/wiki/api/). Copy your application client id and secret.

### Configuration

Create a file called `.env` within the `src/` directory to hold your environment variables, and add the following keys (replacing `<VALUE>` with the real value):

```text
DISCORD_TOKEN=<VALUE>
REDDIT_CLIENT_ID=<VALUE>
REDDIT_CLIENT_SECRET=<VALUE>
```

### Installation

First, make sure you have [Python 3](https://www.python.org/downloads/) installed on your system. Then, install the project dependencies by running the following command from the root of this repository:

```bash
pip3 install -r src/requirements.txt
```

### Execution

Start Bosco by running the following command from the root of this repository:

```bash
python3 src/bot.py
```

## Dependencies

Dependencies are automatically scanned and updated with [Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates) every weekday at 10am UTC, as configured in [dependabot.yml](./.github/dependabot.yml). For questions about security, please reference the [Security Policy](./docs/SECURITY.md).

## Deployment

The bot is automatically deployed to the [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform) whenever a push is made to the [main branch](https://github.com/MoritzHayden/bosco/tree/main).

## Contributing

Contributions are welcome! If you found a bug or have a feature request, please open an [issue](https://github.com/MoritzHayden/bosco/issues). If you would like to contribute changes, please [fork](https://github.com/MoritzHayden/bosco/fork) this repository, open a [pull request](https://github.com/MoritzHayden/bosco/pulls) with your changes, and link the PR with an [issue](https://github.com/MoritzHayden/bosco/issues). All contributions must adhere to the [Code of Conduct](./docs/CODE-OF-CONDUCT.md).

## Special Thanks

- The folks who maintain the [Deep Rock Galactic Wiki](https://deeprockgalactic.gamepedia.com/Deep_Rock_Galactic_Wiki) for supplying game images and data
- The [r/DeepRockGalactic](https://www.reddit.com/r/DeepRockGalactic/) subreddit for supplying deep dive information
- The [Deep Rock Galactic developers](https://ghostship.dk/about/#team) for being awesome and incredibly engaged with the community

## Disclaimer

Neither this project nor its contributors are associated with Deep Rock Galactic or Ghost Ship Games in any way whatsoever.

## Legal

- [Terms of Service](./docs/TERMS-OF-SERVICE.md)
- [Privacy Policy](./docs/PRIVACY-POLICY.md)
- [Security Policy](./docs/SECURITY.md)
- [MIT License](LICENSE)

<div align="center">

  <p>Copyright &copy; 2023 Hayden Moritz</p>

</div>

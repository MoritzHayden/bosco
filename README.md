# Bosco

<div align="center">

  <a href="https://github.com/MoritzHayden/bosco" target="_self">
    <img src="./img/avatar-alt.png" width="30%" alt="Bosco Bot Logo" />
  </a>

  &nbsp;

  [![Platform](https://img.shields.io/badge/platform-discord-blue.svg)](https://discord.com)
  [![Language](https://img.shields.io/badge/language-python-yellow.svg)](https://www.python.org)
  [![License](https://img.shields.io/github/license/MoritzHayden/bosco?color=darkred)](https://github.com/MoritzHayden/bosco/blob/main/LICENSE)

  [![Issues](https://img.shields.io/github/issues/MoritzHayden/bosco)](https://github.com/MoritzHayden/bosco/issues)
  [![Stars](https://img.shields.io/github/stars/MoritzHayden/bosco)](https://github.com/MoritzHayden/bosco)

  [![Install](./img/install.svg)](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147568704&scope=bot)
</div>

---

## Table of Contents

- [About](#about)
- [Usage](#usage)
  - [/ping](#ping)
  - [/deep-dives](#deep-dives)
  - [/loadout](#loadout)
  - [/fun-fact](#fun-fact)
- [Local Development](#local-development)
  - [Registration](#registration)
  - [Configuration](#configuration)
  - [Installation](#installation)
  - [Execution](#execution)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Special Thanks](#special-thanks)
- [Disclaimer](#disclaimer)
- [Legal](#legal)

## About

Bosco is a free, open-source Discord bot and companion for Deep Rock Galactic players. It can fetch weekly Deep Dives, suggest new Dwarf loadouts, provide fun facts, and more!

## Usage

Once Bosco has been [invited](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147568704&scope=bot) to your server, it supports the following [slash commands](https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ):

### `/ping`

- Description: A health check which pings Bosco and returns the latency.
- Arguments:
  - None
- Syntax:
  ```text
  /ping
  ```

### `/deep-dives`

- Description: Returns details about the weekly deep dives.
- Arguments:
  - None
- Syntax:
  ```text
  /deep-dives
  ```

### `/loadout`

- Description: Returns a randomized loadout for the specified Dwarf.
- Arguments:
  - `dwarf`: A required string describing which dwarf the loadout should be generated for (valid values: driller, engineer, gunner, scout).
- Syntax:
  ```text
  /loadout dwarf=engineer
  ```

### `/fun-facts`

- Description: Returns one or more fun facts.
- Arguments:
  - `count`: An optional integer describing how many fun facts should be returned (valid range: 1-10, default: 1).
- Syntax:
  ```text
  /fun-facts count=1
  ```

## Local Development

In order to run Bosco locally, you will need to configure your environment variables.

### Registration

In order for Bosco to interact with the services it depends on (Discord, Reddit, API Ninjas), you will need to register for each of these services and obtain your tokens/secrets:

1. Discord
    - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Copy your bot token.
2. Reddit
    - Register for access to the [Reddit API](https://www.reddit.com/wiki/api/). Copy your client id and secret.
3. API Ninjas
    - Register for access to [API Ninjas](https://api-ninjas.com/). Copy your api token.

### Configuration

Create a file called `.env` within the `src/` directory to hold your environment variables, and add the following keys (replacing `<VALUE>` with the real value):
```text
DISCORD_TOKEN=<VALUE>
REDDIT_CLIENT_ID=<VALUE>
REDDIT_SECRET=<VALUE>
API_NINJAS_TOKEN=<VALUE>
```

### Installation

Install dependencies by running the following command from the root of this repository:

```bash
pip install -U -r src/requirements.txt
```

### Execution

Start Bosco by running the following command from the root of this repository:
```bash
python3 src/bot.py
```

## Deployment

The bot is automatically deployed to the [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform) whenever a push is made to the [main branch](https://github.com/MoritzHayden/bosco/tree/main).

## Contributing

Contributions are welcome! If you found a bug or have a feature request, please open an [issue](https://github.com/MoritzHayden/bosco/issues). If you would like to contribute changes, please [fork](https://github.com/MoritzHayden/bosco/fork) this repository, open a [pull request](https://github.com/MoritzHayden/bosco/pulls) with your changes, and link the PR with an [issue](https://github.com/MoritzHayden/bosco/issues). All contributions must adhere to the [Code of Conduct](./docs/CODE-OF-CONDUCT.md).

## Special Thanks

- The folks who maintain the [Deep Rock Galactic Wiki](https://deeprockgalactic.gamepedia.com/Deep_Rock_Galactic_Wiki) for supplying game images and data
- [@thamara](https://github.com/thamara) for their work on [drg-deep-dive-bot](https://github.com/thamara/https://github.com/thamara/drg-deep-dive-bot) which inspired this project
- The Deep Rock Galactic developers for being awesome. Rock and Stone!

## Disclaimer

Neither this bot nor its contributors are associated with Deep Rock Galactic or Ghost Ship Games in any way whatsoever.

## Legal

- [Terms of Service](./docs/TERMS-OF-SERVICE.md)
- [Privacy Policy](./docs/PRIVACY-POLICY.md)
- [MIT License](LICENSE)

<div align="center">

  Copyright &copy; 2023 Hayden Moritz

</div>

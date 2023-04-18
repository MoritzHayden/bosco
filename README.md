# Bosco

<div align="center">

  <a href="https://github.com/MoritzHayden/bosco" target="_self">
    <img src="./img/avatar-alt.png" width="30%" alt="Bosco Bot Logo" />
  </a>

  &nbsp;

  [![Platform](https://img.shields.io/badge/platform-discord-blue.svg)](https://discord.com)
  [![Language](https://img.shields.io/badge/language-python-yellow.svg)](https://www.python.org)
  [![GitHub License](https://img.shields.io/github/license/MoritzHayden/bosco?color=darkred)](https://github.com/MoritzHayden/bosco/blob/main/LICENSE)

  [![Deployment](https://github.com/MoritzHayden/bosco/actions/workflows/deploy.yml/badge.svg)](https://github.com/MoritzHayden/bosco/actions/workflows/deploy.yml)
  [![GitHub Release](https://img.shields.io/github/v/release/MoritzHayden/bosco?color=darkgreen)](https://github.com/MoritzHayden/bosco/releases)
  [![GitHub Issues](https://img.shields.io/github/issues/MoritzHayden/bosco)](https://github.com/MoritzHayden/bosco/issues)
  [![GitHub Stars](https://img.shields.io/github/stars/MoritzHayden/bosco)](https://github.com/MoritzHayden/bosco)

</div>

---

## Table of Contents

- [About](#about)
- [Usage](#usage)
  - [/ping](#ping)
  - [/deep-dives](#deep-dives)
  - [/fun-fact](#fun-fact)
- [Local Development](#local-development)
  - [Registration](#registration)
  - [Configuration](#configuration)
  - [Installation](#installation)
  - [Execution](#execution)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Legal](#legal)

## About

Bosco is a free, open-source Discord bot and companion for Deep Rock Galactic players. It can fetch weekly Deep Dives, suggest new Dwarf loadouts, provide fun facts, and more!

## Usage

Bosco supports the following [slash commands](https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ):

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

In order for Bosco to interact with the services (Discord, Reddit, API Ninjas) it depends on, you will need to register for each of these services and obtain your tokens/secrets:

1. Discord
    - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Copy your bot token for the next step.
2. Reddit
    - Register for access to the [Reddit API](https://www.reddit.com/wiki/api/). Copy your client id and secret for the next step.
3. API Ninjas
    - Register for access to [API Ninjas](https://api-ninjas.com/). Copy your api token for the next step.

### Configuration

Create a file called `.env` in the `src/` directory to hold your environment variables, and add the following keys (replacing `<VALUE>` with the real value):
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

The bot is automatically deployed to a [DigitalOcean droplet](https://www.digitalocean.com/products/droplets) whenever a push is made to the [main branch](https://github.com/MoritzHayden/bosco/tree/main). This process is automated in the [Deployment](./.github/workflows/deploy.yml) GitHub Actions workflow.

## Contributing

Contributions are welcome! If you found a bug or have a feature request, please open an [issue](https://github.com/MoritzHayden/bosco/issues). If you would like to contribute changes, please open a [pull request](https://github.com/MoritzHayden/bosco/pulls) with your changes and associate it with an [issue](https://github.com/MoritzHayden/bosco/issues).

## Legal

- [Terms of Service](./docs/TERMS-OF-SERVICE.md)
- [Privacy Policy](./docs/PRIVACY-POLICY.md)
- [MIT License](LICENSE)

<div align="center">

  Copyright &copy; 2023 Hayden Moritz

</div>

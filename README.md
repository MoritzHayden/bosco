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

  [![Invite](./img/discord-invite-button.svg)](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147568704&scope=bot)

</div>

---

## Table of Contents

- [About](#about)
- [Usage](#usage)
  - [/help](#help)
  - [/ping](#ping)
  - [/deep-dives](#deep-dives)
  - [/loadout](#loadout)
  - [/rock-and-stone](#rock-and-stone)
  - [/fun-fact](#fun-fact)
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

Bosco is a free, open-source Discord bot and companion for Deep Rock Galactic players. It can fetch weekly Deep Dives, suggest new Dwarf loadouts, provide fun facts, and more!

## Usage

Once Bosco has been [invited](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147568704&scope=bot) to your server, it supports the following [slash commands](https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ):


### `/help`

- Description: Get help with bosco
- Options: None
- Syntax:
  ```text
  /help
  ```

### `/ping`

- Description: A health check which pings Bosco and returns the latency.
- Options: None
- Syntax:
  ```text
  /ping
  ```

### `/deep-dive`

**UNDER DEVELOPMENT**

- Description: Get details about the weekly deep dives.
- Options:
  - `type`: An optional enum indicating which Deep Dive to fetch details for (enum values: `ALL`, `DEEP_DIVE`, `ELITE_DEEP_DIVE`, default: `ALL`).
- Syntax:
  ```text
  /deep-dive type=ELITE_DEEP_DIVE
  ```

### `/loadout`

**UNDER DEVELOPMENT**

- Description: Get a randomized loadout for the specified Dwarf.
- Options:
  - `dwarf`: A required enum indicating which Dwarf the loadout should be generated for (enum values: `DRILLER`, `ENGINEER`, `GUNNER`, `SCOUT`).
- Syntax:
  ```text
  /loadout dwarf=ENGINEER
  ```

### `/rock-and-stone`

- Description: Rock and Stone!
- Options: None
- Syntax:
  ```text
  /rock-and-stone
  ```

### `/fun-fact`

- Description: Get one or more fun facts.
- Options:
  - `count`: An optional integer indicating how many fun facts should be returned (valid range: `1-10`, default: `1`).
- Syntax:
  ```text
  /fun-fact count=1
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
API_NINJAS_TOKEN=<VALUE>
REDDIT_CLIENT_ID=<VALUE>
REDDIT_SECRET=<VALUE>
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

Neither this bot nor its contributors are associated with Deep Rock Galactic or Ghost Ship Games in any way whatsoever.

## Legal

- [Terms of Service](./docs/TERMS-OF-SERVICE.md)
- [Privacy Policy](./docs/PRIVACY-POLICY.md)
- [Security Policy](./docs/SECURITY.md)
- [MIT License](LICENSE)

<div align="center">

  <p>Copyright &copy; 2023 Hayden Moritz</p>

</div>

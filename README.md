# Bosco

<div align="center">

  <a href="https://boscobot.dev/" target="_self">
    <img src="./src/img/avatar.png" width="30%" alt="Bosco Bot Logo" />
  </a>

  &nbsp;

  [![Invite](./src/img/invite-button.svg)](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147485696&scope=bot)

  [![Platform](https://img.shields.io/badge/platform-discord-purple.svg)](https://discord.com)
  [![Language](https://img.shields.io/badge/language-python-yellow.svg)](https://www.python.org)
  [![Python Version](https://img.shields.io/github/pipenv/locked/python-version/MoritzHayden/bosco/main/src?label=python&color=blue)](src/Pipfile)
  [![Code Size](https://img.shields.io/github/languages/code-size/MoritzHayden/bosco?color=blue)](https://boscobot.dev/)
  [![License](https://img.shields.io/github/license/MoritzHayden/bosco?color=darkred)](https://github.com/MoritzHayden/bosco/blob/main/LICENSE)

  [![CodeQL](https://github.com/MoritzHayden/bosco/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/MoritzHayden/bosco/actions/workflows/codeql.yml)
  [![Pytest](https://github.com/MoritzHayden/bosco/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/MoritzHayden/bosco/actions/workflows/pytest.yml)
  [![Pylint](https://github.com/MoritzHayden/bosco/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/MoritzHayden/bosco/actions/workflows/pylint.yml)
  [![Issues](https://img.shields.io/github/issues/MoritzHayden/bosco?color=informational)](https://github.com/MoritzHayden/bosco/issues)
  [![Pull Requests](https://img.shields.io/github/issues-pr/MoritzHayden/bosco?color=informational)](https://github.com/MoritzHayden/bosco/pulls)

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
  - [Registering](#registering)
  - [Configuring](#configuring)
  - [Installing](#installing)
  - [Linting](#linting)
  - [Testing](#testing)
  - [Executing](#executing)
- [Dependencies](#dependencies)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Special Thanks](#special-thanks)
- [Disclaimer](#disclaimer)
- [Legal](#legal)

## About

Bosco is a free, open-source Discord bot and companion for Deep Rock Galactic players. It can fetch weekly Deep Dives, provide random DRG trivia, and more!

## Usage

Once Bosco has been [invited](https://discord.com/api/oauth2/authorize?client_id=1097476432579539026&permissions=2147485696&scope=bot) to your server, it supports the following [slash commands](https://support.discord.com/hc/en-us/articles/1500000368501-Slash-Commands-FAQ):

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
  - `variant`: An optional enum indicating which Deep Dive to fetch details for. Enum values: `ALL` (default), `DEEP_DIVE`, and `ELITE_DEEP_DIVE`.
- Syntax:
  ```text
  /deep-dive variant=ELITE_DEEP_DIVE
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

In order to run Bosco locally, you will need to install [Python 3](https://www.python.org/) and perform some initial setup.

### Registering

Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Then, click on the "Bot" tab and copy your bot token which will be used in the next step.

### Configuring

Create a file called `.env` within the `src/` directory to hold your environment variables, and add the following (replacing `<VALUE>` with the real value):

```text
DISCORD_TOKEN=<VALUE>
```

### Installing

Install dependencies by executing the [install.sh](./src/scripts/install.sh) script with the `-d` flag. Alternatively, you can use the `-i` option while executing the [lint.sh](./src/scripts/lint.sh), [test.sh](./src/scripts/test.sh), or [run.sh](./src/scripts/run.sh) scripts to install dependencies in a single step:

```bash
./src/scripts/install.sh -d
```

### Linting

Run the linter by executing the [lint.sh](./src/scripts/lint.sh) script:

```bash
./src/scripts/lint.sh [-i,-h]
```

### Testing

Run the unit tests by executing the [test.sh](./src/scripts/test.sh) script:

```bash
./src/scripts/test.sh [-i,-h]
```

### Executing

Start Bosco by executing the [run.sh](./src/scripts/run.sh) script:

```bash
./src/scripts/run.sh [-i,-h]
```

## Dependencies

Dependencies are automatically scanned and updated with [Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates) every weekday at 10am UTC, as configured in [dependabot.yml](./.github/dependabot.yml). For questions about security, please reference the [Security Policy](./docs/SECURITY.md).

## Deployment

The bot is automatically deployed to the [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform) whenever a push is made to the [main branch](https://github.com/MoritzHayden/bosco/tree/main).

## Contributing

Contributions are welcome! If you found a bug or have a feature request, please open an [issue](https://github.com/MoritzHayden/bosco/issues). If you would like to contribute changes, please [fork](https://github.com/MoritzHayden/bosco/fork) this repository, open a [pull request](https://github.com/MoritzHayden/bosco/pulls) with your changes, and link the PR with an [issue](https://github.com/MoritzHayden/bosco/issues). All contributions must adhere to the [Code of Conduct](./docs/CODE-OF-CONDUCT.md). PRs must pass all status checks (linting, code quality, etc.) and recieve codeowner approval before they will be merged.

## Special Thanks

- The [DRG API](https://drgapi.com/) contributors for developing the API that powers Bosco
- The folks who maintain the [Deep Rock Galactic Wiki](https://deeprockgalactic.wiki.gg/) for supplying game resources and data
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

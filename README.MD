<div align="center">

<img src="./assets/logo.png" alt="Logo of TaskForce" width="350"/>

# **TaskForce**

🤖 **TaskForce**: A community based framework around [CrewAi](https://crewai.com/) for collaborating AI agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

</div>

# Getting Started

## Options

- [Run inside the dev container](#dev-container)
- [Install the dependencies locally](#local-installation)

## Project structure

```bash
    .
    ├── .github
    │   ├── workflows
    ├── .devcontainer
    │   ├── devcontainer.json # Dev container configuration
    ├── assets
    │   ├──... # Images and other assets
    ├── taskforce
    │   ├── lib
    │   │   ├── interfaces
    │   │       ├── ...     # Interfaces for the framework
    │   │   ├── tools
    │   │       ├── ...     # Tools folders
    │   │   ├── models.py   # General models for the framework
    │   │   ├── task_utils.py
    │   ├── crews
    │   │   ├── ... # Crews folders
    ├── .env.example # Example of the .env file, not all the variables are required
    ├── Dockerfile.dev
    ├── README.md

```

# Development

## Dev Container

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [VSCode](https://code.visualstudio.com/)
- [Dev Container Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Running the Dev Container

- Open the project in VSCode
- Open the `Command Palette` (Cmd+Shift+P)
- Select "Reopen in Container"
- Wait for the container to build
- Run `make run-tests` to run the tests
- Done!

## Local Installation

### Installing Dependencies

```bash
poetry lock
poetry install
```

### Virtual Env

```bash
poetry shell
```

### Pre-commit hooks

```bash
pre-commit install
```

### Running Tests

```bash
poetry run pytest
```

### Contribution

TaskForce is open-source and we welcome contributions. If you're looking to contribute, please:

- Fork the repository.
- Create a new branch for your updates.
- Add your agent, tool or any other improvement.
- Send a pull request.

## License

TaskForce is released under the MIT License.

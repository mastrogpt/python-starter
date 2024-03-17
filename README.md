# Nuvolaris MastroGPT

Build easily AI applications with MastroGPT!

# Setup

You can run Nuvolaris Starter: 
- Online with Codespace 
- Locally with Docker

## Online Setup 

- Get a GitHub account
- Fork this repo in your own account
- Start it with Codespaces (you have 60 free hours)
- See below for setup.

## Local Setup 

- Install Docker and VScode in your machine
- Clone this repo
- Open it in VSCode
- Press F1  and the "Reopen in Container"

# Secrets

- Copy the `.env.example` in `.env`
- Add your secrets there.
- Pass the parameters as secrets to your function with `#--param ARGUMENT $VARIABLE`
- Read the secrets as function arguments

# Development

Use the Nuvolaris Icon to execute or use from the terminal:

- `devel` to run a local development environment
- `deploy` to deploy everything in cloud
- `login` to login again

Note those are actually shortcuts for:

- `nuv ide devel`
- `nuv ide deploy`
- `nuv ide login`

Check `nuv ide` subcommand for more options.

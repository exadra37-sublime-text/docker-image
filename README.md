# Sublime Text 3 Docker Image

This Docker image will allow us to run the amazing [Sublime Text 3](https://www.sublimetext.com/) without the need to install it in our computer.

The intention behind it is that each time I want to install or upgrade a new OS I need to install all Developer tools again, but running them from Docker containers will make my Development environment very portable and easy and fast to install in any computer.

Another benefit is to be able different Sublime versions with different Languages versions without also have to install them on my computer.

## How To Use

#### Using CURL in command line:

```bash
sh -c "$(curl -fsSL https://gitlab.com/exadra37-docker//raw/master/install)"
```

#### Using WGET in command line:

```bash
sh -c "$(wget  https://gitlab.com/exadra37-docker//raw/master/install -O -)"
```

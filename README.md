# Sublime Text 3 Docker Container

This Docker image will allow us to run the amazing [Sublime Text 3](https://www.sublimetext.com/) without the need to
install it in our computers.

Another benefit is to be able to try different Sublime Text builds, with different Programming Languages versions.

The motivation to create this package come from the burn of reinstalling my Development environment across several computers each time I install/upgrade an OS or change computer.

So this package is the first of a series of other packages to make my Development environment very portable, easy and fast to
install in any computer.


## How To Install Sublime Text 3 Docker Container

#### Using CURL in command line:

```bash
bash -c "$(curl -fsSL https://gitlab.com/exadra37-docker/sublime-text-3/raw/master/setup/install)"
```

#### Using WGET in Command Line:

```bash
bash -c "$(wget  https://gitlab.com/exadra37-docker/sublime-text-3/raw/master/setup/install -O -)"
```

## How To Use Sublime Text 3 Docker Container

By default the Sublime Text build is `3126` and the Sublime Text will persist settings, cache and installed packages in
dir `/home/$USER/.docker-sublime`.

The default Host dir shared with the Sublime Text Container is `/home/$USER/Developer`, that we can override at any time.


#### Run With Defaults

```bash
sublime
```

#### See Help

Check how to use it at any time...


```bash
sublime -h
```

#### Run With Other Build

Currently the Sublime Text build defaults to `3126`.

We can build the Docker Image with a previous or future build of Sublime Text, just by providing a different build number...

```bash
sublime -b 3124
```

#### Run With Custom Developer Workspace

By default `/home/$USER/Developer/Workspace` on Host is mapped to Container `/home/$USER/Developer`, but we can change the path
 in the Host we want to map into the Container, like:

```bash
sublime -d /absolute/path/in/host
```

#### Rebuild Docker Image

To have the Ubuntu inside the Docker Image up to date we should rebuild the image every week.

```bash
sublime -r
```

#### How to Debug Sublime Text Docker Container

For trouble shouting Sublime Text 3 installation we may need to go inside the docker container.

To help us on that, when starting the container the exact command will be printed:

```bash
sudo docker exec -it ST3_1486504665 bash
```

# Sublime Text 3 Docker Container

This Docker image will allow us to run the amazing [Sublime Text 3](https://www.sublimetext.com/) without the need to
install it in our computers.

Another benefit is to be able to try different Sublime Text builds, with different Programming Languages versions.

The motivation to create this package come from the burn of reinstalling my Development environment across several computers each time I install/upgrade an OS or change computer.

So this package is the first of a series of other packages to make my Development environment very portable, easy and fast to
install in any computer.

## How To Use From Docker Hub

The recommend way is to build the image locally with bash interface `sublime`. See instructions [here](how-to-install-sublime-text-3-docker-cli).

This will map the current folder in the HOST to folder `developer` inside the Container.


#### Download script to run the Docker Container

```bash
$ curl -OL https://gitlab.com/exadra37-docker/sublime-text-3/raw/master/src/docker-hub.sh && chmod ug+x docker-hub.sh
```

#### Run Sublime Text 3 from a Docker Container

```
$ ./docker-hub.sh
```

**NOTE:** The preferable method is to use the **Sublime Docker CLI** to build the image locally and run it.

## How To Install Sublime Text 3 Docker CLI

#### Using CURL in command line:

```bash
bash -c "$(curl -fsSL https://gitlab.com/exadra37-docker/sublime-text-3/raw/master/setup/install)"
```

#### Using WGET in Command Line:

```bash
bash -c "$(wget  https://gitlab.com/exadra37-docker/sublime-text-3/raw/master/setup/install -O -)"
```

## How To Use Sublime Text 3 Docker Container

Sublime Text will persist settings, cache and installed packages in the Container dir `/home/$USER/.docker-sublime` that is mapped into the host dir `/home/$USER/.config/sublime-text-3`. Meaning that changes done inside the Container will be available in the host and vice versa.

#### Defaults

* The Sublime Text build is `3126`. Any other build of Sublime can be used to build a local Docker Image.
* The image used `exadra37/sublime-textt-3` is pulled from Docker Hub. A local one can be build or another one can be pulled from Docker Hub.
* The Host dir shared with the Sublime Text Container is the current dir as per `$PWD` variable. Another dir can be provided.

#### See Help

Check how to use it at any time...

```bash
sublime -h
```

#### Run With Defaults

The image used is the one in Docker Hub and the current dir `$PWD`, without the part `/home/$USER` is mapped to same path on the container.

```bash
sublime
```

#### Run With Another Docker Hub Image

Personalize the current Docker Hub `exadra37/sublime-text-3` by extending it and then use it like...

```bash
sublime -i my-docker-hub-image-name
```

#### Run With Local Docker Image

This will build locally, using the same Dockerfile used to build the Docker Hub Image...

```bash
sublime -l
```

#### Run With Another Build

Currently the Sublime Text build defaults to `3126`.

We can build a local Docker Image with a previous or future build of Sublime Text, just by providing a different build number...

```bash
sublime -b 3124
```

#### Run With Custom Developer Workspace

Instead of mapping the current dir as the host workspace, another one can be provided...

```bash
sublime -w /absolute/workspace/path/in/host
```

#### Rebuild Local Docker Image

To rebuild the local image just do like...

```bash
sublime -r
```

#### How to Obtain a Shell Inside Sublime Text Docker Container

For trouble shouting Sublime Text 3 installation we may need to go inside the docker container.

To help us on that, when starting the container the exact command will be printed, and will look like:

```bash
sudo docker exec -it ST3_1486504665 zsh
```
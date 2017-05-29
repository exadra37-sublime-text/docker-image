FROM ubuntu:latest

LABEL "com.exadra37.vendor"="Exadra37"
LABEL com.exadra37.package-name="exadra37-sublime-text-3/docker-image"
LABEL version="0.0.1.0"
LABEL description="Dockerize Sublime Text 3. \
This allow us to run the Sublime Text 3 from inside a Docker Container. \

Advantages: \
    * No need to install the ST3 in our Operating System to try it. \
    * Try the ST3 with many different setups without be afraid to break our OS. \
    * More secure to run, once we can destroy the container when finished, therefore if is compromised it will not \
       infect the OS in our computer. \
    * Keep our OS clean and free of bloated APPs, making easy to upgrade it at any time. \
"

# Removes DBUS warning that should be only seen by Developer
# https://bugs.launchpad.net/ubuntu/+source/at-spi2-core/+bug/1193236
ENV NO_AT_BRIDGE=1

ENV LANG en_GB.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL en_GB.UTF-8
ENV SHELL /bin/bash

# Will not prompt for questions
ARG DEBIAN_FRONTEND=noninteractive

ARG CONTAINER_USER="${CONTAINER_USER:-sublime}"
ARG CONTAINER_UID="${CONTAINER_UID:-1000}"
ARG SUBLIME_BUILD="${SUBLIME_BUILD:-3126}"

RUN apt-get update && \
    apt-get -y upgrade && \

    # Install Required Dependencies
    apt-get -y install \
        locales \
        ca-certificates \
        apt-utils \
        dbus-x11 \
        curl \
        git \
        zsh \
        python \
        php \
        libcanberra-gtk-module \
        libgtk2.0-0 \
        libatk-adaptor \
        libgail-common && \

        # Force Install of missing dependencies
        apt-get -y -f install && \

        # Localization
        locale-gen en_GB.UTF-8 && \

        # Intall Oh My Zsh for root user
        bash -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" && \

        # Add new user
        useradd -m -u ${CONTAINER_UID} -s /usr/bin/zsh ${CONTAINER_USER} && \

        # Intall Oh My Zsh for user
        su "${CONTAINER_USER}" -c 'bash -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"' && \

        # Install Sublime
        curl -O https://download.sublimetext.com/sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb && \
        dpkg -i -R sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb || echo "\n Will force install of missing ST3 dependencies...\n" && \

        # Create default dirs in User home directory necessary for Sublime
        su "${CONTAINER_USER}" -c 'bash -c "mkdir -p ~/.local/share ~/.config/sublime-text-3/{Cache,Local,Index,Packages,Installed\ Packages}"' && \

        # Force installation of missing dependencies for Sublime
        apt-get -y -f install && \
        rm -rvf sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb && \

        # Cleanup
        rm -rf /var/lib/apt/lists/*

USER ${CONTAINER_USER}

WORKDIR /home/${CONTAINER_USER}

# Run Sublime
CMD ["/opt/sublime_text/sublime_text", "-w"]

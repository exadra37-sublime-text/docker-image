FROM elixir:latest

LABEL "com.exadra37.vendor"="Exadra37"
LABEL com.exadra37.package-name="exadra37-sublime-text-3/docker-image"
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

# Will not prompt for questions
ENV DEBIAN_FRONTEND=noninteractive

ARG CONTAINER_USER=elixir
ARG CONTAINER_UID=1000
ARG SUBLIME_BUILD=3143

ARG LANGUAGE_CODE=en
ARG COUNTRY_CODE=GB
ARG ENCODING=UTF-8

ARG LOCALE_STRING="${LANGUAGE_CODE}_${COUNTRY_CODE}"
ARG LOCALIZATION="${LOCALE_STRING}.${ENCODING}"

RUN apt-get update && \
    apt-get -y upgrade && \

    # Install Required Dependencies
    apt-get -y install \
        locales \
        ca-certificates \
        apt-utils \
        inotify-tools \
        dbus-x11 \
        curl \
        git \
        zsh \
        nano \
        python \
        libcanberra-gtk-module \
        libgtk2.0-0 \
        libatk-adaptor \
        libgail-common && \

        # Force Install of missing dependencies
        apt-get -y -f install && \

        # Locales
        echo "${LOCALIZATION} ${ENCODING}" > /etc/locale.gen && \
        locale-gen "${LOCALIZATION}" && \

        # Intall Oh My Zsh for root user
        bash -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" && \

        # Add new user
        useradd -m -u ${CONTAINER_UID} -s /usr/bin/zsh ${CONTAINER_USER} && \

        cat /etc/passwd && \

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

ENV LANG "${LOCALIZATION}"
ENV LANGUAGE "${LOCALE_STRING}:${LANGUAGE_CODE}"
ENV LC_ALL "${LOCALIZATION}"
ENV SHELL /bin/bash

USER ${CONTAINER_USER}

WORKDIR /home/${CONTAINER_USER}

# Run Sublime
CMD ["/opt/sublime_text/sublime_text", "-w"]

FROM ubuntu:latest

MAINTAINER Exadra37

RUN apt-get update && apt-get -y upgrade

# Install Required Dependencies
RUN apt-get -y install \
    ca-certificates \
    curl \
    git \
    python \
    sudo \
    libcanberra-gtk-module \
    libgtk2.0-0 \
    --no-install-recommends

# Force Install of missing dependencies
RUN apt-get -y -f install

# Cleanup
RUN rm -rf /var/lib/apt/lists/*

ARG HOST_USER=${HOST_USER}
ARG HOST_UID=${HOST_UID}
ARG HOST_GID=${HOST_GID}
ARG SUBLIME_BUILD=${SUBLIME_BUILD}

#Add new sudo user
RUN useradd -m ${HOST_USER} && \
    echo "${HOST_USER}:${HOST_USER}" | chpasswd && \
    usermod --shell /bin/bash ${HOST_USER} && \
    usermod -aG sudo ${HOST_USER} && \
    echo "${HOST_USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/${HOST_USER} && \
    chmod 0440 /etc/sudoers.d/${HOST_USER} && \
    usermod  --uid ${HOST_UID} ${HOST_USER} && \
    groupmod --gid ${HOST_GID} ${HOST_USER}

# Install Sublime
RUN curl -O https://download.sublimetext.com/sublime-text_build-${SUBLIME_BUILD}_amd64.deb
RUN dpkg -i -R sublime-text_build-${SUBLIME_BUILD}_amd64.deb
RUN rm -rvf sublime-text_build-${SUBLIME_BUILD}_amd64.deb

# Run Sublime
CMD ["/opt/sublime_text/sublime_text", "-w"]

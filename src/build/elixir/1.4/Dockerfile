FROM exadra37/elixir-dev-cli:1.4

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

RUN apt-get update && \
    apt-get -y upgrade && \

    # Install Required Dependencies
    apt-get -y install \
        dbus-x11 \
        firefox \
        python \
        libcanberra-gtk-module \
        libgtk2.0-0 \
        libatk-adaptor \
        libgail-common && \

        # Force Install of missing dependencies
        apt-get -y -f install && \

        # Install Sublime
        curl -O https://download.sublimetext.com/sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb && \
        dpkg -i -R sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb || echo "\n Will force install of missing ST3 dependencies...\n" && \

        # Force installation of missing dependencies for Sublime
        apt-get -y -f install && \
        rm -rvf sublime-text_build-"${SUBLIME_BUILD}"_amd64.deb && \

        # Cleanup
        rm -rf /var/lib/apt/lists/*

USER ${CONTAINER_USER}

WORKDIR /home/${CONTAINER_USER}

# Run Sublime
CMD ["/opt/sublime_text/sublime_text", "-w"]

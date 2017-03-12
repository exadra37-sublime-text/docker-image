#!/bin/bash
# @author Exadra37(Paulo Silva) <exadra37ingmailpointcom>
# @since  2016/03/10
# @link   https://exadra37.com


########################################################################################################################
# Variables
########################################################################################################################

    USER_NAME="dockerize-sublime"
    IMAGE_NAME="exadra37/sublime-text-3"

    # Where to persist Sublime settings, cache and installed packages.
    HOST_SUBLIME_DIR=/home/"$USER"/"${USER_NAME}"/.docker-sublime
    HOST_SUBLIME_CONFIG_DIR="${HOST_SUBLIME_DIR}"/.config/sublime-text-3

    TIMESTAMP=$( date +"%s" )

    CONTAINER_NAME="ST3_${TIMESTAMP}"

    # Setup X11 server authentication
    # @link http://wiki.ros.org/docker/Tutorials/GUI#The_isolated_way
    XSOCK=/tmp/.X11-unix
    XAUTH="${HOST_SUBLIME_DIR}"/x11dockerize


########################################################################################################################
# Execution
########################################################################################################################

    mkdir -p "${HOST_SUBLIME_CONFIG_DIR}"

    # Setup X11 server bridge between host and container
    touch "${XAUTH}" &&
    xauth nlist "${DISPLAY}" | sed -e 's/^..../ffff/' | xauth -f "${XAUTH}" nmerge -
    chmod 644 "${XAUTH}" # not the most secure way, USE INSTEAD sublime cli

    # Run Container with X11 authentication and using same user in container and host
    # @link http://wiki.ros.org/docker/Tutorials/GUI#The_isolated_way
    #
    # Additional to the above tutorial:
    #   * I set the container --workdir in the host to persist Sublime settings and cache across restarts
    #   * I Also map my developer folder in the host to the container.
    #   * XSOCK and XAUTH only have ready access to the Host, instead of ready and write.
    sudo docker run --rm -it \
        --name="${CONTAINER_NAME}" \
        --workdir="${HOST_SUBLIME_DIR}" \
        --volume="${HOST_SUBLIME_CONFIG_DIR}":/home/"${USER_NAME}"/.config/sublime-text-3 \
        --volume="$PWD":/home/"${USER_NAME}"/developer \
        --volume="${XSOCK}":"${XSOCK}":ro \
        --volume="${XAUTH}":"${XAUTH}":ro \
        --env="XAUTHORITY=${XAUTH}" \
        --env="DISPLAY" \
        --user="${USER_NAME}" \
        "${IMAGE_NAME}"

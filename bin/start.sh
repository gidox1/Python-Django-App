#!/bin/bash

# This script will start a single "disposable" instance and connect the caller to it.
# The instance will link to all infrastructure, including the service containers (if it exists)
IMAGE_NAME="djangoapp"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT="$(dirname "${SCRIPT_DIR}")"

echo " ----- Starting Up Infrastructure Containers -----"

docker-compose -p djangoapp up -d

docker run \
    -i \
    -t \
    -p 8200:8200 \
    -v ${ROOT}:/var/www \
    --env-file=${ROOT}/.env \
    --network=${IMAGE_NAME}_main_network \
    ${IMAGE_NAME} \
    bash

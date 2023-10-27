#!/bin/bash

# Utility script to start the Docker build process.

set -x
set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

GIT_DESCRIBE=$(git describe --tags || echo 0.0.0 | cut -d - -f 1)
GIT_TAG=${GIT_TAG-$GIT_DESCRIBE}
DOCKER_VERSION=$(echo $GIT_TAG | sed -e 's/^v//')

ORG=bihealth
REPO=varfish-cli-ng

docker build . \
    --file utils/docker/Dockerfile \
    --build-arg git_treeish=$GIT_TAG \
    --pull \
    -t ghcr.io/$ORG/$REPO:$DOCKER_VERSION \
    "$@"

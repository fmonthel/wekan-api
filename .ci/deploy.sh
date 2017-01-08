#!/usr/bin/env bash

set -ex

cd ${REPO_DIR}

# Git
git fetch --all
git checkout ${BRANCH}
git reset --hard origin/${BRANCH}

# Python virtual environment
source env/bin/activate

# Install step
make bootstrap

# Reload Apache config
sudo service apache2 reload

allu \
    --skip-auth \
    --type text \
    --tag Jenkins \
    --message "Successfully deployed wekan-api ("$(git rev-parse --abbrev-ref HEAD)", "$(git sha)")."

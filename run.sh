#!/bin/sh

set -e

mkdir -pv ./data

. ./venv/bin/activate
. ./.env

python3 ./mybot.py

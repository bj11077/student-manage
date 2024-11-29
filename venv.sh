#!/bin/bash
path=$(pwd)
mkdir "$path/venv"
python3 -m venv $path/venv
source $path/venv/bin/activate
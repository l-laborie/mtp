#!/bin/bash
# Set env variable to set sqlite data base

ENV=${1:-base}

if [ ! -d "../printmail_env" ];then
    mkdir ../printmail_env
fi
if [ ! -d "../printmail_env/$ENV" ];then
    virtualenv ../printmail_env/$ENV -p /usr/bin/python3.4
fi

source ../printmail_env/$ENV/bin/activate

pip install -r ../requierments/pip/$ENV.txt

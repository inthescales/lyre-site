#!/bin/bash

source $1/env/bin/activate
python3 $1/assets/scripts/wotd.py -p $1

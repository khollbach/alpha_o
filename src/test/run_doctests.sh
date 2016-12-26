#!/bin/bash

cd ../main

for F in *.py; do
    if [ "$F" != "alpha_o.py" ]; then
        ./"$F" $@
    fi
done

#!/bin/bash

. env.sh && \
 ./rki_get_cases.py && \
 ./rki_merge_cases.py && \
 git status


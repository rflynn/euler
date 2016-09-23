#!/bin/sh

factor $(seq 2 120000) | grep '^\([0-9]\+\): \1$' | cat -n | grep '^ 10001\s'

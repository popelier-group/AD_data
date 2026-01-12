#!/usr/bin/env bash

home=$(pwd)
for dir in RUN*/; do
    thisdir=$home/$dir
    [ -d "$thisdir" ] || continue
    echo "Entering $thisdir"
    ( cd "$thisdir" && sbatch submit.sh )
done

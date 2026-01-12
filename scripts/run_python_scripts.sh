#!/usr/bin/env bash

module load anaconda3/2024.02
home=$(pwd)
for dir in RUN*/; do
    thisdir=$home/$dir
    [ -d "$thisdir" ] || continue
    echo "Entering $thisdir"
    ( cd "$thisdir" && python read_energies.py )
done

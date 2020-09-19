#!/bin/bash

root_dir="ModelNet10"
scaled_dir="${root_dir}_scaled"
classes=$(ls $root_dir)

rm -rf $scaled_dir
mkdir $scaled_dir
for class in $classes
do
    if ! [[ $class == *.txt ]]; then
        echo "Processing class ${class} ..."
        mkdir "${scaled_dir}/${class}"
        for t in "train" "test"
        do
            mkdir "${scaled_dir}/${class}/${t}"
            python3 scale_off.py "${root_dir}/${class}/${t}/" "${scaled_dir}/${class}/${t}/" --padding 0
        done
    fi
done
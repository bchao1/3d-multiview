#!/bin/bash

root_dir="ModelNet10"
voxel_dir="${root_dir}_voxelized"
scaled_dir="${root_dir}_scaled"
classes=$(ls $root_dir)

rm -rf $voxel_dir
mkdir $voxel_dir
for class in $classes
do
    if ! [[ $class == *.txt ]]; then
        echo "Processing class ${class} ..."
        mkdir "${voxel_dir}/${class}"
        for t in "train" "test"
        do
            mkdir "${voxel_dir}/${class}/${t}"
            for file in  "${scaled_dir}/${class}/${t}/"*
            do
                IFS='/' read -r -a array <<< "$file"
                filename=${array[-1]}
                IFS='.' read -r -a array <<< "$filename"
                fileid=${array[0]}
                newfile="${voxel_dir}/${class}/${t}/${fileid}.h5"
                voxelize --input $file --output $newfile --center
            done
        done
    fi
done
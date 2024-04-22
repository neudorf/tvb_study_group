#!/bin/bash

# Check if a file path is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <sublist_file_path>"
    exit 1
fi

sublist_file=$1

# Check if the file exists
if [ ! -f "$sublist_file" ]; then
    echo "File not found: $sublist_file"
    exit 1
fi

# Iterate through each line in the file
while read -r sub; do
    sbatch ./sbatch_create_emp_funcfeat.sh "$sub"
done < "$sublist_file"

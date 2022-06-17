#!/usr/bin/python3

# The program initialy checks the hash of a given string in a txt file, and if it has a duplicate anywhere within the txt file. It will remove it. 

import hashlib

# Store the Input and Output files
input_file_path = input("Enter full path of a txt file:")
output_file_path = input("Enter full path for output file:")

# Storing hash in a variable
completed_lines_hash = set()

# Write to the output file 
output_file = open(output_file_path, "w")

# Open the original txt file from input
for line in open(input_file_path, "r"):
    # Store and convert each line in a txt file to md5 hash
    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
    # Check if hash is not already in an output file, if not write to it
    if hashValue not in completed_lines_hash:
        output_file.write(line)
        completed_lines_hash.add(hashValue)

# Close the output file
output_file.close()
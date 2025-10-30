#!/bin/sh
# Ensure flag directory exists
mkdir -p /flag

# Write flag from environment variable to file
if [ ! -z "$FLAG" ]; then
    echo "$FLAG" > /flag/flag.txt
else
    echo "FLAG_NOT_SET" > /flag/flag.txt
fi

# Run the Python app
exec python app.py
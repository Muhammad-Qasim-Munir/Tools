#!/usr/bin/env python3
import mmh3
import sys
import requests

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} [Favicon URL]")
    sys.exit(1)

try:
    response = requests.get(sys.argv[1])
    favicon_data = response.content
    hash_value = mmh3.hash(favicon_data)
    print(f"Favicon hash value: {hash_value}")
except Exception as e:
    print(f"Error occurred: {e}", file=sys.stderr)
    sys.exit(1)

import os
import re

# Define the patterns to search for
patterns = {
    'password': re.compile(r'password\s*=\s*["\'].*?["\']', re.IGNORECASE),
    'secret': re.compile(r'secret\s*=\s*["\'].*?["\']', re.IGNORECASE),
    'key': re.compile(r'key\s*=\s*["\'].*?["\']', re.IGNORECASE),
    'connection_string': re.compile(r'connection\s*string\s*=\s*["\'].*?["\']', re.IGNORECASE),
    'token': re.compile(r'token\s*=\s*["\'].*?["\']', re.IGNORECASE)
}

# Function to scan a file for sensitive information
def scan_file(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        for name, pattern in patterns.items():
            matches = pattern.findall(content)
            for match in matches:
                print(f'Found {name}: {match} in file {filename}')

# Function to recursively scan a directory for C# files
def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            #update to any language
            if file.endswith('.cs'):
                filepath = os.path.join(root, file)
                scan_file(filepath)

# Define the directory to scan
directory_to_scan = '/path/to/your/csharp/project'

# Run the scan
scan_directory(directory_to_scan)

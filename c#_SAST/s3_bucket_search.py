import os
import re

# Define the patterns to search for
patterns = {
    's3_url': re.compile(r's3\.amazonaws\.com[^\s\'";]*', re.IGNORECASE),
    'bucket_name': re.compile(r'BucketName\s*=\s*["\'].*?["\']', re.IGNORECASE),
    'bucket_name_var': re.compile(r'["\'][a-zA-Z0-9-]+\.s3\.amazonaws\.com["\']', re.IGNORECASE),
    's3client': re.compile(r'new\s*S3Client', re.IGNORECASE),
    's3': re.compile(r'S3\b', re.IGNORECASE)
}

# Function to scan a file for AWS S3 references
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
            if file.endswith('.cs'):
                filepath = os.path.join(root, file)
                scan_file(filepath)

# Define the directory to scan
directory_to_scan = '/path/to/your/csharp/project'

# Run the scan
scan_directory(directory_to_scan)

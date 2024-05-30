import re

# Patterns to identify potential vulnerabilities
patterns = {
    "SQL Injection": re.compile(r"\b(SqlCommand|ExecuteNonQuery|ExecuteReader)\b.*(\bSelect\b|\bUpdate\b|\bDelete\b|\bInsert\b).*[\+|].*[\@|\$]", re.IGNORECASE),
    "XSS": re.compile(r"\bResponse\.Write\b.*[\+|].*Request\[", re.IGNORECASE),
    "Hard-coded Secrets": re.compile(r"\"[a-zA-Z0-9]{20,}\"")  # simplistic check for hard-coded strings
}

# Function to scan the C# code
def scan_code(code):
    findings = []

    for vuln, pattern in patterns.items():
        for match in re.finditer(pattern, code):
            findings.append({
                "vulnerability": vuln,
                "match": match.group(),
                "line_number": code[:match.start()].count('\n') + 1
            })

    return findings

# Function to read the file and scan it
def scan_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
        return scan_code(code)

# Function to print the findings
def print_findings(findings):
    if findings:
        for finding in findings:
            print(f"[{finding['vulnerability']}] found at line {finding['line_number']}: {finding['match']}")
    else:
        print("No vulnerabilities found.")

# Main function to scan a list of files
def main(file_paths):
    for file_path in file_paths:
        print(f"Scanning {file_path}...")
        findings = scan_file(file_path)
        print_findings(findings)
        print()

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python sast_tool.py <file1.cs> <file2.cs> ...")
    else:
        main(sys.argv[1:])

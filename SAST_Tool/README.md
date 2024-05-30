Nicole Smith basic SAST Tool for C# web applications.

<h2>How It Works</h2><br>
1. Patterns: The script defines regex patterns to identify SQL injection, XSS, and hard-coded secrets in the C# code.<br>
2. Scanning: The scan_code function applies these patterns to the code and records any matches.<br>
3. File Reading: The scan_file function reads the content of a given file and scans it for vulnerabilities.<br>
3. Output: The findings are printed to the console, indicating the type of vulnerability, the line number, and the code snippet that matched the pattern.
<br><br>
<h2>Usage</h2><br>
Save the script as sast_tool.py and run it from the command line, providing the paths to the C# files you want to scan:
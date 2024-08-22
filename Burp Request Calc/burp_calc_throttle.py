# This script calculates the number of requests per hour based on user input for milliseconds per request.

# Number of concurrent requests
concurrent_requests = 4

# Get milliseconds per request from user input
milliseconds_per_request = int(input("Enter milliseconds per request: "))

# Convert milliseconds to hours
milliseconds_per_hour = 60 * 60 * 1000

# Calculate the number of requests per hour
requests_per_hour = (milliseconds_per_hour / milliseconds_per_request) * concurrent_requests

# Output the result
print(f"Requests per hour: {requests_per_hour:.2f}")
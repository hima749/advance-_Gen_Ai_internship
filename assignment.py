#1. User Login Check
username = "admin"
password = "1234"

input_username = "admin"
input_password = "1234"

if input_username == username and input_password == password:
    print("Login Successful")
else:
    print("Invalid Credentials")

#2. Pass / Fail Analyzer
print("----- Pass / Fail Analyzer -----")

marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Pass Students:", pass_count)
print("Fail Students:", fail_count)

print("----- End of Pass / Fail Analyzer -----")

#3. Simple Data Cleaner
names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned_name = name.strip().lower()
    cleaned_names.append(cleaned_name)

print("Cleaned Names:", cleaned_names)

#4. Message Length Analyzer
messages = ["Hi", "Welcome to the platform", "OK"]

for message in messages:
    length = len(message)
    print(f"Message: '{message}' | Length: {length}")

    if length > 10:
        print("Message longer than 10 characters")

#5. Error Message Detector
logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

for log in logs:
    if log == "ERROR":
        error_count += 1

print("Total ERROR messages:", error_count)
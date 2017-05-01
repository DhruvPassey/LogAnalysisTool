import splunklib.client as client

HOST = "localhost"
PORT = 8089
#USERNAME = "admin"
#PASSWORD = "Asia1996"
USERNAME = str(raw_input("Enter Splunk Username : "))
PASSWORD = str(raw_input("Enter Splunk Password : "))

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Print installed apps to the console to verify login
for app in service.apps:
    print app.name

# Create a new index
#mynewindex = service.indexes.create("index_test")

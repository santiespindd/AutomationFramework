import inspect
"CONSTANTS"

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"

#Function name

def whoami():
    return inspect.stack()[1][3]
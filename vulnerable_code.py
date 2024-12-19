import os
import requests
import boto3

# test2

# Hardcoded secret (to trigger secret scanning tools)
API_KEY = "12345-SECRET-KEY"

# AWS Secret (for example purposes)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

# Vulnerable function: uses user input unsafely
def insecure_eval():
    user_input = input("Enter command: ")
    eval(user_input)  # Dangerous: allows arbitrary code execution

# Dependency with known vulnerability
def vulnerable_dependency():
    # Using a vulnerable version of a package
    import flask  # Example of old vulnerable package

    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        return "This is a vulnerable app"

    app.run()

# Insecure HTTP request (no SSL verification)
def insecure_http_request():
    response = requests.get("http://example.com", verify=False)
    print("Response:", response.text)

# Entry point
if __name__ == "__main__":
    print("Starting vulnerable code...")
    insecure_eval()  # Triggers SAST
    vulnerable_dependency()  # Triggers dependency check
    insecure_http_request()  # Triggers SAST

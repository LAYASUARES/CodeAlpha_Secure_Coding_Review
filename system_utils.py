import os

def run_command(cmd):
    # Vulnerabilities: command injection
    return os.popen(cmd).read()

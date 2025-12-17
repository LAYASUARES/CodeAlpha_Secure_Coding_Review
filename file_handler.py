def read_file(filename):
    # Vulnerability: User can input paths such as ../../etc/passwd
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

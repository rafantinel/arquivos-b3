import os

# Calculate file size in MB's
def get_size(file):
    return round(os.path.getsize(file) / 1000000, 2)

# Count file rows
def count_rows(file):
    with open(file, "r") as f:
        count = sum(1 for row in f)  
    return count

# Format exported file
def format_file(header, file):
    rv = []
    rv.append(f"{header[0]},{header[1]},{header[2]},{header[3]}")
    with open(file, "r", newline="") as f:
        for i, row in enumerate(f):
            if i > 0 and row[2:10].isnumeric():
                date = f"{row[2:10][6:8]}/{row[2:10][4:6]}/{row[2:10][0:4]}"
                rv.append(f"{date},{row[12:24].strip()},{row[52:56].strip()},{row[108:121]}")
    return rv

# Read file codes and return unique values
def get_code(file):
    rv = set()
    with open(file, "r", newline="") as f:
        for i, row in enumerate(f):
            if i > 0 and row[2:10].isnumeric():
                 rv.add(row[12:24].strip())
    return list(rv)
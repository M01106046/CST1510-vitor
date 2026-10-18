# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
with open("records.txt", "w") as f:
    f.write("R-001\n")
    f.write("R-002\n")

with open("records.txt") as f:
    print(f.read())

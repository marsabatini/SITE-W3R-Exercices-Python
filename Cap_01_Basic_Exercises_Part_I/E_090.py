# This program creates a copy of its own source code

def copySource(source, fin):
    with open(source) as f, open(fin, 'w') as d:
        d.write(f.read())
        copySource("E_001.py", "E_001b.py")
        with open("E_001b.py", 'r') as file:
            for line in file:
                print(line, end='')
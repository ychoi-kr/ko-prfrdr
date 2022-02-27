import argparse


def readfile(filename, encoding):
    with open(filename, "rt", encoding=encoding) as infile:
        return infile.readlines()

def writefile(filename, content, encoding):
    with open(filename, "wt", encoding=encoding) as outfile:
        outfile.writelines(content)

def main(filename):
    try:
        encoding = "utf8"
        content = readfile(filename, encoding=encoding)
    except UnicodeDecodeError:
        encoding = None
        content = readfile(filename, encoding=encoding)
        
    writefile(filename, sorted(content, key=str.casefold), encoding)

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    main(args.filename)

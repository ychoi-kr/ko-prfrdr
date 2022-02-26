import argparse


def sort(infilename, outfilename):
    with open(infilename, "rt", encoding="utf8") as infile:
        content = infile.readlines()
        
    with open(outfilename, "wt", encoding="utf8") as outfile:
        outfile.writelines(sorted(content))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    sort(args.filename, args.filename)

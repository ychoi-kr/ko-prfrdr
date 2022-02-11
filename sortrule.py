import json
from pathlib import Path
import sys


def sortrule(filename):
    infilename = filename
    j = json.load(open(infilename))
    j.sort(key=lambda x: x["desc"])
    
    outfilename = Path(filename).stem + '2' + Path(filename).suffix
    with open(outfilename, 'w') as f:
        f.write(json.dumps(j, ensure_ascii=False, indent=2, separators=(',', ': ')))

if __name__ == '__main__':
    sortrule(sys.argv[1])


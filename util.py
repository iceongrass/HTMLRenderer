def lines(file):
    for line in file: yield line
    yield "\n"

def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield "".join(block).strip()
            block = []

def test():
    import sys
    args = sys.argv
#    print args
    file = open (args[1])
    print list(blocks(file))
    file.close()

if __name__ == '__main__': test()



import sys


# function of initial state parse
def parser(file):
    # read the first line in the file
    line = file.readline()
    # split the line in to words
    words = line.split()
    # list of initial state declaration
    init_state = []
    # verification if the line contains the initial state: words
    if words[0] == "Initial" and words[1] == "state:":
        # retrieve the whole line without the Initial state words and put it in list
        words = words[2:]
        # loop over the previous line
        for i in words:
            # add to the list each state as tuple
            init_state.append((i[:i.find('(')], i[(i.find('(') + 1):(i.find(')'))]))
    return init_state


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./strips FILE.TXT")
        exit(1)
# read the file insert in command line
    with open(sys.argv[1]) as f:
        print(parser(f))
    exit(0)

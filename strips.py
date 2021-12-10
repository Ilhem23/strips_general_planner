import sys


# general function to parse return the name and argument in tuple
def state_parser(line):
    name = line[:line.find('(')]
    rest_of_the_line = line[line.find(')') + 1:]
    rest_of_the_line = rest_of_the_line.strip(', ')
    line = line[line.find('(') + 1:line.find(')')]
    args = line.split(',')
    args = [a.strip(' ') for a in args]
    return name, args, rest_of_the_line


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
        # convert to string
        new_line = ' '.join(words)
        # loop over the new string and extract the name and the argument, delete the extracted one and return
        # the new line without the extracted one
        while len(new_line):
            name, args, new_line = state_parser(new_line)
            init_state.append((name, args))
    return init_state


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./strips FILE.TXT")
        exit(1)
    # read the file insert in command line
    with open(sys.argv[1]) as f:
        print(parser(f))
    exit(0)

import sys

Z_LETTER = 122


def increment(c, i):
    if ord(c) + i > Z_LETTER:
        return chr(ord(c) + i - 26)
    return chr(ord(c) + i)


def rot_string(s, incrementation):
    return "".join(map(lambda c: increment(c, incrementation), s))


def code_breaker(code):
    solutions = []
    for i in range(1, 26):
        solutions.append(rot_string(code, i))
    return solutions


def print_solutions(code):
    print("\n".join(code))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Send a message to decode")
        exit(-1)
    code = sys.argv[1]
    s = code_breaker(code.lower())
    print_solutions(s)

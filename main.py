import time


def main():
    start = time.time()
    max = 10000
    fizzbuzz_list = [
        ["fizz", 3],
        ["buzz", 5],
	["rezz", 23]
    ]
    fizzbuzzed_list = []
    for i in range(1, max):
        name = ""
        for tups in fizzbuzz_list:
            if i % tups[1] == 0:
                name += tups[0]
        if name == "":
            fizzbuzzed_list.append(i)
        else:
            fizzbuzzed_list.append(name)
    print(fizzbuzzed_list)
    end = time.time()
    time_elapsed = end - start
    print(f"Execution time was: {time_elapsed} seconds")
main()

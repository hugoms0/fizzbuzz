import time


def main():
    start = time.time()
    max = 10000000
    fizzbuzz_list = [
        ["fizz", 3],
        ["buzz", 5]
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
    end = time.time()
    time_elapsed = end - start
    print(time_elapsed)
main()

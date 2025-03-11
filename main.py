import time


def main():
    start = time.time()
    max = 350
    fizzbuzz_list = [
        ["fizz", 3],
        ["buzz", 5],
        ["rezz", 23]
    ]
    fizzbuzzed_list = []
    for i in range(1, max + 1):
        name = ""
        for tups in fizzbuzz_list:
            if i % tups[1] == 0:
                name += tups[0]
        if name == "":
            fizzbuzzed_list.append(i)
        else:
            fizzbuzzed_list.append(name)
    
    with open("fizzbuzz_output.txt", "w") as file:
        for item in fizzbuzzed_list:
            file.write(f"{item}\n")

    # print(fizzbuzzed_list)

    end = time.time()
    time_elapsed = end - start
    print(f"Execution time was: {time_elapsed} seconds")
main()

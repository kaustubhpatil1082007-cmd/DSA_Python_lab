# DSA with Python - Algorithm Analysis Labs
# Install graphs library: pip install matplotlib

import time
import random
import statistics
import platform
import sys
import csv
import math
import matplotlib.pyplot as plt

random.seed(10)


def measure(func, runs=5):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        func()
        times.append(time.perf_counter() - start)
    return statistics.median(times)

# ---------------- Lab 2 ----------------

def prefix_average1(a):
    result = []
    for j in range(len(a)):
        total = 0
        for i in range(j + 1):
            total += a[i]
        result.append(total / (j + 1))
    return result


def prefix_average2(a):
    result = []
    total = 0
    for j in range(len(a)):
        total += a[j]
        result.append(total / (j + 1))
    return result


def lab2():
    examples = [[], [5], [1, 2, 3], [-1, -2, -3], [2, -4, 6, -8]]

    print("\nLAB 2 - Validation")
    for a in examples:
        first, second = prefix_average1(a), prefix_average2(a)
        assert len(first) == len(second)
        assert all(math.isclose(x, y) for x, y in zip(first, second))
        print(a, "->", second)

    results = []
    for n in [100, 500, 1000, 2000, 4000, 8000]:
        a = [random.randint(-50, 50) for _ in range(n)]
        t1 = measure(lambda: prefix_average1(a))
        t2 = measure(lambda: prefix_average2(a))
        results.append((n, t1, t2))

    with open("lab2_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "prefix_average1", "prefix_average2"])
        writer.writerows(results)

    print("\nn       Prefix 1 O(n^2)    Prefix 2 O(n)")
    for n, t1, t2 in results:
        print(f"{n:<8} {t1:.6f}             {t2:.6f}")

    plt.figure()
    plt.plot([r[0] for r in results], [r[1] for r in results],
             marker="o", label="prefix_average1 - O(n^2)")
    plt.plot([r[0] for r in results], [r[2] for r in results],
             marker="o", label="prefix_average2 - O(n)")
    plt.xlabel("Input size (n)")
    plt.ylabel("Median time (seconds)")
    plt.title("Lab 2 - Prefix average comparison")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("lab2_plot.png")
    plt.show()
    plt.close()




if __name__ == "__main__":
    print("Python:", sys.version.split()[0])
    print("Platform:", platform.platform())
    print("Median time from 5 trials is reported.")
    lab2()
    print("\nDone! Lab 2 CSV file and plot have been saved.")

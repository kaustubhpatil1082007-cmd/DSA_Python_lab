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

# ---------------- Lab 1 ----------------

def binary_search(a, x):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def pair_counter(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count


def subset_count(a):
    count = 0
    for mask in range(2 ** len(a)):
        subset = [a[i] for i in range(len(a)) if mask & (1 << i)]
        count += 1
    return count


def lab1():
    results = []
    sizes = {
        "indexing": [1000, 10000, 100000, 500000],
        "binary search": [1000, 10000, 100000, 500000],
        "linear search": [1000, 5000, 10000, 20000],
        "merge sort": [500, 1000, 2000, 4000, 8000],
        "pair counter": [100, 250, 500, 1000, 2000],
        "subset count": [4, 6, 8, 10, 12, 14, 16]
    }

    for n in sizes["indexing"]:
        a = list(range(n))
        results.append(("indexing", n, measure(lambda: a[n // 2])))

    for n in sizes["binary search"]:
        a = list(range(n))
        results.append(("binary search", n, measure(lambda: binary_search(a, n - 1))))

    for n in sizes["linear search"]:
        a = list(range(n))
        results.append(("linear search", n, measure(lambda: linear_search(a, -1))))

    for n in sizes["merge sort"]:
        a = [random.randint(0, n * 10) for _ in range(n)]
        results.append(("merge sort", n, measure(lambda: merge_sort(a))))

    for n in sizes["pair counter"]:
        results.append(("pair counter", n, measure(lambda: pair_counter(n))))

    for n in sizes["subset count"]:
        a = list(range(n))
        results.append(("subset count", n, measure(lambda: subset_count(a), 5)))

    with open("lab1_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "n", "Median time"])
        writer.writerows(results)

    growth = {
        "indexing": (lambda n: 1, "O(1)"),
        "binary search": (lambda n: math.log2(n), "O(log n)"),
        "linear search": (lambda n: n, "O(n)"),
        "merge sort": (lambda n: n * math.log2(n), "O(n log n)"),
        "pair counter": (lambda n: n ** 2, "O(n^2)"),
        "subset count": (lambda n: n * 2 ** n, "O(n * 2^n)")
    }

    print("\nLAB 1")
    print("Algorithm          n       Median time    Bound")
    for name, n, t in results:
        print(f"{name:18} {n:<8} {t:.6f}       {growth[name][1]}")

    for normalized in [False, True]:
        plt.figure()
        for name, (formula, _) in growth.items():
            data = [r for r in results if r[0] == name]
            y = [r[2] / formula(r[1]) for r in data] if normalized else [r[2] for r in data]
            plt.plot([r[1] for r in data], y, marker="o", label=name)

        plt.xlabel("Input size (n)")
        plt.ylabel("Time / growth" if normalized else "Median time (seconds)")
        plt.title("Lab 1 - Normalized timings" if normalized else "Lab 1 - Execution times")
        plt.yscale("log")
        plt.legend(fontsize=8)
        plt.grid()
        plt.tight_layout()
        plt.savefig("lab1_normalized.png" if normalized else "lab1_plot.png")
        #plt.show()
        plt.close()




if __name__ == "__main__":
    print("Python:", sys.version.split()[0])
    print("Platform:", platform.platform())
    print("Median time from 5 trials is reported.")
    lab1()
    print("\nDone! Lab 1 CSV files and plots have been saved.")

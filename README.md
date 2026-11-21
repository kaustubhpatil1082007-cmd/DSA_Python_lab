# DSA in Python - Assignment 2 - Lab Work 
This repository contains the two lab assignments, separated into two Python files.

## Files

- `lab1.py` - Lab 1: Benchmarking Algorithmic Growth Rates
- `lab2.py` - Lab 2: Prefix Averages
- `requirements.txt` - plotting dependency

## Run

Install matplotlib:

```bash
python -m pip install -r requirements.txt
```

Run Lab 1:

```bash
python lab1_benchmarking.py
```

Run Lab 2:

```bash
python lab2_prefix_averages.py
```

Each program prints the Python version and platform, uses median timing over repeated trials, and saves its CSV data and plots in the current folder.

## Lab 1 comparison table

| Algorithm | Theoretical bound | Expected measured trend | Experimental limitation |
|---|---|---|---|
| List indexing | O(1) | Almost constant | Timer overhead is noticeable for very short operations. |
| Binary search | O(log n) | Slow increase | Input must be sorted; timings are very small. |
| Linear search | O(n) | Roughly linear | The code searches for an absent value, so it scans the full list. |
| Merge sort | O(n log n) | Between linear and quadratic | Slicing and temporary lists add overhead. |
| Pair counter | O(n^2) | Rapid increase | Large input sizes take much longer. |
| Subset count | O(n * 2^n) in this implementation | Exponential increase | Only small input sizes are practical. |

The subset function visits `2^n` masks and builds each subset by checking up to `n` elements, so this implementation takes O(n * 2^n) time.

## Lab 2 operation-count derivation

For `prefix_average1`, the inner loop runs 1, 2, 3, ..., n times.

Total additions:

`1 + 2 + ... + n = n(n + 1) / 2`

Therefore, its time complexity is O(n^2).

For `prefix_average2`, the running sum is updated once for each element. Therefore, its time complexity is O(n).

The validation examples include empty, singleton, positive, negative and mixed-value inputs.

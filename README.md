# DSA with Python - Algorithm Analysis Labs

This repository contains the two lab assignments in separate Python files. The code follows a simple, student-style approach.

## Files

- `lab1_benchmarking.py` - Lab 1: Benchmarking Algorithmic Growth Rates
- `lab2_prefix_averages.py` - Lab 2: Prefix Averages
- `requirements.txt` - Required plotting library

## How to run

Install the required library:

```bash
python -m pip install -r requirements.txt
```

Run each lab:

```bash
python lab1_benchmarking.py
python lab2_prefix_averages.py
```

The programs print the Python version and platform. They use repeated measurements and report the median execution time. Input generation and validation are kept outside the timed function calls. The programs save timing data as CSV files and graphs as PNG files.

## Lab 1: Benchmarking Algorithmic Growth Rates

### Algorithms and theoretical complexity

| Algorithm | Theoretical time complexity | Expected trend | Experimental limitation |
|---|---|---|---|
| List indexing | O(1) | Nearly constant time | The operation is very short, so timer and interpreter overhead can be significant. |
| Binary search | O(log n) | Very slow increase | The input must be sorted, and the measured times may be close to timer overhead. |
| Linear search | O(n) | Approximately proportional to n | The experiment searches for an absent value, so the whole list is scanned. |
| Merge sort | O(n log n) | Faster growth than linear, slower than quadratic | Slicing, temporary lists and Python object handling add overhead. |
| Pair counter | O(n²) | Rapid increase as n grows | Large inputs require many loop iterations and take substantially longer. |
| Subset enumeration | O(n · 2ⁿ) for this implementation | Exponential growth | Only small input sizes are practical. |

The subset-enumeration function considers all `2ⁿ` masks. For each mask, it checks up to `n` positions to construct a subset. Therefore, this implementation takes O(n · 2ⁿ) time.

### How to interpret the measured results

Use the values in `lab1_results.csv` and the generated plots to compare the observed behaviour with the theoretical bounds above. The expected patterns are:

- **List indexing:** execution time should remain approximately constant as the list gets larger.
- **Binary search:** execution time should increase slowly because the search interval is approximately halved at each step.
- **Linear search:** execution time should increase roughly in proportion to the number of elements. The absent search target makes this a worst-case scan.
- **Merge sort:** execution time should increase approximately with n log₂(n). Its measured time also includes Python-level overhead, list slicing and temporary-list allocation.
- **Pair counter:** execution time should rise much faster than linear search because the number of examined pairs grows quadratically.
- **Subset enumeration:** execution time should rise very rapidly as n increases because the number of subsets doubles whenever n increases by one, with additional work to construct each subset.

The measured values will not match the theoretical functions exactly. Big-O notation describes how growth behaves for large n; it does not specify the constant multiplier or all lower-order terms. For small inputs, fixed costs such as function calls, loop setup, object allocation and `time.perf_counter()` overhead can be a large part of the total measured time. These costs can make two algorithms appear closer in performance than their asymptotic complexities suggest.

Python interpreter overhead also affects the algorithms differently. For example, a Python loop performs interpreter-level work on every iteration, while list indexing is a single operation. Memory allocation and cache effects can also influence the results. The selected input sizes are therefore limited to keep the quadratic and exponential experiments practical.

When writing the final observation from your run, refer to the actual CSV and plots. State whether each measured curve follows the expected trend, and mention any small-size irregularities rather than claiming an exact theoretical match.

## Lab 2: Prefix Averages — Quadratic versus Linear Time

### Implementations and operation counts

For `prefix_average1`, the sum for each prefix is recomputed using a nested loop. The inner loop performs 1, 2, 3, ..., n additions.

The total number of additions is:

`1 + 2 + ... + n = n(n + 1) / 2`

The dominant term is proportional to n², so `prefix_average1` has O(n²) time complexity.

For `prefix_average2`, a running sum is updated once for each new element. Each iteration performs a constant amount of work, so the total work is proportional to n and the algorithm has O(n) time complexity.

### Validation and empty input

The implementations are checked using empty, singleton, positive, negative and mixed-value sequences. Both functions return an empty list for empty input. Their corresponding outputs are compared with a tolerance using `math.isclose()`.

### Numerical precision

Both methods calculate the same mathematical prefix averages, but Python floating-point numbers represent many decimal values approximately. Consequently, rounding can occur during addition and division. The two implementations may accumulate rounding errors in slightly different orders, so their results should be compared with a small numerical tolerance rather than requiring exact equality. For ordinary input sizes and values, any differences are generally expected to be very small.

### Performance observations and crossover

The quadratic implementation repeats earlier additions for every prefix, while the running-sum implementation reuses the sum already calculated. As n increases, the amount of repeated work in `prefix_average1` grows much faster.

For small inputs, the measured difference may be modest because fixed Python and timing overhead can dominate. At larger input sizes, the quadratic method should take increasingly longer, while the linear method should grow much more slowly.

The input size at which the linear implementation becomes noticeably faster is an experimental result, not a fixed theoretical constant. Identify it from `lab2_results.csv`: compare the two median-time columns at each n and report the first size where the difference is clear and remains evident for larger sizes. The exact crossover can vary with the computer, Python version and system load.

## Experimental limitations

- Timings can vary with background processes, CPU frequency changes and system load.
- Very short operations are difficult to measure accurately because timer and interpreter overhead are significant.
- Big-O describes asymptotic growth, not exact execution time for every input size.
- Results are specific to the tested Python implementation, machine and input sizes.

## Generated output files

After running the scripts, the following files are created:

- `lab1_results.csv`
- `lab1_plot.png`
- `lab1_normalized.png`
- `lab2_results.csv`
- `lab2_plot.png`

## Lab 1: Actual Experimental Observations

The experimental results broadly agree with the theoretical time complexities of the implemented algorithms.

### Measured Results

| Algorithm | Input size (n) | Initial time | Final time | Observed behaviour |
|---|---:|---:|---:|---|
| List indexing | 1,000–500,000 | 0.00000060 s | 0.00000030 s | Nearly constant |
| Binary search | 1,000–500,000 | 0.00000180 s | 0.00000280 s | Very slow increase |
| Linear search | 1,000–20,000 | 0.00004530 s | 0.00067820 s | Approximately linear |
| Merge sort | 500–8,000 | 0.000693 s | 0.019409 s | Consistent with n log n |
| Pair counter | 100–2,000 | 0.000139 s | 0.069071 s | Rapid quadratic growth |
| Subset enumeration | 4–16 | 0.00000780 s | 0.086779 s | Rapid exponential growth |

### Discussion of Results

- **List indexing – O(1):** Execution time remained nearly constant even when the input size increased from 1,000 to 500,000.
- **Binary search – O(log n):** Execution time increased only slightly because the search interval is approximately halved at every iteration.
- **Linear search – O(n):** Execution time increased approximately in proportion to the input size. Since the search target was absent, the entire list was scanned.
- **Merge sort – O(n log n):** Execution time increased with input size, following the expected n log n growth pattern.
- **Pair counter – O(n²):** Execution time increased rapidly because the number of pair comparisons grows quadratically.
- **Subset enumeration – O(n · 2ⁿ):** Execution time increased extremely rapidly because the number of possible subsets doubles whenever n increases by one, with additional work required to construct each subset.

### Experimental Limitations and Interpretation

The experimental results generally follow the expected theoretical complexity trends. However, measured execution times are affected by several factors:

1. **Constant factors:** Different operations have different execution costs, even when they have similar asymptotic complexity.
2. **Lower-order terms:** These can influence execution time, particularly for smaller input sizes.
3. **Python interpreter overhead:** Function calls, loops and object handling contribute additional execution time.
4. **Memory allocation:** Algorithms such as merge sort create temporary lists, which introduce additional overhead.
5. **Timer resolution:** Very short operations, such as list indexing, are difficult to measure accurately.

Therefore, the measured execution times may not follow theoretical growth functions perfectly. Nevertheless, the overall experimental trends support the expected complexity classes.

---

## Lab 2: Actual Experimental Results

The following table presents the measured execution times of both prefix-average implementations. The values have been converted from seconds to milliseconds.

### Measured Timing Results

| Input size (n) | prefix_average1 – O(n²) (ms) | prefix_average2 – O(n) (ms) |
|---:|---:|---:|
| 100 | 0.241 | 0.015 |
| 500 | 5.314 | 0.076 |
| 1,000 | 26.906 | 0.197 |
| 2,000 | 127.240 | 0.454 |
| 4,000 | 669.088 | 0.600 |
| 8,000 | 1,873.111 | 0.894 |

### Discussion of Experimental Results

The experimental measurements clearly demonstrate the performance difference between the two implementations.

- The quadratic implementation, `prefix_average1`, becomes increasingly slower as the input size increases.
- The linear implementation, `prefix_average2`, exhibits significantly slower growth because it maintains a running sum instead of repeatedly recalculating previous sums.
- At n = 100, the linear implementation is already approximately 15.6 times faster.
- At n = 1,000, it is approximately 136.8 times faster.
- At n = 8,000, it is approximately 2,095.9 times faster.

The linear implementation was already noticeably faster at the smallest tested input size (n = 100). Its performance advantage becomes increasingly significant as the input size grows.

These results experimentally support the theoretical conclusion that O(n) is considerably more efficient than O(n²) for calculating prefix averages.

### Numerical Precision

Both implementations calculate the same mathematical prefix averages. However, Python floating-point numbers represent many decimal values approximately, which can introduce small rounding errors during arithmetic operations.

The two implementations may accumulate floating-point errors in slightly different orders. Therefore, their outputs are compared using `math.isclose()` instead of requiring exact equality.

For ordinary input sizes and values, any differences are expected to be very small.

---

## Experimental Setup

The experiments were conducted using the following environment and methodology:

| Parameter | Description |
|---|---|
| Programming language | Python 3.13.7 |
| Operating system | Windows 11 |
| Processor | Intel Core i5-1235U |
| Timing function | `time.perf_counter()` |
| Measurement method | Median execution time |
| Repeated measurements | Multiple trials |
| Plotting library | Matplotlib |
| Input generation | Outside the timed section |
| Experimental data | Stored in CSV files |

The same measurement approach was used to compare the algorithms. Input generation and validation were performed outside the timed sections to avoid affecting the measured execution times.


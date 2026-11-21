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

Keep these generated files in the repository when submitting so that the experimental timing data and plots are available alongside the source code.

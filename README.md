# Advents of Code solutions

My solutions for prior advents of code years.
The order of solving is:
2020 -> 2015 -> 2021 -> 2022

Plan is to revisit code again and update it with cleaner code.


aocdl: https://github.com/GreenLightning/advent-of-code-downloader

## Run a puzzle file

Use `puzzleCaller.py` with an input file and the exact Python file to run:

```bash
python3 puzzleCaller.py \
  --input aoc/year2015/day07/input.txt \
  --file aoc/year2015/day07/day7.original.py
```

Filenames do not need to follow the normal `dayN.py` pattern, so another
version can be selected directly:

```bash
python3 puzzleCaller.py \
  --input aoc/year2015/day07/input.txt \
  --file aoc/year2015/day07/day7.2.original.py
```

By default the caller runs a function named `puzzle`. Select a different
function with `--function`:

```bash
python3 puzzleCaller.py --input path/to/input.txt --file path/to/solution.py \
  --function function_name
```

The older `--path`/`-p` option remains an alias for `--file`/`-f`.
# 🎄 Advent of Code 2022

My solutions for 2022. Python and C.

I try to focus a bit on clean code, that is also performant on larger inputs.

Therefore, I generated larger inputs, that are similar to the original ones to test performance.

Execute all scripts from the base directory `2022`, like so:
```sh
# Python
python3 python/dayXX.py

# C
mkdir c/build
gcc -std=c17 c/dayXX.c -o c/build/dayXX
./c/build/dayXX
```

## Performance test results

- CPU: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- RAM: 8 GB

- Python: cpython 3.11.1
- C: gcc 10.2.1 C17

All results are mean results of 10 runs using [multitime](https://github.com/ltratt/multitime) in seconds.

### Day 1

All results with input `day01_large.txt`.

- C
  - 0.023
- Python
  - a: 0.207
  - b: 0.177
  - c: 0.170

Notes on memory: Python solutions b and c require lots of memory, since all data is loaded at once.

### Day 2

All results with input `day02_large.txt`.

- C
  - 0.019
- Python
  - a: 0.617
  - b: 1.267

### Day 3

All results with input `day03_large.txt`.

- C
  - 0.144
- Python
  - a: 0.324
  - b: 3.765
  - c: ----- (did not finish in about 10 min 🤨)
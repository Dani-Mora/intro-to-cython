## Intro to Cython

This is my first trial to using Cython for optimizing Python code. I have used this [blog post](https://www.peterbaumgartner.com/blog/intro-to-just-enough-cython-to-be-useful/)
as inspiration.

## Set up

Make sure you create a separate Python 3.8+ environment and then type:

```bash
make setup
```

## Experiment

We have implemented quicksort algorithm and then iteratively optimized it using the steps described
in the blog post mentioned above.

### Vanilla Python

First, we start by computing the baseline using vanilla Python:

```bash
make time_original
```

This retrieves an average close to 5 seconds in our machine.

### Compile using Cython

Then we can check speed up if we only change file extension to ".pyx" and compile using Cython, 
without any additional changes in the code.

```bash
make time_compile
```

Sorting takes now around 3.8 seconds in our machine. This is ~25% time reduction already.

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

### Add C types

After that, we can proceed replacing function definitions to use C types, and test it
by typing:

```bash
make time_ctypes
```

This gives us an average time around 2 seconds. We are achieving a ~48% absolute reduction this time.

### Optimizing using memoryview

Finally, we can use memoryviews (array views), which should let us further optimize our
sorting code. We can run it by typing:

```bash
make time_memviews
```

This results into an average time of ~0.15 seconds. It is an absolute time reduction of around
~92% given the previous step and around 33 times faster than the original approach!

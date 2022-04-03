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

First, we start by computing the baseline using vanilla Python:

```bash
make time_original
```

This retrieved an average close to 5 seconds in our machine.

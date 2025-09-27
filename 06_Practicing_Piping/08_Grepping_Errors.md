# Grepping errors

Using grep on errors using `|` and `>&` instead of redirecting it onto a file

## My solve
**Flag** `pwn.college{w8WWActfV72ZQggRn9MhMkuMPlo.QX1ATO0wCO2gjNzEzW}`
- The challenge requires us to use live grepping on the standard error which contains the flag

```
/challenge/run 2>& 1 | grep "pwn.college"
```

## What I learned
We can use `>&` to redirect one FD to another, in this case we are redirecting the stderr to stdout as piping only works on the output

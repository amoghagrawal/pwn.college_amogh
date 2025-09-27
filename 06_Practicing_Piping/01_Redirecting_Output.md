# Redirecting Output

Using `>` to force the output of the `echo` command to a file called `COLLEGE`

## My solve
**Flag** `pwn.college{YF5jYk0Cr0W9IvYvYRpnryuyx0J.QX0YTN0wCO2gjNzEzW}`

```
echo PWN > COLLEGE
```

## What I learned
`stdin` is the channel in which the input is taken, `stdout` is the output channel and `stderr` is the error channel. We can redirect the output using `>`

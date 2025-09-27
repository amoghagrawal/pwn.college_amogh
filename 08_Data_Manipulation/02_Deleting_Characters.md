# Deleting Characters

Using `tr -d` to delete the unwanted characters to obtain the correct flag

## My solve
**Flag** `pwn.college{EuUCp0kt4H3fAeXRyG_RjaWjBTV.0FNxEzNxwCO2gjNzEzW}`
- The flag has unwanted "^" and "%" characters that we have to remove using `tr -d`

```
/challenge/run | tr -d '^%'
```

## What I learned
We can use `tr -d` to delete characters
# Exclusionary Globbing

Using `!` or `^` in `[]` to show the results not containing the keywords

## My solve
**Flag** `pwn.college{4dchsAevKs_X_b83R4vbjt0RIiq.QX2IDO0wCO2gjNzEzW}`
- Tried running `/challenge/run *[^pwn]*` but it had the word `pwning` in the result which was unwanted
- `[^pwn]*` gave the expected result
```
cd /challenge/files
/challenge/run [^pwn]*
```

## What I learned
We can use `!` or `^` in newer bash versions with the `[]` glob to show the files that dont start with the given arguements

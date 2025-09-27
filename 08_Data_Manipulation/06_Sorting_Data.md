# Sorting Data

Using `sort` to sort the output to obtain the correct flag in a list of fake flags

## My solve
**Flag** `pwn.college{AGpi9cABIO2p2cH2NYeAD7DHjg2.0FM0MDOxwCO2gjNzEzW}`
- The challenge requires us to sort the text file in order to obtain the flag which would be present at the bottom of the list

```
sort /challenge/flags.txt
```

## What I learned
The `sort` command can be used to sort a file alphabetically by default or, `-r` to do it in reverse, `-n` for numbers, `-u` to remove duplicate entries and `-R` for a random order
# Filtering with grep-v

Using `grep -v` (invert match) to output the results not containing the keyword mentioned in the arguement

## My solve
**Flag** `pwn.college{sVbGmSdHW0PspIDLuzw_SwsYhem.0FOxEzNxwCO2gjNzEzW}`
- In this challenge, the standard output as multiple flags with DECOY in them and we need to filter those out using `grep -v`

```
/challenge/run | grep -v "DECOY"
```

## What I learned
We can use `grep -v` to show results which do not contain the keyword

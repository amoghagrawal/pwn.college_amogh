# Exporting Variables

Exporting variables to obtain the flag

## My solve
**Flag** `pwn.college{UexVlbrrrP4jKPxSVlDf8tFYF9I.QXyYTN0wCO2gjNzEzW}`
- The challenge requires us to set the value of PWN to COLLEGE and export it and set the value of COLLEGE to PWN but not export it

```
export PWN=COLLEGE
COLLEGE=PWN
/challenge/run
```

## What I learned
We can export the variables using the command `export`
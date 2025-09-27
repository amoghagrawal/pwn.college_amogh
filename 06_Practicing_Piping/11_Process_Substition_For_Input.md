# Process Substition for Input

Comparing the output of two files without saving them

## My solve
**Flag** `pwn.college{8o9v_MWw1mCnhkg4ArIuclMJrQV.0lNwMDOxwCO2gjNzEzW}`
- We need to compare the output of two files having decoy flags without saving them

```
diff /challenge/print_decoys <(/challenge/print_decoys_and_flag)
```

## What I learned
Using process substition to temporarily store the output of both commands and compare them using diff with the operator `<()`

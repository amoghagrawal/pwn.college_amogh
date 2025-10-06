# Finding Commands

Finding the directory from which `win` runs and running the `flag` command present in the same directory to find the flag

## My solve
**Flag** `pwn.college{0j2-JYBWY5OLzuyOPRZqdSuKPnJ.01NzEzNxwCO2gjNzEzW}`
- We need to find the path from which `win` runs
- On running `which win` we get the path as `/challenge/paths/9061/win`
- A flag file is also present in the same `9061` directory which we can access with cat

```
which win
cat /challenge/paths/9061/flag
```

## What I learned
We can use `which` to find the path of a command
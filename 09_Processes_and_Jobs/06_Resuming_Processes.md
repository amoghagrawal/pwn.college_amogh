# Resuming Processes

Suspend the run program to the background and continue it using `fg` to get the flag

## My solve
**Flag** `pwn.college{wK0jhYRfAqNswQcakduuq-A44Yr.QX2QDO0wCO2gjNzEzW}`
- We need to press CTRL+Z when we run `/challenge/run` to suspend the process and then type `fg` to resume it

```
/challenge/run #press ctrl+z
fg
```

## What I learned
We can use `fg` command to resume suspended processes
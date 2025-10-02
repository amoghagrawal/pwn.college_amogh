# Suspending Processes

Suspending the process to the background to obtain the flag

## My solve
**Flag** `pwn.college{EUhs3xnLxMKekRKSixnid4adrV4.QX1QDO0wCO2gjNzEzW}`
- The challenge requires us to be running two instances of `/challenge/run`
- We can do that using Ctrl+Z to suspend the process but keep it running in the background

```bash
/challenge/run #press ctrl+z then
/challenge/run
```

## What I learned
We can use CTRL+Z to suspend processes to the background
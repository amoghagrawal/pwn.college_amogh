# Listing Processes

To find the flag filename running in the processes using `ps` and run it to obtain the flag

## My solve
**Flag** `pwn.college{wz-TgyfAS_LnkzhinSPgZxVRBok.QX4MDO0wCO2gjNzEzW}`
- `/challenge/run` wont give the output as its been renamed to some random file
- We run `ps aux` or `ps -ef` to find the flag process in the list
- We get `/challenge/27703-run-17307`

```
ps aux
/challenge/27703-run-17307
```

## What I learned
We can see the running processes in the terminal using `ps`. To get every process we use `-e` and to get the full format we use `-f` and both can be merged into `-ef`. We can also use `ps aux` to get an almost similar output. `aux` also shows the CPU and memory the process is utilizing
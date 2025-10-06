# The PATH Variable

Mess with the path so that `/challenge/run` is unable to delete the flag

## My solve
**Flag** `pwn.college{oQIWv7AOVgdMVmq5HiXxpsOML-Y.QX2cDM1wCO2gjNzEzW}`
- When we run `/challenge/run` it tries to find the flag file and if found, it deletes it
- By doing `PATH=""` we mess with the path and the program is unable to find the flag file

```
PATH=""
/challenge/run
```
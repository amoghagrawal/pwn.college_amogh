# Using Sudo

Using `sudo` to get root access to get the flag

## My solve
**Flag** `pwn.college{MQygaU3cMEfqUnWevgAHQv2AVaI.QX4UDN1wCO2gjNzEzW}`
- `/challenge/run` doesnt give us the flag in this challenge
- On running `ls` we find the flag file as **not-the-flag**
- Using sudo to open it as admin we get the flag

```
ls
sudo cat not-the-flag
```

## What I learned
Modern systems use `sudo` to get admin access instead of su now. Sudo checks if the user is allowed to run commands as root whereas su relied on passwords.
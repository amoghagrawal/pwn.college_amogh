# Killing Processes

To `kill` the dont_run process to allow the run program to function and output the flag

## My solve
**Flag** `pwn.college{4XMLc7g8JQ6FSYTEcEj3iM7b4Y4.QXyQDO0wCO2gjNzEzW}`
- We need to kill the process `/challenge/dont_run` by finding its PID
- Using `ps` we find that its PID is 136

```
ps -ef
kill 136
/challenge/run
```

## What I learned
We can kill the processes running using the `kill` command. It needs a PID as an arguement
# Killing Misbehaving Processes

Killing misbehaving process which is sending decoy flags into the output to just obtain the actual flag

## My solve
**Flag** `pwn.college{8FbXN6UV0s-y9O3m4HwNqewxibr.0FNzMDOxwCO2gjNzEzW}`
- We need to kill the processes which are sending the decoy files to the `flag_fifo` file
- Using `ps -ef` we find that PID 142 is the process needed to be killed
- After killing, when we run `/challenge/run` it sends the actual flag to the `flag_fifo` file
- Using `cat` to open the `flag_fifo` file to get the flag

```
ps -ef
kill 142
/challenge/run
cat /tmp/flag_fifo
```
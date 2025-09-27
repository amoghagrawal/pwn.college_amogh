# Interrupting Processes

To Ctrl+C to stop an already running process to get the flag

## My solve
**Flag** `pwn.college{4fTXgb6Wcj3XsYRzjkoIYpIbCH1.QXzQDO0wCO2gjNzEzW}`
- `/challenge/run` is a process which keeps on running and to get the flag we must stop it
- To stop the program, we use Ctrl+C to interrupt it

```
/challenge/run
^C
```
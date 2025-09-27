# Backgrounding Processes

Running two versions of run, one in the background and one in the foreground to obtain the flag

## My solve
**Flag** `pwn.college{YPJ-3PNrL3ljpx5WsJ28b_U4PC5.QX3QDO0wCO2gjNzEzW}`
- The challenge requires us to run two processes of run at the same time
- We run one `/challeng/run` and stop it using CTRL+Z and start it again but move it to the background using `bg`
- We run another `run` process now

```
/challenge/run #press ctrl+z
bg
/challenge/run
```

## What I learned
We can use `bg` to resume suspended processes in the background
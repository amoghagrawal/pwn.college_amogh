# Split-piping stderr and stdout

Writing stderr and stdout to different commands to get the flag

## My solve
**Flag** `pwn.college{I_Npyf3Jur8Tqr83jkg_I3po6a8.QXxQDM2wCO2gjNzEzW}`
- We need to redirect the output of `/challenge/hack` to `/challenge/planet` and the error to `/challenge/the`
- To output the stderr to `/challenge/the` we make use of process substitution which is redirecting into a command with `>()`
- We can directly pipe the stdout to `/challenge/planet` using `|`

```
/challenge/hack 2> >(/challenge/the) | /challenge/planet
```
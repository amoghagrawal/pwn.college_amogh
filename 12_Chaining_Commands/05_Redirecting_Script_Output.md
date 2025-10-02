# Redirecting Script Output

Piping a shell script to the mentioned command to get the flag

## My solve
**Flag** `pwn.college{cmTNTsvlSw8slO0njQmpb3VNjHn.QX4ETO0wCO2gjNzEzW}`
- We create an script file called x.sh having the command for us
- We pipe the output of the script to `/challenge/solve` as input to get the flag

```bash
# x.sh
/challenge/pwn ; /challenge/college
```

```
bash x.sh | /challenge/solve
```

## What I learned
We can use the same output redirecting and piping methods on shell scripts as normal commands
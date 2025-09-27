# Duplicating piped data with tee

Learn the usage of the `tee` command and use it to find a secret needed for the flag

## My solve
**Flag** `pwn.college{Q3LUQud79aPHuGm_jmYAq1kiqir.QXxITO0wCO2gjNzEzW}`
- In this challenge the command `/challenge/pwn` a secret needs to be passed and then the output to `/challenge/college`
- We intercept the output first using tee command and it is `Q3LUQud7`

```
/challenge/pwm | tee logs.txt | /challenge/college
cat log.txt
/challenge/pwn --secret Q3LUQud7 | /challenge/college
```

## What I learned
The `tee` command duplicates the stdin of the command and writes it onto the stdout of multiple files

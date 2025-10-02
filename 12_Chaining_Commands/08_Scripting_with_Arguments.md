# Scripting with Arguments

Take arguements using special variables to the shell script and reverse them i.e. second comes in place of first and vice versa to get the flag

## My solve
**Flag** `pwn.college{gKKKuiKeZaIa69Lt1zjlYnRFBN8.0VNzMDOxwCO2gjNzEzW}`
- In the script we take two variables a and b and print them out in the reverse order using `echo`
- On running `/challenge/run` the expected output of the script was `college_4PbFFIoisw pwn_LYhvepQqSzE`
- I first did `echo b,a` which just printed `b,a` which was wrong
- Then I did `echo $b,$a` which gave the output as `college_4PbFFIoisw,pwn_LYhvepQqSzE`
- To get the correct output we had to print them with `echo $b $a`

```bash
#!/bin/bash
# solve.sh
a=$1
b=$2
echo $b $a
```

```
/challenge/run
```

## What I learned
We can arugements in the shell script using special variables like $1 for the first arugement, $2 for the second arguement and so on
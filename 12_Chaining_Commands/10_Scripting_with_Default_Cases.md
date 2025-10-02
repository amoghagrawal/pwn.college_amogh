# Scripting with Default Cases

Using an **if-else** conditional in the shell script and running it through `/challenge/run` to get the flag

## My solve
**Flag** `pwn.college{oXSHSPTxHU4vHxTXj5__2UAiMY4.01NzMDOxwCO2gjNzEzW}`
- The challenge requires us to make a shell script which outputs "college" if the input arguement is "pwn" and if the input is anything else, it outputs "nope"
- Then on running `/challenge/run` we will get the flag

```bash
#!/bin/bash
# solve.sh
if [ "$1" == "pwn" ]
then
	echo "college"
else
	echo "nope"
fi
```

```
/challenge/run
```
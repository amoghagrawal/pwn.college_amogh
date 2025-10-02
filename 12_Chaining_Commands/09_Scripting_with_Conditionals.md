# Scripting with Conditionals

Using an if conditional in the shell script and running it through /challenge/run to get the flag

## My solve
**Flag** `pwn.college{kGwC8_lWNEhcyMDMlqPuzICznNH.0lNzMDOxwCO2gjNzEzW}`
- The challenge requires us to make a shell script which outputs "college" if the input arguement is "pwn"
- Then on running /challenge/run we will get the flag
- Initially, the 2nd line of the script was `if ["$1" == "pwn"]` and it was giving an error on running /challenge/run
- Fixing the line to `if [ "$1" == "pwn" ]` gets us the flag

```bash
#!/bin/bash
# solve.sh
if [ "$1" == "pwn" ]
then
	echo "college"
fi
```

```
/challenge/run
```

## What I learned
We can add if conditionals in shell scripts where **if** is to start it and **fi** is to end it. All if, then, fi are needed to be on seperate lines
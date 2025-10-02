# Scripting with Multiple Conditions

Using multiple conditions in the shell script and running it through `/challenge/run` to get the flag

## My solve
**Flag** `pwn.college{ggt2VGMvUYZIxfdll3dGxUuGqqy.0FOzMDOxwCO2gjNzEzW}`
- The challenge requires us to make a shell script which outputs the following:
1. "college" if input is "pwn
2. "the planet" if input is "hack"
3. "linux" if the input is "learn"
4. "unknown" if the input is anything else
- Then on running `/challenge/run` we will get the flag

```bash
#!/bin/bash
# solve.sh
if [ "$1" == "pwn" ]
then
	echo "college"
elif [ "$1" == "hack" ]
then 
	echo "the planet"
elif [ "$1" == "learn" ]
then 
	echo "linux"
else
	echo "unknown"
fi
```

```
/challenge/run
```
# Adding Commands

Making a script called `win` and adding its location to path to get the flag

## My solve
**Flag** `pwn.college{k-xQHTYraMlPMRCu4Kh3zAi8fX8.QX2cjM1wCO2gjNzEzW}`
- First we need to find the path from which `cat` is executed and we get that as `/run/dojo/bin/cat`
- Next I set the PATH as `home/hacker/` but it failed to invoke `win`
- Setting it to `/home/hacker/` was also failing
- I realized that `win` didnt have execute permissions so we had to give that to the world
- Now when I run `/challenge/run` it can successfully invoke win to get us the flag

```bash
# win
/run/dojo/bin/cat /flag
```

```
chmod a+x
PATH="/home/hacker/
/challenge/run
```

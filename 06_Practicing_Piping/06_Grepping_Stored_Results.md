# Grepping stored results

Using grep on a file which contains the redirected output containing the flag

## My solve
**Flag** `pwn.college{IcQrivT9XOIl-CPZzvi5lr11ozH.QX4EDO0wCO2gjNzEzW}`
- The challenge wants us to write the output of `/challenge/run` to `/tmp/data.txt` which now contains thousands of lines along with the flag
- We search for the flag in the file using `grep` with the keyword `pwn.college` which is common in all flags on the platform

```
/challenge/run > /tmp/data.txt
grep "pwn.college" /tmp/data.txt
```

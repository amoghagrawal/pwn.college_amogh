# Executable Files

Changing the file permissions to make it executable by the hacker user to get the flag

## My solve
**Flag** `pwn.college{wmIEJVyOwMEJuFW_d0FI2_EJ7JR.QXyEjN0wCO2gjNzEzW}`
- On running `ls -l` we find the file is owned by the hacker user and the hacker group. 
- To make it executable we can use the arguement `u+x`

```
ls -l
chmod u+x /challenge/run
/challenge/run
```
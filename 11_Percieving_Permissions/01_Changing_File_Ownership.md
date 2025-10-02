# Changing File Ownership

Changing the ownership of the file containing the flag to access it and get the flag

## My solve
**Flag** `pwn.college{si_iGMdhT5oYMeV6vG9LD7e2rCq.QXxEjN0wCO2gjNzEzW}`
- The challenge wants us to change ownership of `/flag` using `chown`
- We can change the ownership of the file from root to hacker

```
chown hacker /flag
cat /flag
```

## What I learned
Chown is invoked by the root user to change the ownership of the flags and it takes two arguements, the new owner and the file name. **d** indicates a directory and **-** means a file.
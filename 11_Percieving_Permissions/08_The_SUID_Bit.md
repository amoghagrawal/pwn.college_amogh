# The SUID Bit

Add SUID to the file to make it execute as root user to get the flag

## My solve
**Flag** `pwn.college{4nK-OVTUaRKQ-f4Ve-Ks1CK3Ap-.QXzEjN0wCO2gjNzEzW}`
- The challenge requires us to add the SUID to /challenge/getroot
- Then I tried running `cat /challenge/getroot` but it doesnt work so on running `/challenge/getroot` we open a shell with root access
- We can get the file in the shell using `cat /flag`

```
chmod u+s /challenge/getroot
/challenge/getroot
cat /flag
```

## What I learned
By adding SUID to a file it executes it as a owner user always and the SUID can be added with `u+s`
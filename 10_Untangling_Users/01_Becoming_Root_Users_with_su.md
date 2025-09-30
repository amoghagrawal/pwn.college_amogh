# Becoming Root Users with su

Utilize root access with `su` to get the flag file

## My solve
**Flag** `pwn.college{cmEUii5rHFGyXsvBHEQthN3KArO.QX1UDN1wCO2gjNzEzW}`
- The challenge wants us to get root access using `su`
- The password is already given and is **hack-the-planet**
- Using `ls` we find the file flag as `not-the-flag` which requires permission to be opened by the user which root provides
- On running `cat` to read the file we get the flag

```
su
hack-the-planet
ls
cat not-the-flag
```

## What I learned
`su` which is now obselete is a method to get access to root if the password is already known but nowadays most devices dont have passwords for root and have different mechanisms for root access.
# Cracking Passwords

Cracking the password of Zardus using **JohntheRipper** to obtain the flag

## My solve
**Flag** `pwn.college{A--rn41yc5Mdc2KhCi6Bt-z0UnC.QX3UDN1wCO2gjNzEzW}`
- The challenge requires us to use a tool to decrypt a hashed password using **John the Ripper**
- We have a leaked file in `/challenge/shadow-leak` which we save as a text file
- On inputting the text file to John the Ripper, it decrypts the password to **aardvark** as in the image

```
/challenge/shadow-leak
su zardus
aardvark
/challenge/run
```

## What I learned
Passwords are stored in `/etc/shadow` and it holds the username and password seperated by a **:**. In the challenge the passwords were one way encrypted.
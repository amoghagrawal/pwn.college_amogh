# Changing Permissions

Changing the file permissions to make it readable to the hacker user to access it

## My solve
**Flag** `pwn.college{AVBgSDaAzsJsSRbByZ3G7TedNd3.QXzcjM1wCO2gjNzEzW}`
- We have to change the flag file permissions so that we can read it
- I tried `chmod u+r` but it doesnt give us access as user is root here
- By doing `chmod a+r` we provide the read access to everyone

```
chmod a+r /flag
cat /flag
```

# What I learned
The file permissions can be changed using `chmod` in the format `chmod u+rwx /flag` where u is the user, g is the group, a is all users and o is others. r is read, w is write, x is execute and a is append.
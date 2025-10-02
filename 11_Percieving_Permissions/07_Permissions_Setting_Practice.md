# Permissions Setting Practice

Changing the file permissions in the asked order to get the flag

## My solve
**Flag** `pwn.college{Q0FT2dAZPlRCFurUoLNM3OQ5Khn.QXzETO0wCO2gjNzEzW}`
- We have to correctly answer all 8 rounds to get the flag

```
/challenge/run
chmod u=w,g=w,o=rw /challenge/pwn
chmod u+r,g=rx,o=rx /challenge/pwn
chmod g=wx,o=x /challenge/pwn
chmod u+x,g-w,g+r,o+r /challenge/pwn
chmod u=-,g=wx,o=x /challenge/pwn
chmod u=rwx,g=rx,o=rw /challenge/pwn
chmod u-r,g-r /challenge/pwn
chmod u=rx,g=rx,o=x /challenge/pwn
chmod a+r /flag
cat /flag
```

## What I learned
We can set the file permissions with the symbol **=** also like `u=rwx` which adds all permissions or `u=-` which removes all permissions
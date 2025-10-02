# Permission Tweaking Practice

Changing the file permissions in the asked order to get the flag

## My solve
**Flag** `pwn.college{wa-Xs2M0MSRK02UDkHg_PnQY1hN.QXwEjN0wCO2gjNzEzW}`
- The challenge requires us to use `chmod` correctly 8 times in a row as it asks us to get the flag
1. Write access to the group
2. Write access to the other users
3. Execute access to all
4. Remove read access from the user and other users
5. Remove execute access from others
6. Remove write access from others
7. Remove read,write and execute access from group
8. Remove write and execute access from user
- The flag file is accessible to us but we need to make it readable
- To be on the safer side, we make the file readable to all users with **a+r**

```
/challenge/run
chmod g+w /challenge/pwn
chmod o+w /challenge/pwn
chmod a+x /challenge/pwn
chmod o-r,u-r /challenge/pwn
chmod o-x /challenge/pwn
chmod o-w /challenge/pwn
chmod g-rwx /challenge/pwn
chmod u-wx /challenge/pwn
chmod a+r /flag
cat /flag
```
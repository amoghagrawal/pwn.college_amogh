# Matching paths with []

Using the third glob `[]` to match paths directly

## My solve
**Flag** `pwn.college{8W73JqJFk93WDB_UvG3WypYhaY3.QX0IDO0wCO2gjNzEzW}`
- The challenge placed files in `/challenge/files` directory and we had to access them without going there
- `[]` requires you to be present in the folder you are addressing for it to properly work
- `/challenge/files/file` is the path of the file present and it can also be used with the `[]` glob

```
/challenge/run /challenge/files/file_[absh]
```

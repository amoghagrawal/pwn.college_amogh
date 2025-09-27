# finding files

Finding files using `find`

## My solve
**Flag** `pwn.college{cDmS98LM4-o8ylZHj7bEFlEUDuw.QXyMDO0wCO2gjNzEzW}`
- Tried finding the flag file in `/` but couldnt find anything
- Ran the find command in `challenge` but no result
- Ran the command in `usr` to get two possible flag files: `/usr/local/lib/python3.8/dist-packages/pwnlib/flag` and `usr/share/emacs/26.3/lisp/obsolete/flag`
- `/usr/local/lib/python3.8/dist-packages/pwnlib/flag` contains `flag.py` but permission is denied
- `usr/share/emacs/26.3/lisp/obsolete/flag` is the program containing the flag

```
cd /
find usr -name flag
cat usr/share/emacs/26.3/lisp/obsolete/flag
```

## What I learned
The `find` command takes the name and the location to find the file in, otherwise it shows all the files and uses the current location to find the files.

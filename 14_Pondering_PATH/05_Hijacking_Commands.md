# Hijacking Commands

Stopping `/challenge/run` from deleting the flag file by changing the path to `rm` to get the flag

## My solve
**Flag** `pwn.college{Mw3jVoTuvxAcFXAKacZCNrTHSos.QX3cjM1wCO2gjNzEzW}`
- The `/challenge/run` file checks for the path of `rm` using the `which` command
- We can replace the rm function by changing the path of the function to something we want
- In this case, to read the file, we will make a fake `rm` that runs `cat /flag`
- We will write that fake rm to `/tmp` becuase its writable easily
- `<<'EOF'` is a heredoc which makes it easy to write multiple lines into a file.
- In the fake `rm` command, we call `/run/dojo/bin/cat /flag` so when `/challenge/run` runs rm, the flag is printed instead of being removed

```bash
#!/bin/sh
cat > /tmp/rm <<'EOF'
/run/dojo/bin/cat /flag
EOF
```

```
chmod +x hijack
./hijack
chmod +x /tmp/rm
export PATH="/tmp:$PATH"
/challenge/run
```

## What I learned
By setting the path using "/filepath:$PATH" we make it a higher priority path which is used first
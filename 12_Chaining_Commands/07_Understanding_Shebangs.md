# Understanding Shebangs

Adding a shebang to the script file at the start to get the flag

## My solve
**Flag** `pwn.college{suECJstjl1Aw4FX-fBVJ9yozE6k.0VOzMDOxwCO2gjNzEzW}`
- The challenge requires us to add the sheband `#!/bin/bash` for the file to be interpreated as a bash file
- In the terminal we run `/challenge/run` to get the flag

```bash
#!/bin/bash
# solve.sh
echo "hack the planet"
```

```
/challenge/run
```

## What I learned
Shebangs begin with `#!` and are like `#!/bin/bash` or `#!/usr/bin/python3`
# Groups and Files

Changing the group that can read a file to get the flag using `chgrp`

## My solve
**Flag** `pwn.college{waWMWBJZzDhIvEAYMIi9_0VfhTZ.QXxcjM1wCO2gjNzEzW}`
- The challenge has given us access to change groups which is required to get the flag
- Using `chgrp` we change the file group from root to hacker

```
chgrp hacker /flag
cat /flag
```

## What I learned
Chgrp is another command which can be invoked by the root user to change the group ownership of a file to a different group. Using the `id` command we can see information about the user like what its UID, group ID etc.
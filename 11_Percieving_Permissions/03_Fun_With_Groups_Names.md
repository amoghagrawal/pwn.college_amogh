# Fun With Groups Names

Finding the group belonging to the hacker and changing the flag ownership to that group

## My solve
**Flag** `pwn.college{8ZlYEYFFerj6ofTK8QtYsX8zJsH.QXycjM1wCO2gjNzEzW}`
- We have to first find the group *hacker* belongs to
- Using `id` we find the group as **grp17541** which was randomly assigned by the challenge
- Changing the flag file ownership to grp17541 to get the flag

```
id
chgrp grp17451 /flag
cat /flag
```
# Handling Failure

Obtain the flag by chaining two commands with ||

## My solve
**Flag** `pwn.college{wGGl8cEcsK_bC4PY9nHy-kN8Tte.01M0MDOxwCO2gjNzEzW}`

```
/challenge/first-failure || /challenge/second
```

## What I learned
We can chain files using **||** and the second command is only executed if the first command fails
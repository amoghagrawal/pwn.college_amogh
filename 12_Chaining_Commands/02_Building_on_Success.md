# Building on Success

Obtain the flag by chaining two commands with &&

## My solve
**Flag** `pwn.college{sF1ea9i5OnX6ZcIMB5jyHJGWUcN.0lM0MDOxwCO2gjNzEzW}`
- On running `/challenge/first-success` there is no output
- On running `/challenge/second`, it shows the error saying that it needs to be chained to work
- On chaining using **&&** we get the proper flag

```
/challenge/first-success && /challenge/second
```

## What I learned
We can chain files using **&&** and it works as an AND operator meaning the second command is only executed if the first command is properly executed and gives an output 
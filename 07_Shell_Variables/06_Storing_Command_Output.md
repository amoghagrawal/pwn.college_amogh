# Storing Command Output

Storing a command into a variable using `$()`

## My solve
**Flag** `pwn.college{AHypoEz9pXqkUKkAwjSk9Uk2yk7.QX1cDN1wCO2gjNzEzW}`
- Store the `/challenge/run` command in the PWN variable
- Display the variable using echo

```
PWN=$(/challenge/run)
echo $PWN
```

## What I learned
We can store a command into a variable using `$()` or backticks
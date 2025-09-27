# Grepping live output

Using grep on the live output using piping or `|` instead of redirecting it onto a file

## My solve
**Flag** `pwn.college{MJejgZF8X2cr5DoC8VgzY6nX8tO.QX5EDO0wCO2gjNzEzW}`

```
/challenge/run | grep "pwn.college"
```

## What I learned
We can also directly grep a file without storing it first by using `|` which "pipes" the output onto the grep command

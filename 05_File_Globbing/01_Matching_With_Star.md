# Matching with *

Using the first glob `*` to replace characters

## My solve
**Flag** `pwn.college{o6EsYmpwqnynJ3Dg6-ciT33bmwg.QXxIDO0wCO2gjNzEzW}`
- The challenge asked to just use 4 characters in the command and use `*`

```
cd /c*
/challenge/run
```

## What I learned
We can use `*` to replace characters of an arguement in any command and the shell matches the arguement/file to the closest thing

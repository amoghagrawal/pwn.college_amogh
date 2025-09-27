# Matching with []

Using the third glob `[]` to replace characters

## My solve
**Flag** `pwn.college{EXbUr3Q7T0IwgxaiGkWYbwB-qby.QXzIDO0wCO2gjNzEzW}`
- The challenge wanted us to change our directory to `/challenge/files`
- Run `/challenge/run` with a single arguement using `[]`

```
/challenge/files
/challenge/run file_[absh]
```

## What I learned
Similar to `?` but instead of matching any character, it choses from a set of characters given in `[]`

# Searching for manuals

Learning to search for the right manual pages

## My solve
**Flag** `pwn.college{sdnAYLZYHpipjoPdC7UvHGSCtIX.QX2EDO0wCO2gjNzEzW}`
- By doing `man man` we see that we can use `apropos` or `-k` to search for keywords in the manual
- Doing `man -k challenge` gives us `sdnpipjodv` which is the hidden name for the challenge manual
- Doing `man sdnpipjodv` gives us the arguement for the challenge which is `--sdnpip NUM` and the num is `720`

```
man man
man -k challenge
man sdnpipjodv
/challenge/challenge --sdnpip 720 
```

## What I learned
In a given manual, along with `/` to search, we can also use `-k` to seacrch for a keyword like `man -k challenge` or `apropos challenge`.

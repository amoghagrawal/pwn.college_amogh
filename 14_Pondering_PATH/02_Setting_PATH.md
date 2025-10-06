# Setting PATH

Change the path so a command can be directly invoked to get the flag

## My solve
**Flag** `pwn.college{wezeioVHo2P2Wr5CYs97DA91OXt.QX1cjM1wCO2gjNzEzW}`
- For us to get the flag, `/challenge/more_commands/win` must run directly from its name `win` so we can change the path
- By setting the path to `/challenge/more_commands/` we achieve the above
- On running `/challenge/run` we get the flag

```
PATH="/challenge/more_commands/"
/challenge/run
```
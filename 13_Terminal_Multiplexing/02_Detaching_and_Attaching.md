# Detaching and Attaching

Detach and reattach a screen session to get the flag

## My solve
**Flag** `pwn.college{8gDjjlSzIK7muBuHQtCPaVlt3EH.0lN4IDOxwCO2gjNzEzW}`
- The challenge requires us to detach the session first which we can do by pressing Ctrl+a and then d on the keyboard
- Typing `/challenge/run` sends the flag to the detached terminal
- By reattaching the flag is not shown to us

```bash
screen
# press Ctrl+A following by d
/challenge/run
screen -r
```

## What I learned
We can detach a screen with "Ctrl+A" and then pressing "d" and reattach it with the command `screen -r`. 
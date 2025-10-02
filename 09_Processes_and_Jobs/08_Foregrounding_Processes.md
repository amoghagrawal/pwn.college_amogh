# Foregrounding Processes

To get the flag, we must send a background process to the foreground

## My solve
**Flag** `pwn.college{ospvKV30SBV1PQ2x0mUFLC_bFNg.QX4QDO0wCO2gjNzEzW}`
- We first suspend the initial process and resume it into the background with `bg`
- We then move the background process into foreground with `fg`

```bash
/challenge/run #press ctrl+z
bg
fg
```

## What I learned
We can use `fg` to move both suspended and background processes into foreground
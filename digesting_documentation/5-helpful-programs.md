# Helpful Programs

Finding arguements for commands without a manual using `--help` or `-h`

## My solve
**Flag** `pwn.college{U3VKF8CrCXIGWMF3e30iQxkrm6q.QX3IDO0wCO2gjNzEzW}`
- `challenge --help` leads nowhere so I tried `\challenge\challenge --help` to get `--get-the-flag` and `--print-value`
- `\challenge\challenge --g` needs an arguement that we get from `\challenge\challenge --p` and I got `383`

```
\challenge\challenge --help
\challenge\challenge --print-value
\challenge\challenge --get-the-flag 383
```

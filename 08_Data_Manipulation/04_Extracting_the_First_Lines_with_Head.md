# Extracting the First lines with Head

Using `head` to display the first n number of lines of the output

## My solve
**Flag** `pwn.college{Yh_0J9hVUXc48Aq2aN13U4SlF4H.0lNxEzNxwCO2gjNzEzW}`
- The challenge requires us to pipe the first 7 lines of `/challenge/pwn` to `/challenge/college`
- `head -n 7` outputs the first 7 lines needed and we pipe them to `/challenge/college` using `|`

```
/challenge/run | cut -d " " -f 2 | tr -d "\n"
```
# Translating Characters

Using `tr` to modify characters recieved over standard output via piping

## My solve
**Flag** `pwn.college{I9NqxwT0r0Iw414b-KYK270j6Yw.01MxEzNxwCO2gjNzEzW}`
- In the flag, the upper and lower cases have been swapped and we have to convert them
- Using tr, we can convert all "a-z" to "A-Z" and vice versa

```
/challenge/run | tr 'a-zA-Z' 'A-Za-z'
```

## What I learned
We can use `tr` to modify characters over stdout and print them over stdout also

## What I referred
Referred to [Stackoverflow](https://stackoverflow.com/questions/23178769/unix-tr-command-to-convert-lower-case-to-upper-and-upper-to-lower-case) to get help over the command
# Redirecting Input

Using `<` to direct the input from a file to the program

## My solve
**Flag** `pwn.college{IwNfGR7QWdj4RU2LhIPo5dBj5Z8.QXwcTN0wCO2gjNzEzW}`
- We need to append `COLLEGE` into the PWN file, we can do this by appending the output of the echo command
- This PWN file now serves as the stdin of `/challenge/run`

```
echo COLLEGE > PWN
/challenge/run < PWN
```

# Reading Files

Using `read` to read off a file

## My solve
**Flag** `pwn.college{QdM_IIQDuUHUja0jI7ron5lSBuF.QXwIDO0wCO2gjNzEzW}`
- The challenge requires us to read the flag into the PWN variable
- Since `read` reads the input of PWN, we store the output of `/challenge/read_me` into the input of PWN

```
read PWN < /challenge/read_me
```
# Named Pipes

Manually creating a named pipe to redirect the output using the FIFO technique to get the flag

## My solve
**Flag** `pwn.college{MeOF4n-0su6OdU0E-lpXO3hrjY4.01MzMDOxwCO2gjNzEzW}`
- We need to create a pipe in tmp called flag_fifo using `mkfifo`
- A FIFO performs the write operation only when it is open in both and read and write mode in seperate terminals
- We redirect the output of `/challenge/run` to `/tmp/flag_fifo` using `>` and also open the flag_fifo file using `cat` in a different terminal

```
mkfifo /tmp/flag_fifo
/challenge/run > /tmp/flag_fifo

# in a different terminal
cat /tmp/flag_fifo 
```

## What I learned
We can create our own pipes called FIFOs using `mkfifo`. These FIFOs show up in the directory when operated upon by `ls`. They also perform operations only when it is opened in both read and write mode
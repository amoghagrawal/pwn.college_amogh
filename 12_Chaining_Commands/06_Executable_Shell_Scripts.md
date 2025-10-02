# Executable Shell Scripts

Executing a shell script by giving execute permissions and running it without using `bash`

## My solve
**Flag** `pwn.college{0Kzc8HvypmjgLGPiaPJqGTecuoH.QX0cjM1wCO2gjNzEzW}`
- In the script we have the command to execute `/challenge/solve`
- The script is stored in `home/hacker`
- On running the script using `~/q6.sh`, we get that the we dont have permission to execute it
- On adding the permission using `chmod` we can get the flag

```bash
# q6.sh
/challenge/solve
```

```
ls -l
chmod u+x q6.sh
./q6.sh
```
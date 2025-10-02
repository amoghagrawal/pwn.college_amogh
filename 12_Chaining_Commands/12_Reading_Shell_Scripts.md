# Reading Shell Scripts

Obtaining the password of the shell script `/challenge/run` and using that password as the input for the if conditional to get the flag

## My solve
**Flag** `pwn.college{4XM8u2lb7vduLj25OvG8xpYaQJn.0lMwgDOxwCO2gjNzEzW}`
- On reading the /challenge/run script we find an IF condition with `if [ "$GUESS" == "hack the PLANET" ]` so the secret is **hack the PLANET**
- The script contained:
```bash
#!/opt/pwn.college/bash
read GUESS
if [ "$GUESS" == "hack the PLANET" ]
then
        echo "CORRECT! Your flag:"
        cat /flag
else
        echo "Read the /challenge/run file to figure out the correct password!"
fi
```
- I tried running `/challenge/run "hack the PLANET"` but that didnt work
- So I set `GUESS="hack the PLANET"` but that doesnt work since variables inside the script are different from the ones in the shell
- The script had its first line as `read GUESS` so I decided to send the stdout of an echo command to the stdin of `/challenge/run` which is the read command
- On setting `echo "hack the PLANET" | /challenge/run`, the secret is set in the GUESS variable inside the script and we get the flag

```
cat /challenge/run
echo "hack the PLANET" | /challenge/run
```
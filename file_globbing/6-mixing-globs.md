# Mixing Globs

Using an arguement of 6 globs or less to get the words "challenging", "educational", and "pwning"

## My solve
**Flag** `pwn.college{YVSPUlioWHkfk3IA6f0S67UhNHV.QX1IDO0wCO2gjNzEzW}`
- Tried combinations like `*[np]*`, `*n*`, `*[ae]*` etc but all ended up giving words other than the required ones
- By using the starting words in the `[]` glob we eliminated all the extra words to get the flag

```
cd /challenge/files
/challenge/run [cep]*
```
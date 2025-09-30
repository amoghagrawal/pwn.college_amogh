# Other Users with su

Getting access to the user "Zardus" with su to get the flag

## My solve
**Flag** `pwn.college{wYiNnMlK3XKDyf7m6lguVBw_hrj.QX2UDN1wCO2gjNzEzW}`
- The challenge wants us to get access to a particular user "zardus" using `su`
- Giving `zardus` as an arguement to `su` gives us access to the user
- On running `/challenge/run` we get the flag

```
su zardus
/challenge/run
```
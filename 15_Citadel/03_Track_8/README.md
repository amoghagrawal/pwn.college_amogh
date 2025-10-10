# DESCRIPTION
Decode the following message to get the flag
```
twj eys zpr ukm 'viamnwqw' bx lzgo: 
esmqqui{yyr_oshwwcm_bwupa}
```

# WRITEUP

- The cipher might be a vigenère cipher as it requires a key
- On [cryptii.com](cryptii.com), decoding the intial cipher as vigenere with the key **Ginkgo** which is Panchiko's latest album
- We get the result `rigckmv{osd_ikumqog_tjkjm}`
- Again using the vigenere cipher but **panchiko** as the key to get the final flag

> citadel{add_vinegar_twice}

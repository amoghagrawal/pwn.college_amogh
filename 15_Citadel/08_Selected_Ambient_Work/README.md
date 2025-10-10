# DESCRIPTION
Find the hidden message in the audio file to proceed. Flag is in the format citadel{S3L3CT3D_AMB13NT_W0RK}

# WRITEUP

- Seeing an audio file, the first instinct is to check the spectogram
- The [spectogram](spectogram.png) reveals `citadel{      }`
- The audio is morse code but running the entire audio through decoders gives nothing
- We tried to run only the part inside the brackets on morse code decoders but nothing
- Then we saw the morse code at the bottom of the spectogram
- Decoding the morse code on https://www.dcode.fr/morse-code gives us the flag element `1L0V31DM`
- The morse code was
```
.---- .-.. ----- ...- ...-- .---- -.. --
```

> citadel{1_L0V3_1DM}
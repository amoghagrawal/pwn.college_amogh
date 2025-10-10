# DESCRIPTION
Decode the given .pcap file to get the flag

# WRITEUP

- Seeing a .pcap file, my first thought was to check the packets in wireshark
- Reading it in wireshark only bought up lines irrelevant to the challenge as mentioned below:
```
you are breaking my heart mijo
Hey, Catch! ···············
If you read this you are gae LMAO
*notices bulge* OwO what's this?
what's up choom?
Whatever it takes.
Wish we could go to the moon together.
All i wanted was for u to live
You never had to save me.
I can feel the sun!
```
- Next was to run the file through exiftool and foremost
- foremost extracted an [image](extracted.jpg) which directly contained the flag

> citadel{1_r34lly_w4nt_t0_st4y_4t_y0ur_h0us3}


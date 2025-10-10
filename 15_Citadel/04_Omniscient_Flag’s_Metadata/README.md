# DESCRIPTION
The challenge suggests that there is a hidden image in the image which has the flag

# WRITEUP

- First instinct was to run exiftool on the image but it only revealed `kdj had a habit of hiding images within images` which was not useful
- To extract any hidden images from the jpg file, we can use **foremost** on WSL to extract any hidden image and we get **00000170.png**
- 00000170.png has the flag in the image itself

> citadel{th1s_ch4ll3ng3_1s_f0r_th4t_0n3_ex1ft00l_4nd_b1nw4lk_enthus14st}

# Magic Bytes (100)

> My friend sent me this text file and said they put a flag inside. I opened it and it doesn't look like a normal 
text file to me! Maybe you'll be able to find it.


# Solution

![Image of file command](https://github.com/bombunx/CTFs/blob/master/utctf-d4ddy_p0k0_p4nts/Beginner/Magic%20Bytes/MagicBytes%20-%20file%20command.PNG)

Using the `file` command, we can see that the challenge file - *out.txt* is a PNG file 
instead of a text file. After changing the file extension, we can get the flag. 

Flag: `utflag{file_extensions_mean_nothing}`

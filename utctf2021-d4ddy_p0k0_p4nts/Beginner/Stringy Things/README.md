# Stringy Things (100)

> I know there's a string in this binary somewhere.... Now where did I leave it?

# Solution

![Image of flag](https://github.com/bombunx/CTFs/blob/master/utctf-d4ddy_p0k0_p4nts/Beginner/Stringy%20Things/Flag.PNG)

Using the `strings` command, we can store all the strings present in [calc](./calc) to a text file called output.txt.
To find the string starting with *utflag...* (which is the flag), we can enter `grep utflag output.txt`, which will give us the flag.

Flag: `utflag{strings_is_op}`

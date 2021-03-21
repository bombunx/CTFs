# Run-ELF (100)

> Anyone know how to run an ELF file? I bet you could figure it out.


# Solution

The first thing we do with all files are to use the `strings` command to find all the string characters within the file. Using `strings run > output.txt`, 
we stored all the strings found in the challenge file - [run](./run) into `output.txt`. 

![Image of flag](https://github.com/bombunx/CTFs/blob/master/utctf-d4ddy_p0k0_p4nts/Beginner/Run-ELF/Flag.PNG)

From here, we entered `grep utflag output.txt`, which basically displays all strings containing the word `utflag`. 

Flag: `utflag{run_run_binary_9312854}`

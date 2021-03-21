# Doubly Deleted Data (330)

> We got a copy of an elusive hacker's home partition and gave it to someone back in HQ to analyze for us. We think the hacker deleted the 
> file with the flag, but before our agent could find it, they accidentally deleted the copy of the partition! Now we'll never know what that 
> flag was. :(

# Solution

Autopsy 4.17.0 was used for the analysis of [flash_drive.img](./flash_drive.img). 

Upon opening up the image, we can see that there are 1103 deleted files in total and out of them are 4 file systems. We can see that there is a suspicious
disk image named **sus_image.img**. Next, we tried to extract the image. However, the extraction was unsuccessful as the the image was too big. 

We looked around for other suspicious looking files and found **plan.txt**. However, it was just a text file and nothing much. 

We continued digging and found a filed named **Unalloc_4_872448_435159040** under the **$Unalloc** folder. Files in the Unallocated space are basically deleted 
files with no pointers pointing to them. This means that they do not exist within a partition and users will not be able to access them through the Windows 
File Explorer.

The file is successfully extracted and we entered `strings Unalloc_4_872448_435159040 > output.txt`, which will store all the readable text from the file into 
**output.txt**. Next, using the `grep utflag output.txt` command, we obtain 2 flags. The first flag is the correct flag. 

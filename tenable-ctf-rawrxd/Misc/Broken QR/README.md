# Broken QR (100)
> Description: Can you scan this QR code for me?
![QR_broken](./QR_broken.PNG)

# Solution
First we studied how QR codes worked. As a result, we discovered that QR codes would always have the same 3 large squares on the top left, top right, 
and bottom left of the QR code. Using a drawing application (in this scenario, ibisPaint X), the bottom left large square was "lassoed" and pasted on to
the top left and top right of the QR code.

![QR_3squares](./QR_3squares.PNG)

Afterwards, taking a closer look at the QR code, we "fixed" the code by colouring in the black bits that were rubbed off. It was crucial to understand that
the size of a black bit would always have the same dimemsions, allowing us to only add what was needed.

![QR_fixed](./QR_fixed.PNG)

# Flag
Scanning the fixed QR code would give us our flag.
![QR_scanned](./QR_scanned.PNG)

```
flag{d4mn_it_w0nt_sc4n}
```

# HTTPS Decryption (150)
```
In this challenge, you are provided with a file containing captured network packets and a file containing master keys. Your task is to decrypt the HTTPS traffic and find the flag hidden within the decrypted data. The target domain for this challenge is mrgray.xyz. Good luck!
```

# Solution
Open the PCAP file in Wireshark. Perform TLS Decrypt under Edit -> Preferences -> Protocols -> TLS. Import the master key log file. Search packet details for 'uctf'.

# Flag
```
uctf{St. Sarkis_Church}
```

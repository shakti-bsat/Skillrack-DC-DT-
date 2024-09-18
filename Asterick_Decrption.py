encrypted = input().strip()

decrypted, i = '', 0
while i < len(encrypted):
    if i + 2 < len(encrypted) and encrypted[i + 2] == '*':  
        num = int(encrypted[i:i + 2])  
        i += 3
    else:
        num = int(encrypted[i]) 
        i += 1
    decrypted += chr(num + 97)  

print(decrypted)

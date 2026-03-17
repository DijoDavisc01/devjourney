# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))
char=input("enter a character: ")
asci_value=ord(char)
if asci_value in range(97,122) or asci_value in range(65,90):
    print(char,"is alphabet..")
else:
    print(char,"is not alphabet")
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
letters = 'abcdefghijklmnopqrstuvwxyz'
new_str = ''

for char in text:
    if char in letters:
        index = letters.index(char)
        if index < len(letters) - 2:
            new_str += letters[index + 2]
        elif char == 'y':
            new_str += 'a'
        elif char == 'z':
            new_str += 'b'

    else:
        new_str += char

print(new_str)
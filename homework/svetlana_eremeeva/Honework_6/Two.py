words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


for key, value in words.items():
    if key == 'I':
        print(key*3)
    elif key == 'love':
        print(key*5)
    elif key == 'Python':
        print(key*1)
    elif key == '!':
        print(key*50)

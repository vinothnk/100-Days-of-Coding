def readfile():
    with open('data.txt', mode='r') as data:
        value = data.read()
        print(value)
        data.close()
    return

def writefile(score):
    with open('data.txt', mode='w') as data:
        value = data.write(score)
        print(value)
        data.close()
    return

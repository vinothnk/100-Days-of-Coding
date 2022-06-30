with open('/Users/wooo_/PycharmProjects/Day 24 - Files, Directories and Paths'
          '/Mail Merge Project Start/Input/Names/invited_names.txt') as data2:
    nameslist = data2.readlines()
    print(nameslist)

    for name in nameslist:
        print(name)

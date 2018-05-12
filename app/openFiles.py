# open file
file = open('test.txt', 'rt', encoding='UTF-8')

# each line
for line in file:
    print(line)

# end work
file.close()

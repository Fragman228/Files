with open('First_file.txt', 'w+') as first_file:
    first_file.write('Я гений и стараюсь учить питон')
with open('First_file.txt', 'r') as first_file:
    first_part = first_file.read(7)
print(first_part)


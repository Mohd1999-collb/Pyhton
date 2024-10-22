
with open('chapter_9_File_Handling/animal.txt') as f :
    data = f.read()
    

content = data.replace('Donkey', '######')

with open('chapter_9_File_Handling/animal.txt', 'w') as f :
    f.write(content)
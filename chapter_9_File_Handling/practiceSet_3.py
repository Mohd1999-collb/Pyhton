

n = 2
def table(n):
    for i in range(1, 11) :
        with open(f'chapter_9_File_Handling/13_years_old/{n}_table.txt', 'a') as f :
             f.write(f"{n} x {i} = {n*i}\n")





while n <= 20 :
    table(n)
    n += 1
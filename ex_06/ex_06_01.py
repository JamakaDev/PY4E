#EX_06_01
fruit = 'banana'
count = len(fruit)
while count >0:
     print(fruit[count-1])
     count-=1

#EX_06_02
print(f'fruit[:] prints the entire string, {fruit[:]}')

#EX_06_03
def count(string, letter):
    counter = 0
    for l in string:
        if l == letter:
            counter +=1
    return (f'The letter "{letter}" is in {string} {counter} times')

print(count(fruit, 'a'))

#EX_06_04
a_count = fruit.count("a")
n_count = fruit.count("n")
print(a_count)
print(n_count)



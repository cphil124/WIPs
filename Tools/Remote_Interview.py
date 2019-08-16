def reverse_vowels(line):
    vowels = ['a','e','i','o','u']
    vowel_indexes = []
    vowel_list = []
    for i in range(len(line)):
        if line[i] in vowels:
            vowel_indexes.append(i)
            vowel_list.append(line[i])
    new_line = ''
    counter = 0
    for i in range(len(line)):
        if i in vowel_indexes:
            print(vowel_list)
            new_line = new_line + vowel_list[-(1+counter)]
            print(vowel_list[-(1+counter)])
            print('Counter: ', counter)
            counter += 1
        else:
            new_line = new_line + line[i]
        
    print(new_line)

# reverse_vowels('alphabet')




def count_piles(N, M, P):
    print('Loop Start:', N)
    num_piles = 0
    if N <= M:
        num_piles += 1
    elif N <= P:
        num_piles += N
    else:
        cursor = N
        if N % 2 == 1:
            pile_size = (N // P) + 1
        else:
            pile_size = N // P
        for i in range(P):
            print('Loop:', N, 'Cursor:' , cursor, 'Pile Size: ', pile_size, 'M:', M)
            if cursor > pile_size:
                num_piles += count_piles(pile_size, M, P)
                cursor = cursor - pile_size
            else:
                num_piles += count_piles(cursor, M, P)
    print('Loop Close:', N, 'Num Piles', num_piles)
    return num_piles

print(count_piles(3,2,5))

        
            

        






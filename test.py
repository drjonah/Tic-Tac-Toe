
# for i in range(6):

#     for j in range(3):
        
#         if (i > 2): 
#             row = i + (j - 2 - i%3)
#             col = i - 3

#         else: 
#             row = i
#             col= j

#         print(f'[{row},{col}]')

for i in range(3):
    print('i = ' + str(i))

    print('horizontal')
    print(str(i*3) + ' ' + str((i*3)+1) + ' ' + str((i*3)+2))

    print('vertical')
    print(str(i) + ' ' + str((i+3)) + ' ' + str((i+6)))

    print()
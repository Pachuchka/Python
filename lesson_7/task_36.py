#task_36
def print_operation_table(operation,num_row = 6, num_col = 6):
    for i in range(1,num_row+1):
        print("\n")
        for j in range(1,num_col+1):
            print (operation(i,j), end = " ")
print_operation_table(lambda x,y:x*y)
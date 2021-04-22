def create(n):
    k = n - 1
    counter = 0
    for i in range(0,n):
        # print(f".", e/nd='')
        print("\t" * (n-i),end="")
        for j in range(1, i+2):
            counter += 2 if(counter+1 == 3) else 1
            power = 2 if((i)%2 == 0) else 1
            print(f'\t{counter** power}',end="")
        print("")
create(3)

"""
output: 

				1
			2	4
		25	36	49
"""
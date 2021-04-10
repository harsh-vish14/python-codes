num_list = [5, 'c', 20, 0, 40]

b = 15

for x in num_list:

    try:

        c = b / x


    except ZeroDivisionError:

        print("An element with 0 value")

    except TypeError:

        print("Only numbers can be used")
    else:
        print(c)
    finally:
        print(f'num_list elements used :{x}\n')
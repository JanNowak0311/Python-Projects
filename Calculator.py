calc_list = [0] * 10
print("Type 'i' to add a number to operate on (e.g., 'i 0 5')\n"
      "Type 'c' to clear all numbers from the list\n"
      "Type 's' to show list\n"
      "Use '+', '-', '*', '/', '%' to calculate (e.g., '+ 0 1')")
while True:
    try:
        line = input().split()
        if len(line) == 1 and line[0] == 's':
            print(calc_list)
            continue
        if len(line) == 1 and line[0] == 'c':
            calc_list = [0] * 10
            print("List cleared:", calc_list)
            continue

        x = str(line[0])
        y = int(line[1])
        z = int(line[2])

        if not (0 <= y <= 9 and 0 <= z <= 9):
            print("Index out of range")
            continue
        if x == 'i':
            calc_list[y] = z
            print(calc_list)
        elif x == '+':
            print(calc_list[y] + calc_list[z])
            print(calc_list)
        elif x == '-':
            print(calc_list[y] - calc_list[z])
            print(calc_list)
        elif x == '*':
            print(calc_list[y] * calc_list[z])
            print(calc_list)
        elif x == '/':
            if calc_list[z] == 0:
                print("Error: Divide by zero")
                continue
            print(calc_list[y] / calc_list[z])
            print(calc_list)
        elif x == '%':
            if calc_list[z] == 0:
                print("Error: Modulo by zero")
                continue
            print(calc_list[y] % calc_list[z])
            print(calc_list)

    except (IndexError, ValueError):
        print("Invalid input, try again (format: command index1 index2, e.g., 'i 0 5' or '+ 0 1')")
        continue
    except:
        print("Exiting calculator")
        break
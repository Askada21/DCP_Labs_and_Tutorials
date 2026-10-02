print("IBM 1401 OPERATOR CONSOLE")
print("=========================")

option = 1

#repeat until loop is 0
while option != 0:
    print("1. Card reader check")
    print("2. Payroll batch run")
    print("3. Job time estimate")
    print("4. Core memory calculator")
    print("5. Two-digit date check")
    print("6. GCD (converted from FORTRAN)")
    print("7. Interest table (converted from FORTRAN)")
    print("0. Power down")
  
    option = int(input("\nSelect: _"))

    if option == 1:
        print("Card reader check")
    elif option == 2:
        print("Payroll batch run")
    elif option == 3:
        print("Job time estimate")
    elif option == 4:
        print("Core memory calculator")
    elif option == 5:
        print("Two-digit date check")
    elif option == 6:
        print("GCD (converted from FORTRAN)")
    elif option == 7:
        print("Interest table (converted from FORTRAN)")
    elif option == 0:
        print("Power down")
    else:
        print("No option")
print("Shut down")


    

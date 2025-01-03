def list_digits():
    number = int(input("Enter a 4 digit positive integer: "))
    print(number // 1000)
    print((number % 1000) // 100)
    print((number % 100) // 10)
    print(number % 10)
    

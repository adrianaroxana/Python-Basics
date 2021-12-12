while True:
    a = input("Please enter first number: ")
    b = input("Please enter second number: ")

    try:
        c = int(a) + int(b)
        print(c)
    except ValueError:
        print("These are not integers!")
    except Exception as e:
        print(str(e))
    finally:
        print("Introduce numbers!")

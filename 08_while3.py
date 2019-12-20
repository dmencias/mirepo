while True:
    x=input("Ingrese un numero hasta donde contar: ")
    if x == 'q' or x == 'quit':
        break
    else:
        x = int(x)
        y=1
        while True:
            print(y)
            y=y+1
            if y>x:
                break
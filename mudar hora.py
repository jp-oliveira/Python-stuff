def mudar(h,m):
    global nh
    if h >= 12:
        nh= h - 12
    else:
        nh = h
    return nh

def saída(nh):
    if h>=12:
        if nh == 1 or 0:
            print("É %i : %i PM"%(nh,m))
        else:
            print("São %i : %i PM"%(nh,m))
    else:
        if nh == 1 or 0:
            print("É %i : %i AM"%(nh,m))    
        else:
            print("São %i : %i AM"%(nh,m))
    

h = int(input("Diga a hora desejada: "))
m = int(input("Diga os minutos desejados: "))

mudar(h,m)
saída(nh)
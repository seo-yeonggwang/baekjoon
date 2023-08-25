def cook(Si, Bun):
    time = int(input())
    Cs = time//60
    Cb = time % 60
    
    Si = Si + Cs
    Bun = Bun + Cb
    
    if Bun >= 60:
        Bun = Bun - 60
        Si = Si + 1
        
    if Si >= 24:
        Si = Si - 24
        
    print(Si, Bun)
    
    return 0

Si, Bun = map(int, input().split())
cook(Si, Bun)
bino = int(input("quantos dedos você jogou bino?\n"))
cino = int(input("quantos dedos você jogou cino?\n"))

if bino < 10 or cino < 10:
    impar_ou_par = (bino + cino)%2
    if impar_ou_par == 0:
        print(f"{bino} mais {cino} é igual a par! Bino venceu!")
    else:
        print(f"{bino} mais {cino} é igual a impar! Cino venceu!")
else:
    print("Bino e cino, vcs so tem 10 dedos, digite um numero ate 10")
     

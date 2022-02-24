def run():
    #squares= []
    #for i in range(1,101):
        #Para guardar los números que no sean divisibles entre 3 
        #if i % 3 != 0:
            #squares.append(i**2)
        #print(squares) 
           
#Resolviendo por medio de list comprehensions

    squares =[i**2 for i in range(1,101) if i % 3 !=0]
    print(squares)

        





if __name__ == '__main__':
    run()





"""Se crea un arreglo en el cual se guardaran los elementos del for, que son 100 números elevados al cuadrado
Se agrega el if ya que es el que valida que los numeros que se guarden dentro de square No sean divisibles entre 3"""    

"""La línea 11 cumple la función de todas las líneas de código anteriores, ya que hace la validación desde la lista (array)
eleva el valor de i al cuadrado para todos los enelemento de i en el rango de 1 a 100 si el modulo de i es diferente de 3 
eso es lo que imprime"""
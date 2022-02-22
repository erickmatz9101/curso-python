from multiprocessing.sharedctypes import Value


def run ():
    my:list = [1,"Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname":"Garcia" }

    ##Creando una superlista que contenga diccionarios:
    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"},
    ]

    ##Creando un diccionario que contenga listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    ##Creando el ciclo for para poder recorrer las llaves y los diccionarios asi como imprimir sus valores 

    for key, value in super_dict.items():
        print(key,"-",value)






if __name__ == '__main__':

    run()



"""El método .ute permite recorrer las llaves y los valores de las llaves y los dicicionarios"""
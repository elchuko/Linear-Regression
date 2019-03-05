import random as rnd
#los archivos estan separados por espacio, no por coma, modificar el "split(" ")
#este script es solo para generar el archivo con el que se va a trabajar

def extract_my_data():
    data_file = "airfoil_self_noise_.csv"
    in_file = open(data_file, 'r')
    my_file = open("airfoil_jass_.csv", 'w') #iniciales

    #rnd.seed(17)#seed valor inicial, se puede quitar
    for line in in_file:
        r = rnd.random() #numero [0,1)
        if r < 0.2: #separar 20% de datos
            my_file.writelines(line)

    in_file.close()
    my_file.close()


def split_train_and_test():
    #separar aqui con 70% para entrenamiento y 30% para prueba
    #hacer programa que va linea por linea
    file_to_split = "airfoil_jass_.csv"
    in_file = open(file_to_split, 'r')
    train_file = open("airfoil_train_.csv",'w')
    test_file = open("airfoil_test_.csv",'w')

    for line in in_file:
        r = rnd.random()
        if r < 0.7:
            train_file.writelines(line)
        else:
            test_file.writelines(line)


if __name__ == "__main__":
    extract_my_data()
    split_train_and_test()


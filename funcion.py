def sumar(n1, n2):
    return n1+n2

def restar(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1/n2

n1 = int (input("ingresa el numero 1 :"))
n2 = int (input("ingresa el numero 2 :")) 

print("la suma es:", sumar(n1,n2))
print("la resta es:", restar(n1,n2))
print("la multiplicacion es:", multiplicar(n1,n2))
print("la division es:", dividir(n1,n2))
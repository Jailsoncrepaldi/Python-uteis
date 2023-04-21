def validate_cpf(num):
    n1 = int(num[0])
    n2 = int(num[1])
    n3 = int(num[2])
    n4 = int(num[3])
    n5 = int(num[4])
    n6 = int(num[5])
    n7 = int(num[6])
    n8 = int(num[7])
    n9 = int(num[8])
    d1 = n9 * 2 + n8 * 3 + n7 * 4 + n6 * 5 + n5 * 6 + n4 * 7 + n3 * 8 + n2 * 9 + n1 * 10
    d1 = 11 - (d1 % 11)
    if d1 >= 10:
        d1 = 0
    d2 = d1 * 2 + n9 * 3 + n8 * 4 + n7 * 5 + n6 * 6 + n5 * 7 + n4 * 8 + n3 * 9 + n2 * 10 + n1 * 11
    d2 = 11 - (d2 % 11)
    if d2 >= 10:
        d2 = 0
    calculated = str(d1) + str(d2)
    entered = num[9] + num[10]
    if calculated == entered:
        return True
    else:
        return calculated


# Exemplo de uso
cpf = input("Digite um cpf ")
res =validate_cpf(cpf)
if validate_cpf(cpf)==True:
    print("CPF válido")
else:
    print("CPF inválido")
    print("Correto seria",cpf[:-2]+res)
input()
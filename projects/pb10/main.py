from pb3.main import is_prime



def pour_n(n):
    somme = 0
    count = 0
    for i in range(3, n):
        if is_prime(i):
            somme += i
            count +=1
            # print(i)
    print(f"Somme pour n={n} est {somme} (somme de {count} nombres premiers)")


for n in range(10, 100):
    pour_n(n)


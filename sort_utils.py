import random

# adaptei o meu laboratorio de quicksort pra isso. de diferenças, basicamente ele possibilita inverter a ordem,
# também recebe key, que vai funcionar pra ordenar com base em um parametro do nodo (rating, por exemplo)
# o "arr" será uma lista montada com base na extração de dados da tabela hash

def partition_hoare(arr, left, right, key, reverse=False):
    pivot = arr[left]
    pivot_val = key(pivot)

    i = left
    j = right + 1

    while True:
        # anda i, se for crescente, i para de incrementar quando val_i for maior q o pivo, se for dec, i para de incrementar quando é menor q o pivo
        while True:
            i += 1
            if i == right:
                break

            val_i = key(arr[i])

            if (not reverse and val_i > pivot_val) or (reverse and val_i < pivot_val):
                break

        # anda j
        while True:
            j -= 1
            if j == left:
                break

            val_j = key(arr[j])

            if (not reverse and val_j <= pivot_val) or (reverse and val_j >= pivot_val):
                break

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


def choose_random(arr, left, right):            # pivo aleatorio
    r = random.randint(left, right)
    arr[left], arr[r] = arr[r], arr[left]

def quicksort_random_hoare(arr, left, right, key, reverse=False):
    if right > left:
        choose_random(arr, left, right)
        p = partition_hoare(arr, left, right, key, reverse)
        quicksort_random_hoare(arr, left, p - 1, key, reverse)
        quicksort_random_hoare(arr, p + 1, right, key, reverse)

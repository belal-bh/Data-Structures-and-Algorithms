def maximum_pairwise_product(numbers):
    product = numbers[0]*numbers[1]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            product = max(product, numbers[i]*numbers[j])
    return product


def maximum_pairwise_product_fast(numbers):
    index_1 = 0
    for i in range(1, len(numbers)):
        if numbers[index_1] < numbers[i]:
            index_1 = i
    
    if index_1 == 0:
        index_2 = 1
    else:
        index_2 = 0
    
    for i in range(1, len(numbers)):
        if i != index_1 and numbers[index_2] < numbers[i]:
            index_2 = i

    # print(index_1, index_2)
    product = numbers[index_1] * numbers[index_2]
    return product


def maximum_pairwise_product_fastest(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    product = sorted_numbers[0] * sorted_numbers[1]
    return product


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))

    # print(maximum_pairwise_product(numbers))
    print(maximum_pairwise_product_fast(numbers))
    # print(maximum_pairwise_product_fastest(numbers))
    # print(numbers)
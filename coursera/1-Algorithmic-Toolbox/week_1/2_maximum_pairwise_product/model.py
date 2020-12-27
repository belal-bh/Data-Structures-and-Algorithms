def maximum_pairwise_product(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    product = sorted_numbers[0] * sorted_numbers[1]
    return product


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    
    print(maximum_pairwise_product(numbers))

from numba import jit

@jit(nopython=True)
def min_coins(amount, denominations):
    # Сортируем номиналы в обратном порядке
    denominations.sort(reverse=True)
    count = 0

    for coin in denominations:
        while amount >= coin:
            amount -= coin
            count += 1
        if amount == 0:
            break

    return count

# Тестовые примеры
if __name__ == "__main__":
    denominations1 = [1, 5, 10, 25]
    amount1 = 99
    print(f"Сумма: {amount1}, Номиналы: {denominations1} -> Минимальное количество монет: {min_coins(amount1, denominations1)}")

    denominations2 = [1, 3, 4]
    amount2 = 6
    print(f"Сумма: {amount2}, Номиналы: {denominations2} -> Минимальное количество монет: {min_coins(amount2, denominations2)}")

    denominations3 = [1, 2, 5]
    amount3 = 11
    print(f"Сумма: {amount3}, Номиналы: {denominations3} -> Минимальное количество монет: {min_coins(amount3, denominations3)}")

    denominations4 = [10, 25, 50]
    amount4 = 80
    print(f"Сумма: {amount4}, Номиналы: {denominations4} -> Минимальное количество монет: {min_coins(amount4, denominations4)}")
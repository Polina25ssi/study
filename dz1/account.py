def calculate_income(rate, curen, month):
    if curen <= 0:
        return 0

    for i in range(1, month + 1):
        curen = round(curen + curen * rate / 100 / 12, 2)
    return curen


def main():
    rate =10
    cache = 100000
    period = 12

    result = calculate_income(rate, cache, period)
    print("Параметры счёта:\n", "Сумма:", cache,"\n", "Ставка: ", rate, "\n", "Период", period, "Сумма на счёте в конце периода:", result)

if __name__=="__main__":
    main()
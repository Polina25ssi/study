import account
import currency

def main():
    rate = int(input('Введите процентную ставку:'))
    money = int(input('Введите сумму:'))
    period = int(input('Введите период ведения счета в месяцах:'))

    curen= currency.cur(money)
    print("Внесено в банк:", curen)

    result= account.calculate_income(rate,curen,period)
    print('Параметры счета:\n', 'Сумма:', curen, '\n', 'Ставка:', rate, '\n', 'Период:', period, '\n', 'Сумма на счете в конце периода:', result)

if __name__ == "__main__":
    main()

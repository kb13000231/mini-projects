from requests import get
from pprint import PrettyPrinter

base_url = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()


def get_curr():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = base_url + endpoint
    data = get(url).json()['results']

    data = list(data.items())

    data.sort()

    return data


def print_curr(currs):
    for name, curr in currs:
        name = curr['currencyName']
        _id = curr['id']
        symbol = curr.get('currencySymbol', '')
        print(f"{_id} {name} {symbol}")
    print()


def exchange_rates(curr1, curr2):
    endpoint = f'api/v7/convert?q={curr1}_{curr2}&compact=ultra&apiKey={API_KEY}'
    url = base_url + endpoint
    res = get(url)

    data = res.json()

    if len(data) == 0:
        print('Invalid currencies')
        return
    rate = list(data.values())[0]
    print(f'{curr1} = {rate} {curr2}')

    return rate


def convert(curr1, curr2, amount):
    rate = exchange_rates(curr1, curr2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except Exception:
        print('Invalid amount')
        return

    conv_amount = rate*amount
    print(f'{amount} {curr1} is {conv_amount} {curr2}\n')
    return conv_amount


def main():
    currencies = get_curr()

    print("Welcome to currency converter")
    print('Available commands:')
    print('1- List\n2- Convert\n3- Exchange Rate(rate)\n')

    while True:
        command = input('Enter a command(q to exit): ').lower()

        if command == 'q':
            break
        elif command == 'list':
            print_curr(currencies)
        elif command == 'convert':
            curr1 = input('Enter your currency: ').upper()
            curr2 = input('Enter currency you want to convert to: ').upper()
            amount = input('Please enter the amount: ')
            convert(curr1, curr2, amount)
        elif command == 'rate':
            curr1 = input('Enter first currency: ').upper()
            curr2 = input('Enter currency you want to convert to: ').upper()
            exchange_rates(curr1, curr2)
        else:
            print('Invalid command! Please try again')


main()

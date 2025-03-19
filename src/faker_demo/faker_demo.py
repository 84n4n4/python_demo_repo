from faker import Faker

def main():
    fake = Faker('de_DE') # de_DE
    for _ in range(10):
        print(fake.name())

    print(fake.iban())
    print(fake.company_email())
    print(fake.paragraph())
    print(fake.csv(header=('time', 'sensor_mac', 'value'), data_columns=('{{date_time}}', '{{mac_address}}', '{{pyfloat}}')))


if __name__ == '__main__':
    main()
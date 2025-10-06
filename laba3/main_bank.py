import sys
from datetime import datetime

# ========== Исключения ==========
class BankError(Exception):
    """Базовое исключение банковской системы"""
    pass

class AccountExistsError(BankError):
    """Счет в этой валюте уже существует"""
    pass

class AccountNotFoundError(BankError):
    """Счет не найден"""
    pass

class InsufficientFundsError(BankError):
    """Недостаточно средств на счете"""
    pass

class UnauthorizedError(BankError):
    """Пользователь не владелец счета"""
    pass


# ========== Классы сущностей ==========
class Client:
    def __init__(self, client_id: str, name: str):
        self.client_id = client_id
        self.name = name
        self.accounts = {}   # { 'USD': Account, 'EUR': Account }

    def __str__(self):
        return f"{self.client_id} | {self.name}"


class Account:
    def __init__(self, account_id: str, client_id: str, currency: str):
        self.account_id = account_id
        self.client_id = client_id
        self.currency = currency.upper()
        self.balance = 0.0
        self.created_at = datetime.now()

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств на счете")
        self.balance -= amount

    def __str__(self):
        return f"Счет {self.account_id} | {self.currency} | Баланс: {self.balance:.2f}"


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.clients = {}   # {client_id: Client}

    # ---------- Управление клиентами ----------
    def register_client(self, client_id: str, name: str):
        # нормализация имени для сравнения (убираем пробелы и приводим к нижнему регистру)
        norm_name = name.strip().lower()
        # проверка по имени
        for cid, client in self.clients.items():
            if client.name.strip().lower() == norm_name:
                raise BankError(f"Клиент с именем '{name}' уже существует (ID: {cid}).")
        # проверка по ID
        if client_id in self.clients:
            raise BankError(f"Клиент с ID '{client_id}' уже существует.")
        # если всё ок — регистрируем
        self.clients[client_id] = Client(client_id, name)

    def get_client(self, client_id: str) -> Client:
        if client_id not in self.clients:
            raise BankError("Клиент не найден")
        return self.clients[client_id]

    # ---------- Управление счетами ----------
    def open_account(self, client_id: str, currency: str):
        client = self.get_client(client_id)
        if currency.upper() in client.accounts:
            raise AccountExistsError("Счет в этой валюте уже существует")

        account_id = f"{client_id}-{currency.upper()}"
        account = Account(account_id, client_id, currency)
        client.accounts[currency.upper()] = account
        return account

    def close_account(self, client_id: str, currency: str):
        client = self.get_client(client_id)
        if currency.upper() not in client.accounts:
            raise AccountNotFoundError("Счет не найден")
        del client.accounts[currency.upper()]

    # ---------- Операции со счетами ----------
    def deposit(self, client_id: str, currency: str, amount: float):
        account = self._get_account_for_client(client_id, currency)
        account.deposit(amount)

    def withdraw(self, client_id: str, currency: str, amount: float):
        account = self._get_account_for_client(client_id, currency)
        account.withdraw(amount)

    def transfer(self, from_client_id: str, from_currency: str, to_client_id: str, to_currency: str, amount: float):
        from_account = self._get_account_for_client(from_client_id, from_currency)
        to_account = self._get_account_for_client(to_client_id, to_currency)
        from_account.withdraw(amount)
        to_account.deposit(amount)

    # ---------- Выписка ----------
    def export_statement(self, client_id: str, filename: str):
        client = self.get_client(client_id)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Выписка по клиенту {client.name} ({client_id})\n")
            f.write("="*40 + "\n")
            for acc in client.accounts.values():
                f.write(f"{acc.currency}: {acc.balance:.2f}\n")
            f.write("="*40 + "\n")

    # ---------- Вспомогательные ----------
    def _get_account_for_client(self, client_id: str, currency: str) -> Account:
        client = self.get_client(client_id)
        if currency.upper() not in client.accounts:
            raise AccountNotFoundError("Счет не найден")
        account = client.accounts[currency.upper()]
        if account.client_id != client_id:
            raise UnauthorizedError("Вы не владелец счета")
        return account


# ========== Интерфейс терминала ==========
def main():
    bank = Bank("MINIONS")

    # Создадим несколько клиентов для теста
    bank.register_client("1", "Иван Иванов")
    bank.register_client("2", "Анна Смирнова")

    while True:
        print("\n=== БАНКОВСКАЯ СИСТЕМА ===")
        client_id = input("Введите ваш ID (или 'q' для выхода): ")
        if client_id.lower() == 'q':
            print("Выход...")
            exit()

        try:
            client = bank.get_client(client_id)
        except BankError:
            print("Клиент с таким ID не найден.")
            create = input("Хотите зарегистрировать нового клиента? (1-да/2-нет): ").strip().lower()
            if create == "1":
                name = input("Введите имя клиента: ").strip()
                if not name:
                    print("Имя не может быть пустым.")
                    continue
                try:
                    bank.register_client(client_id, name)
                    print(f"Клиент '{name}' успешно зарегистрирован с ID: {client_id}")
                    client = bank.get_client(client_id)
                except BankError as e:
                    # если ошибка — выводим сообщение (например, дублирование имени/ID)
                    print(f"Не удалось зарегистрировать клиента: {e}")
                    # дополнительно можно показать существующих клиентов с похожими именами
                    # (опционально)
                    similar = [f"{cid} ({c.name})" for cid, c in bank.clients.items()
                               if c.name.strip().lower() == name.strip().lower()]
                    if similar:
                        print("Найден(ы) существующий(ие) клиент(ы) с таким именем:", ", ".join(similar))
                    continue
            else:
                continue

        while True:
            print(f"\nДобро пожаловать, {client.name}!")
            print("1. Открыть счет")
            print("2. Закрыть счет")
            print("3. Пополнить счет")
            print("4. Снять со счета")
            print("5. Перевести деньги")
            print("6. Выписка в файл")
            print("7. Список счетов")
            print("8. Просмотр клиентов банка")
            print("9. Завершить программу")
            print("0. Сменить пользователя")

            choice = input("Выберите действие: ")

            try:
                if choice == "1":
                    currency = input("Введите валюту (например USD): ")
                    account = bank.open_account(client_id, currency)
                    print(f"Счет {account.account_id} успешно открыт")

                elif choice == "2":
                    currency = input("Введите валюту: ")
                    bank.close_account(client_id, currency)
                    print("Счет закрыт")

                elif choice == "3":
                    currency = input("Введите валюту: ")
                    amount = float(input("Введите сумму: "))
                    bank.deposit(client_id, currency, amount)
                    print("Счет пополнен")

                elif choice == "4":
                    currency = input("Введите валюту: ")
                    amount = float(input("Введите сумму: "))
                    bank.withdraw(client_id, currency, amount)
                    print("Снятие успешно выполнено")

                elif choice == "5":
                    from_currency = input("С какой валюты перевод: ")
                    to_client_id = input("ID получателя: ")
                    to_currency = input("Валюта получателя: ")
                    amount = float(input("Сумма: "))
                    bank.transfer(client_id, from_currency, to_client_id, to_currency, amount)
                    print("Перевод выполнен")

                elif choice == "6":
                    filename = f"statement_{client_id}.txt"
                    bank.export_statement(client_id, filename)
                    print(f"Выписка сохранена в файл {filename}")


                elif choice == "7":
                    print("\nВаши счета:")
                    if not client.accounts:  # словарь пустой
                       print("У вас нет открытых счетов.")
                    else:
                        for acc in client.accounts.values():
                            print(f"Счет: {acc.account_id} | Валюта: {acc.currency} | Баланс: {acc.balance}")

                elif choice == "8":
                    print("\n=== Список всех клиентов ===")
                    for cid, cl in bank.clients.items():
                        print(f"ID: {cid} | Имя: {cl}")

                elif choice == "9":
                    exit()

                elif choice == "0":
                    break

                else:
                    print("Неверный выбор")
            except BankError as e:
                print(f"Ошибка: {e}")
            except ValueError:
                print("Некорректный ввод числа")


if __name__ == "__main__":
    main()
base_minutes = 60
base_sms = 30
base_mb = 1024
base_price = 24.99

extra_minute_price = 0.89
extra_sms_price = 0.59
extra_mb_price = 0.79
tax_rate = 0.02
print("Введите целочисленные данные")
used_minutes = int(input("Введите количество израсходованных минут: "))
used_sms = int(input("Введите количество израсходованных SMS: "))
used_mb = int(input("Введите количество израсходованных МБ: "))

if used_minutes < 0 or used_sms < 0 or used_mb < 0:
    print("Ошибка: значения не могут быть отрицательными")


extra_minutes = max(0, used_minutes - base_minutes)
extra_sms = max(0, used_sms - base_sms)
extra_mb = max(0, used_mb - base_mb)

base_cost = base_price
extra_minutes_cost = extra_minutes * extra_minute_price
extra_sms_cost = extra_sms * extra_sms_price
extra_mb_cost = extra_mb * extra_mb_price

subtotal = base_cost + extra_minutes_cost + extra_sms_cost + extra_mb_cost

tax = subtotal * tax_rate

total = subtotal + tax

print("\n" + "=" * 50)
print(f"Базовая стоимость тарифа: {base_cost:.2f} руб.")

if extra_minutes > 0:
    print(f"Дополнительные минуты ({extra_minutes} мин.): {extra_minutes_cost:.2f} руб.")

if extra_sms > 0:
    print(f"Дополнительные SMS ({extra_sms} шт.): {extra_sms_cost:.2f} руб.")

if extra_mb > 0:
    print(f"Дополнительный трафик ({extra_mb} МБ): {extra_mb_cost:.2f} руб.")

print(f"Налог (2%): {tax:.2f} руб.")
print("-" * 50)
print(f"ИТОГО К ОПЛАТЕ: {total:.2f} руб.")
print("=" * 50)


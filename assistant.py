name = input("Як тебе звати ?")

print("Привіт,", name)
print("Я твій простий асистент.")

tasks = []
last_remaining = None
while True:
    command = input("Введи команду:").lower().strip()

    if command == "привіт":
        print("Привіт! Радий тебе бачити.")

    elif command == "як справи":
        print("У мене все добре. Готовий працювати!")

    elif command == "допомога":
        print("Я знаю команди: привіт, як справи, допомога, вихід")
    elif command == "список справ":
        print(tasks)
    elif command == "додати справу":
         task = input("Яку справу додати? ")
         tasks.append(task)
         print("Справу додано!")
    elif command == "маршрут":
          total = int(input("Скільки всього адрес на маршруті?"))
          delivered = int(input("Скільки адрес уже закрито?"))
          remaining = total - delivered
          if delivered > total:
              print("Перевір числа: закритих адрес більше, ніж усього на маршруті.")
          elif remaining == 0:
              last_remaining = remaining
              print("Маршрут завершено!")
          else:
              last_remaining = remaining
              print("Залишилось адрес:", remaining)
    elif command == "статус":
        if last_remaining is None: 
            print("Спочатку введи команду маршрут.")
        else:
            print("Останній залишок адрес:", last_remaining)
    elif command == "вихід":
         print("До зустрічі!")
         break

    else:
        print("Я поки не знаю такої команди.")


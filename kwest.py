print('Доброе утро,ты голоден?')
otvet = input("да,нет? ")
if otvet == "да":
    product = input("Есть продукты дома,да или нет?")
    if product == "да":
        print("Так вставай и иди готовь!")
    elif product == "нет":
        print("Собирайся в магазин!")
        while True:
            transport=input("Выбирай на чем поедешь:авто,такси,автобус? ")
            if transport == "авто":
                toplivo=input("А топливо есть????да,нет??? ")
                if toplivo== "да":
                    print("Пиши список продуктов!")
                    break
                else: print("Выбери другой транспорт")
            elif transport== "такси":
                taxi=input("Какой такси: убер или яндекс? ")
                if taxi == "убер":
                    print("оплата только по карте")
                    otvet1=input("согласны?да или нет")
                    if otvet1=="да":
                        print("Пиши список прдуктов!")
                        break
                    else:
                        print("Выбери другой транспорт")
                if taxi == "яндекс":
                    print("оплата только по карте или наличкой")
                    otvet1 = input("согласны?да или нет")
                    if otvet1 == "да":
                        print("Пиши список прдуктов!")
                        break
                    else: print("Выбери другой транспорт")
            elif  transport=="автобус" :
                print("Прверяй расписание!")
                raspisanie=input("автобус скоро или нет?")
                if raspisanie=="скоро":
                    print("Пиши список продуктов!")
                    break
                else: print("Выбери другой транспорт")
    input("Напиши список продуктов!:")
    print("Отлично!")
    print("Давай выберем магазин!")
    market=input("Какой магазин продпочитаешь: \n"
                 "1-с дешевыми фруктамиn \n"
                 "2-с недорогим алкоголем \n"
                 "3-с хорошей выпечкой \n"
                 "4-предложи свой вариант.... \n")
    if market== ("1" or "2" or "3"):
        print("Отлично!поехали!")
    elif market=="4":
        input("Введи свой магазин: ")
        print("Отлично!поехали!")
    print("Мы в магазине....")
    print("Набираем в корзину продукты....")
    print("Идем рассчитывться....")
    oplata=input("Как собираешься рассчитываться? \n"
          "1-банковской карточкой \n"
          "2-наличными \n"
          "Твой выбор: ")
    print("Отлично,тогда плати-"+oplata)
    print("При расчете на кассе возникает проблемка....")
    if oplata=="1":
        print("Карточка заблокирована!Давай в двери!")
    elif oplata=="2":
        print("Наличка фальшивая!Уходи в двери!")
    print("Дальше всё  понятно...не стоило это того...")
elif otvet == "нет":
    print("спи дальше!")

bucket_5 = 5
bucket_3 = 3
trigger = 0
print("""Есть загадка как говорится "от Стива Джобса 🍏".
Имеется 2 🪣, одно 3 литра другое 5 литров и неограниченное количество воды🚰.Необходимо получить 4 литра воды 
Пользователь может:
❕ Набирать воду в любое 🪣.
❕ Выливать воду из любого 🪣.
❕ Переливать воду из одного 🪣 в  другое 🪣.
""")
print('В 🪣 на 5л', bucket_5, '- литров воды\nВ 🪣 на 3л', bucket_3, '- литров воды')
print("""
fill_upbucket_5 - налить в ведро 5, fill_upbucket_3 - налить в ведро  3
pour_outbucket_5 - вылить из ведра 5, pour_outbucket_3 - вылить из ведра 3
bucket_5bucket_3 - перелить из ведра 5 в ведро 3, bucket_3bucket_5 - перелить из ведра 3 в ведро 5
quit - выход""")
while bucket_5 != 4:
    aqua = input(':')
    if aqua == 'quit':
        break
    elif aqua == 'fill_upbucket_5' and bucket_5 <= 5:
        bucket_5 = 5
        trigger += 1
        print(bucket_5, 'l - в 5-ти литровом 🪣')
    elif aqua == 'fill_upbucket_3' and bucket_3 <= 3:
        bucket_3 = 3
        trigger += 1
        print(bucket_3, 'l - в 3-ех литровом 🪣')
    elif aqua == 'pour_outbucket_5' and bucket_5 > 0:
        bucket_5 = 0
        trigger += 1
        print(bucket_5, 'l - в 5-ти литровом 🪣')
    elif aqua == 'pour_outbucket_3' and bucket_3 > 0:
        bucket_3 = 0
        trigger += 1
        print(bucket_3, 'l - в 3-ех литровом 🪣')
    elif aqua == 'bucket_5bucket_3' and bucket_3 != 3:
        if bucket_3 == 2 and bucket_5 >= 1:
            bucket_3 += 1
            bucket_5 -= 1
        elif bucket_3 == 1 and bucket_5 >= 2:
            bucket_3 += 2
            bucket_5 -= 2
        elif bucket_3 == 0 and bucket_5 == 5:
            bucket_3 += 3
            bucket_5 -= 3
        elif bucket_3 == 0 and bucket_5 == 3:
            bucket_3 += 3
            bucket_5 -= 3
        elif bucket_3 == 0 and bucket_5 == 2:
            bucket_3 += 2
            bucket_5 -= 2
        else:
            print('error 200')
        trigger += 1
        print(bucket_3, '🪣 3-l', bucket_5, '🪣 5-l')
    elif aqua == 'bucket_3bucket_5' and bucket_5 < 5:
        if bucket_5 == 4 and bucket_3 == 1:
            bucket_5 += 1
            bucket_3 -= 1
        elif bucket_5 == 3 and bucket_3 == 2:
            bucket_5 += 2
            bucket_3 -= 2
        elif bucket_5 == 3 and bucket_3 == 3:
            bucket_5 += 2
            bucket_3 -= 2
        elif bucket_5 == 2 and bucket_3 == 3:
            bucket_5 += 3
            bucket_3 -= 3
        elif bucket_5 == 1 and bucket_3 == 3:
            bucket_5 += 3
            bucket_3 -= 3
        elif bucket_5 == 0 and bucket_3 == 3:
            bucket_5 += 3
            bucket_3 -= 3
        elif bucket_5 == 0 and bucket_3 == 1:
            bucket_5 += 1
            bucket_3 -= 1
        else:
            print('error 100')
        trigger += 1
        print(bucket_3, '🪣 3-l', bucket_5, '🪣 5-l')
    else:
        'ошибка ввода'
print('вы закончили за', trigger, 'попыток')

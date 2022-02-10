import datetime
import random

a_file = open("foresights.txt", encoding='UTF-8')
file_contents = a_file.read()
contents_split = file_contents.split('.')

a_file.close()

print(datetime.date(2022, 2, 10) == datetime.date.today())

users_list = {"@pasha1561": 915489577, '@ira_hrdv': 455735498, '@ura': 1316194498, '@anastasia_preveda': 807119959, '@iryna_volodymyrivna': 651780710, '@tanya': 818234057, '@dmytro': 519468181}


def daily_suggestion():
    for user in users_list.values():
        message = ""
        if datetime.date(2022, 2, 10) == datetime.date.today():
            if user == 455735498:
                message = 'Іра, дивимось сьогодні гру престолів) \n І передбачення: \n ' + random.choice(contents_split).strip()
            elif user == 1316194498:
                message = 'Юра, маєш файну шкодовку) \n І передбачення: \n ' + 'a'
            elif user == 807119959:
                message = 'Настя, ти купила свічки? \n І передбачення: \n ' + random.choice(contents_split).strip()
            elif user == 651780710:
                message = 'Іра, не переживай, в тебе все вийде) \n І передбачення: \n ' + random.choice(contents_split).strip()
            elif user == 818234057:
                message = 'Єржан, вставай) \n І передбачення: \n ' + random.choice(contents_split).strip()
            elif user == 519468181:
                message = 'Дмитре, ніхуя собі блять маєш вихідний) \n І передбачення: \n ' + random.choice(contents_split).strip()
        else:
            message = random.choice(contents_split).strip()
        print(message)

daily_suggestion()
        # message = random.choice(contents_split).strip()


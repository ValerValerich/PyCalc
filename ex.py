import time
import logg
import ui
import operation


def check_nums(a, b, a1=0, b1=0):
    res = []
    for i in [a, a1, b, b1]:
        temp = False
        if str(i).isdigit():
            temp = True

        elif str(i)[0] == '-' and str(i)[1:].isdigit():
            temp = True

        elif str(i)[0].isdigit() and str(i).replace('.', '').isdigit() and str(i).find('.') >= 1 and str(i).count('.') < 2:
            temp = True

        elif str(i)[0] == '-' and str(i).replace('-', '').replace('.', '').isdigit() and str(i).find('.') >= 2 and str(i).count('-') <= 1 and str(i).count('.') <= 1:
            temp = True

        if temp:
            res.append(temp)
    if res == [True, True, True, True]:
        return True
    else:
        mess = "Ошибка с форматом цифр! Попробуем еще разок?\n\n\n"
        logg.logging.error(mess)
        print(mess)
        time.sleep(1)


def chech_in(a, b, ch, op='', a1=0, b1=0):
    if (ch == "/" or ch == '//') and (float(b) == 0 and float(b1) == 0):
        logg.logging.error("Деление на ноль!")
        print("Деление на ноль!")
        time.sleep(2.5)
        ui.first_displey()
    elif op == "r" and ch not in ['*', '**', '/', '//', '+', '-', '^', 'V', '%']:
        logg.logging.error("Недопустимая операция для рациональных чисел")
        print("Недопустимая операция для рациональных чисел\n\n\n")
        time.sleep(2.5)
        ui.first_displey()
    elif op == "k" and ch not in ['*', '**', '/', '+', '-', '^', 'V']:
        logg.logging.error("Недопустимая операция для комплексных чисел\n\n\n")
        print("Недопустимая операция для комплексных чисел")
        time.sleep(2.5)
        ui.first_displey()
    elif check_nums(a, b, a1, b1):
        if ch == 'V' and op == 'r':
            operation.sqrt_two_r_nums(a, b)
        elif ch == 'V' and op == 'k':
            operation.sqrt_two_k_nums(a, a1, b, b1)
        else:
            operation.math_operation(a, a1, b, b1, ch, op)
    else:
        logg.logging.error("Некорректные данные на входе")
        print("Правила нарушать нельзя. Будь внимательнее\n\n\n")
        time.sleep(2.5)
        ui.first_displey()

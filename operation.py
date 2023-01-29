import logg
import ui
import time


def math_operation(a, a1, b, b1, ch, op):
    if op == "r":
        logg.logging.info(f"{a} {ch} {b} = {round(eval(f'{a}{ch}{b}'), 3)}")
        print(f"{a} {ch} {b} = {round(eval(f'{a}{ch}{b}'), 3)}")
        print("Еще разок?\n"
              "\n")
        time.sleep(3.0)
        ui.first_displey()
    elif op == "k":
        logg.logging.info(
            f"{complex(float(a), float(a1))}{ch}{complex(float(b), float(b1))}={eval(f'{complex(float(a), float(a1))}{ch}{complex(float(b), float(b1))}')}")
        print(
            f"{complex(float(a), float(a1))}{ch}{complex(float(b), float(b1))}={eval(f'{complex(float(a), float(a1))}{ch}{complex(float(b), float(b1))}')}")
        print("Еще разок?\n"
              "\n")
        time.sleep(3.0)
        ui.first_displey()
    else:
        logg.logging.error("Что-то пошло не так во время вычислений!")
        print("Что-то пошло не так во время вычислений!")
        time.sleep(2.5)
        ui.first_displey()


def sqrt_two_r_nums(a, b):
    logg.logging.info(f"sqrt({a}) = {float(a)**0.5}\n"
                      f"sqrt({b}) = {float(b)**0.5}\n")
    print(f"sqrt({a}) = {float(a)**0.5}\n"
          f"sqrt({b}) = {float(b)**0.5}\n")
    print("Еще разок?"
          "\n")
    time.sleep(3.0)
    ui.first_displey()


def sqrt_two_k_nums(a, a1, b, b1):
    logg.logging.info(f"sqrt({complex(a, a1)}) = {eval(complex(a, a1)**0.5)}\n"
                      f"sqrt({complex(b, b1)}) = {eval(complex(b, b1)**0.5)}\n")
    print(f"sqrt({complex(a, a1)}) = {eval(complex(a, a1)**0.5)}\n"
          f"sqrt({complex(b, b1)}) = {eval(complex(b, b1)**0.5)}\n")
    print("Еще разок?"
          "\n")
    time.sleep(3.0)
    ui.first_displey()

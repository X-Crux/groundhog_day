from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777

current_carma = 0
days = 0


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day(dice):
    if dice == 1:
        raise IamGodError(f'IamGodError')
    elif dice == 2:
        raise DrunkError(f'DrunkError')
    elif dice == 3:
        raise CarCrashError(f'CarCrashError')
    elif dice == 4:
        raise GluttonyError(f'GluttonyError')
    elif dice == 5:
        raise DepressionError(f'DepressionError')
    elif dice == 6:
        raise SuicideError(f'SuicideError')

    carma_value = randint(1, 7)
    print(f'Карма сегодня + {carma_value}')

    return carma_value


def exc_handling(exc):
    print(f'Поймано исключение {exc}')
    with open('log.txt', mode='a') as file:
        file.write(f'День {days}. Поймано исключение {exc}\n')


while current_carma < ENLIGHTENMENT_CARMA_LEVEL:

    dice = randint(1, 13)
    days += 1

    try:
        current_carma += one_day(dice)
    except IamGodError as exc:
        exc_handling(exc)
    except DrunkError as exc:
        exc_handling(exc)
    except CarCrashError as exc:
        exc_handling(exc)
    except GluttonyError as exc:
        exc_handling(exc)
    except DepressionError as exc:
        exc_handling(exc)
    except SuicideError as exc:
        exc_handling(exc)
    finally:
        print(f'Дней прошло {days}. Карма итого: {current_carma}')

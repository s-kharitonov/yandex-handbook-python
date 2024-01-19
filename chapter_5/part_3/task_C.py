# Ломать — не строить 2
# Вашему решению будет предоставлена функция func,
# которая на этот раз принимает неограниченное число позиционных параметров
# и производит с ними некую операцию приведения типа.
#
# Предложите вызов функции, который гарантированно породит ошибку внутри функции.
#
# Примечание
# Если ошибка произойдёт внутри функции, то она будет перехвачена и обработана.
# Если же она произойдет в вашем коде, то программа будет завершена с ошибкой.

class Error:

    def __repr__(self):
        raise TypeError


func(Error())

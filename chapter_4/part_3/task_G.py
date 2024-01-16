# Однотипность не порок
# Во многих задачах требуется контроль входных данных, в частности, несмотря на динамическую типизацию, их типов.
#
# Разработайте декоратор same_type, который производит проверку переменного количества позиционных параметров.
# В случае получения не одинаковых типов выводит сообщение "Обнаружены различные типы данных"
# и прерывает выполнение функции.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def same_type(fn):
    def decorated_function(*args):
        first_arg_type = type(args[0])
        if any(type(arg) is not first_arg_type for arg in args):
            print('Обнаружены различные типы данных')
            return
        return fn(*args)

    return decorated_function

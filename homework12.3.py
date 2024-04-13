from datetime import datetime

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        execution_time = datetime.now() - start_time
        print(f"Функция '{func.__name__}' выполнилась за {execution_time}")
        return result
    return wrapper

@measure_time
def func1():
    for _ in range(500000):
        pass

@measure_time
def func2():
    for _ in range(500000):
        pass

func1()
func2()
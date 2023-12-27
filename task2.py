import threading


def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@printer
def reverse_number(n):
    return int(str(n)[::-1])


def main():
    numbers = input("Son kiriting: ").split()
    for num in numbers:
        threading.Thread(target=reverse_number, args=(num,)).start()


if __name__ == "__main__":
    main()

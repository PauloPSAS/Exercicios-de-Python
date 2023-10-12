from time import sleep


def maior(*num):
    m = c = 0
    sleep(2.5)
    print("-=" * 30)
    print("Analisando os valores passados...")
    for value in num:
        print(value, end=' ', flush=True)
        sleep(.5)
        if c == 0:
            m = value
        else:
            if value > m:
                m = value
        c += 1
    print(f"Foram informados {c} valores ao todo.")
    print(f"O maior valor informado foi {m}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0, 8, 3, 1, 1, 0, 9)
maior(1, 2, 15, 17, 28, 21)
maior(6, 9, 6, 5, 0, 3)
maior()
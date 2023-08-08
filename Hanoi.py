def hanoi(height, start, to):
    if height ==1:
        print(f'from {start } to {to}')
        return

    temp = 6 - start - to
    hanoi(height-1, start, temp)
    print(f'from {start} to {to}')
    hanoi(height-1, temp, to)

hanoi(4, 1, 2)
with open('Demo.txt', 'r') as f:

    # for line in f:
    #     print(line, end='')

    size_to_read = 10

    f_content = f.read(size_to_read)

    while len(f_content) > 0:
        print(f_content, end='')
        f_content = f.read(size_to_read)

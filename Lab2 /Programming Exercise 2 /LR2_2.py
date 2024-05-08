def navigate_file():
    filename = input("Enter a filename: ")
    try:
        with open(filename, 'r') as f:
            file_contents = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("File not found. Please try again.")
        return

    while True:
        print(f"The file has {len(file_contents)} lines.")
        print("Enter a line number (0 to quit): ", end='')
        line_num = int(input())
        if line_num == 0:
            break
        elif 1 <= line_num <= len(file_contents):
            print(file_contents[line_num - 1])
        else:
            print("Invalid line number. Please try again.")

navigate_file()

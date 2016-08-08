def main():
    file = open('problem1.txt')

    row_hints = []
    column_hints = []

    blank_lines_seen = 0
    for line in file:
        line = line.strip()

        if line == '':
            blank_lines_seen += 1
        else:
            if blank_lines_seen == 0:
                row_hints.append([int(x) for x in line.split()])
            elif blank_lines_seen == 1:
                column_hints.append([int(x) for x in line.split()])
            else:
                raise Exception('Bad file format.')

    print(row_hints)
    print(column_hints)

if __name__ == '__main__':
    main()

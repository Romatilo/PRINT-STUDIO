def count_lines(filename, chunk_size=1<<13):
    with open(filename, encoding="utf-8") as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

f = open("C:\!!Study\PRINT-STUDIO\defects.csv", "r", encoding="utf-8")
lines_number = count_lines("C:\!!Study\PRINT-STUDIO\defects.csv")
empty = "         "
string_U = "46 УЧЕБНАЯ"
U46 = open("U46.csv", "a+")
for line in f:
    if (string_U in line):
        subline = line[line.find("46 УЧЕБНАЯ") : line.find("           ")]
        U46.writelines(subline)
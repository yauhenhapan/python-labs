# -*- coding: utf-8 -*-
import xml.sax.saxutils
import sys

def main():
    options = maxwidth, nformat = process_options()
    if options != (None, None):
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, nformat)
                count += 1
            except EOFError:
                break
        print_end()

def print_start():
    print("<table border='1'>")

def print_end():
    print("</table>")

def print_line(line, color, maxwidth, nformat):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                string = "<td align='right'>{0:{1}}</td>".format(number, nformat)
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = xml.sax.saxutils.escape(field)
                if len(field) <= maxwidth:
                    print("<td>{0}</td>".format(field))
                else:
                    print("<td>{0:.{1}} ...</td>".format(field, maxwidth))
    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:  # начало строки в кавычках
                quote = c
            elif quote == c:  # конец строки в кавычках
                quote = None
            else:
                field += c
                # другая кавычка внутри строки в кавычках
                continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c
            # добавить символ в поле
    if field:
        fields.append(field)  # добавить последнее поле в список
    return fields

def process_options():
    maxwidth = 100
    nformat = ".0f"
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            message = ("usage:\ncsv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html \nmaxwidth - необязательное целое число. Если задано, определяет"
                        + "\nмаксимальное число символов для строковых полей. В противном случае"
                        + "\nиспользуется значение по умолчанию 100."
                        + "\n\nformat - формат вывода чисел. Если не задан, по умолчанию используется"
                        + """\nформат ".0f".""")
            print(message)
            return None, None
        else:
            for arg in sys.argv[1:]:
                if arg.startswith("maxwidth"):
                    maxwidth = int(arg.split("=")[1])
                elif arg.startswith("format"):
                    nformat = arg.split("=")[1]
    return maxwidth, nformat


main()

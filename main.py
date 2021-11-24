import pdfplumber
import re

grades = {'A': 5.0, 'B': 4.5, 'C': 4.0, 'D': 3.5, 'E': 3.0, 'F': 0.0}

with pdfplumber.open("intyg.pdf") as pdf:
    pages = pdf.pages
    sum_1 = 0
    sum_2 = 0

    for k, page in enumerate(pages):
        table = page.extract_table(table_settings={"vertical_strategy":"text",
                                                    "horizontal_strategy":"text",
                                                    })
        for line in table:
            found = False
            for i, item in enumerate(line):
                if re.search(r"\dhp", item):
                    hp = float(item.strip('hp'))
                    found = True
                    index = i
            if found:
                if line[index+1] in grades.keys():
                    points = grades[line[index+1]]
                    sum_1 += hp * points
                    sum_2 += hp
    print(f"Your GPA is: {round(sum_1 / sum_2, 1)}")


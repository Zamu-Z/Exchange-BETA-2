from website import url_link
import string
from time import process_time

table = url_link().find("table", {"id": "ctl00_PlaceHolderMain_dgAvg"})
countries = table.find_all("tr", {"class": "bg-gray"})


def data_1():
    list_country = []
    for n, c in enumerate(countries):
        c1 = countries[n].text.strip()
        c2 = c1.split()
        if c2[0][len(c2[0]) - 1] not in string.ascii_uppercase:
            c2[0] = c2[0] + c2[1] + c2[2] + c2[3]
            del c2[1:4]
        if c2[0][len(c2[0]) - 3] in string.ascii_uppercase:
            c2[0] = c2[0][:len(c2[0]) - 3] + " " + c2[0][len(c2[0]) - 3:]
            split = c2[0].split()
            c2[0] = split[0]
            c2.insert(1, split[1])
        c2[2] = float(c2[2])
        c2[3] = float(c2[3])
        c2[4] = float(c2[4])
        list_country.append(c2)
    return list_country


if __name__ == "__main__":
    print(process_time())

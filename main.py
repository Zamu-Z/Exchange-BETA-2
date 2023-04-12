import os
from datetime import datetime
from dict_of_file import dict_month
from tkinter.messagebox import showerror, askokcancel, showinfo
from format_excel import format_excel
from tkinter.filedialog import askdirectory

now = datetime.now()
content_ask = "ตอนนี้ : " + str(now.day) + " " + list(dict_month)[now.month - 1] + " " + str(now.year + 543)


def file_directory():
    ask = askdirectory()
    with open(file="path.txt", mode="a") as file:
        file.write(ask + "\n")
    with open(file="path.txt", mode="r") as file:
        file_read = file.read()
        f = file_read.split()
        path = f[-1]
        print(path + "/")


def control_file(new):
    try:
        # path_f = os.listdir(path_file)
        if now.day >= 1:
            ask = askokcancel("Exchange", content_ask)
            if ask is True:
                ask_directory = askdirectory()
                if bool(ask_directory) is True:
                    with open(file="path.txt", mode="a") as file:
                        file.write(ask_directory + "\n")
                        file.close()
                    with open(file="path.txt", mode="r+") as file_write:
                        file_read = file_write.read()
                        f = file_read.split()
                        path = f[-1]
                        path_file = path + "/"
                        file_write.close()

                    path_f = os.listdir(path_file)

                    if new_file() not in path_f:
                        if path[-1] != "/":
                            format_excel(path + "/" + new)
                        else:
                            format_excel(path + new)
                        showinfo("Exchange", "บันทึกแล้ว")

                    else:
                        showerror("Exchange", "มีไฟล์นี้ใน Folder นี้แล้ว")
                else:
                    showerror("Exchange", "ยกเลิกการบันทึก")
            else:
                showerror("Exchange", "File ไม่ถูกบันทึก")

    except FileNotFoundError:
        p = "Folder ที่จะบันทึก ถูกปิดอยู่"
        showerror("Exchange", p)

    finally:
        with open(file="path.txt", mode="r+") as file_text:
            read = file_text.readlines()
            if len(read) > 10:
                file_text.seek(0)
                file_text.truncate()
                file_text.writelines(read[7:])
            file_text.close()


def new_file():
    year = str(now.year + 543)
    month = list(dict_month)[now.month - 1]
    new1 = year + "-" + month + ".xlsx"
    return new1


if __name__ == '__main__':
    control_file(new_file())

from tkinter import *
import random
import csv
import os.path

score = 0
window = Tk()
window.configure(bg='tan')
window.geometry("500x500")
window.resizable(False, False)
window.title("Dice Roller - Odds or Evens")
entername = Entry(window)
entername.pack(side='top')
frame_status = Frame()
radio_status = IntVar()
radio_status.set(0)
Oddbutton = Radiobutton(frame_status, text="Odds", variable=radio_status, value=1, bg='tan')
Evenbutton = Radiobutton(frame_status, text="Evens", variable=radio_status, value=2, bg='tan')
Evenbutton.pack(side='right')
Oddbutton.pack(side='left')
frame_status.pack(anchor='w', padx=190, )
frame_roll_label = Frame(window)
roll_label = Label(window,text='',bg='tan',width = 30)
roll_label.pack(side='bottom')
frame_pointslabel = Frame(window)
pointslabel = Label(window,text=score,bg='tan')
pointslabel.pack(side='bottom',pady=70)




def convert_dice(d:str)->int:
    """
    convert the unicode for the dice into numeric values
    :param d:
    :return: d
    """
    if d == '\u2680':
        return 1
    elif d == '\u2681':
        return 2
    elif d == '\u2682':
        return 3
    elif d == '\u2683':
        return 4
    elif d == '\u2684':
        return 5
    else:
        return 6


def roll_dices()-> None:
    """
    randomly rolls the dices and gets the status from the radio button and user name
    :return: none
    """
    global score
    dice = ['\u2680', '\u2681',
            '\u2682', '\u2683',
            '\u2684', '\u2685']
    one = random.choice(dice)
    two = random.choice(dice)
    four = random.choice(dice)
    three = random.choice(dice)

    label.configure(
        text=f'{one}{two}')
    label.pack()
    convertednum = convert_dice(one)
    convertednumtwo = convert_dice(two)
    status = radio_status.get()
    if status == 1:
        status = 'ODDS'
    elif status == 2:
        status = 'EVENS'
    else:
        status = 'UNSELECTED'
    if convertednum % 2 == 0 and convertednumtwo % 2 == 0 and status == 'EVENS':
        roll_label.config(text='EVENS')
        score += 100
        pointslabel.config(text=score)
    elif convertednum % 2 != 0 or convertednumtwo % 2 != 0 and status == 'ODDS':
        roll_label.config(text='ODDS')
        score += 100
        pointslabel.config(text=score)

    name = entername.get()
    info = [name, status, roll_label.cget('text'), convertednum, convertednumtwo]

    # Check if file exists, create it if it doesn't
    file_exists = os.path.isfile('diceroll.csv')
    with open('diceroll.csv', 'a', newline='') as csv_file:
        headers = ['Name', 'Selection', 'Result', 'Dice 1', 'Dice 2','Score']
        dictwriter_object = csv.DictWriter(csv_file, fieldnames=headers)
        if not file_exists:
            dictwriter_object.writeheader()
        dictwriter_object.writerow({
            'Name': name,
            'Selection': status,
            'Result': roll_label.cget('text'),
            'Dice 1': convertednum,
            'Dice 2': convertednumtwo,
            'Score': score
        })

    # Clear the input field
    entername.delete(0, END)

    # Close the CSV file
    csv_file.close()

roll_button = Button(window, text="Roll!",
                     width=15, height=2,
                     font=15, bg="grey",
                     bd=2, command=roll_dices)
# Setting the position of the button
roll_button.pack(padx=10, pady=15)

# Adding Label
label = Label(window, font=("times", 100),
              bg="tan", fg="white")

window.mainloop()
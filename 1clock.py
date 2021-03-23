from tkinter import *
from tkinter.ttk import *
from datetime import datetime
import pygame, time

#Tkinter window
window = Tk(className='Clock')
window.geometry('600x230')  #size of window
window.configure(bg='LavenderBlush2') #changed bg to a different colour
window.resizable(False, False)  #prevents resizing window

#operates stopwatch
stopwatch_counter_num = 66600
stopwatch_running = False


def clock():
    date_time = datetime.now()
    date = date_time.strftime('%b %d %Y     %A') #shows date, month/date/year/week
    time = date_time.strftime('%I:%M:%S %p') #shows time in 12hr clock with am/pm indication
#converted date & time into tkinter labels to display output into window
    date_label.config(text= date)
    time_label.config(text= time)
    time_label.after(1000, clock)


def alarm():
    date_time = datetime.now()
    time_now = date_time.strftime('%I:%M %p') #current date/time
    alarm_time = alarm_time_input.get() #asks user to input time for alarm
    if str(alarm_time) == str(time_now):  #conditional statement, compares current time to user input time
        alarm_status_label.config(text='It is time!')
        pygame.mixer.init()
        sounda = pygame.mixer.Sound('/Users/marichuanne/Downloads/trumpet.wav') 
        sounda.play()   #song starts when condition met
        pygame.mixer.fadeout(10000) #song is 9 mins long, song will slowly fadeout after 10s

        alarm_time_input.config(state='enabled')
        set_alarm_button.config(state='enabled')
        alarm_time_input.delete(0,END)      #input box will reset once alarm is fulfilled
        alarm_status_label.config(text='')
        
    else:
        alarm_status_label.config(text='Alarm Started')
        alarm_time_input.config(state='disabled')   #only 1 alarm input at a time
        set_alarm_button.config(state='disabled')
        alarm_status_label.after(1000, alarm)


def stopwatch_counter(label):
    def count():
        if stopwatch_running:
            global stopwatch_counter_num
                if stopwatch_counter_num==66600:
                    display="Starting..."
                else:
                    tt = datetime.datetime.fromtimestamp(stopwatch_counter_num) 
                    string = tt.strftime("%H:%M:%S") 
                    display=string 
                label.config(text=display)
                label.after(1000, count)
                stopwatch_counter_num += 1
    count()

    
#Notebook initialization
tabs_control = Notebook(window)

#clock
clock_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text='Clock')
date_label = Label(clock_tab, font='calibri 30')
date_label.pack(anchor='center')
time_label = Label(clock_tab, font='calibri 50 bold')
time_label.pack(anchor='center')

#alarm
alarm_tab = Frame(tabs_control)
tabs_control.add(alarm_tab, text='Alarm')
alarm_time_input = Entry(alarm_tab, font='calibri 15 bold')
alarm_time_input.pack(anchor='center')
alarm_instructions_label = Label(alarm_tab, font= 'calibri 10 bold', text='Enter Alarm Time.\nFormat: 00:00 PM')
alarm_instructions_label.pack(anchor='s')
set_alarm_button = Button(alarm_tab, text='Set', command=alarm)
set_alarm_button.pack(anchor='s')
alarm_status_label = Label(alarm_tab, font='calibri 15 bold')
alarm_status_label.pack(anchor='s')

#stopwatch
stopwatch_tab = Frame(tabs_control)
tabs_control.add(stopwatch_tab, text='Stopwatch')
stopwatch_label = Label(stopwatch_tab, font='calibri 40 bold', text='Stopwatch')
stopwatch_label.pack(anchor='center')
stopwatch_start = Button(stopwatch_tab, text='Start', command=lambda:stopwatch('start'))
stopwatch_start.pack(anchor='center')
stopwatch_stop = Button(stopwatch_tab, text='Stop', state='disabled',command=lambda:stopwatch('stop'))
stopwatch_stop.pack(anchor='center')
stopwatch_reset = Button(stopwatch_tab, text='Reset', state='disabled', command=lambda:stopwatch('reset'))
stopwatch_reset.pack(anchor='center')

#timer
timer_tab = Frame(tabs_control)
tabs_control.add(timer_tab, text='Timer')


tabs_control.pack(expand= 1, fill='both')


clock()
window.mainloop()
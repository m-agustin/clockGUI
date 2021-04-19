from tkinter import *
from tkinter.ttk import *
from datetime import datetime
import pygame, time

#Tkinter window
window = Tk(className='Clock')
window.geometry('600x250')  #size of window
window.configure(bg='LavenderBlush2') #changed bg to a different colour
window.resizable(False, False)  #prevents resizing window

#Stopwatch functions
stopwatch_counter_num = -1
stopwatch_running = False
#Timer functions
timer_counter_num = 60000   #1 minute
timer_running = False

def clock():
    date_time = datetime.now()
    date = date_time.strftime('%b %d %Y     %A') #shows date, month/date/year/week
    time = date_time.strftime('%I:%M:%S %p') #shows time in 12hr clock with am/pm indication
#converted date & time into tkinter labels to display output into window
    date_label.config(text=date)
    time_label.config(text=time)
    time_label.after(1000, clock)


def alarm():
    date_time = datetime.now()
    time_now = date_time.strftime('%I:%M %p') #current date/time
    alarm_time = alarm_time_input.get() #asks user to input time for alarm
    if str(alarm_time) == str(time_now):  #conditional statement, compares current time to user input time
        alarm_status_label.config(text='It is time!')
        pygame.mixer.init()
        sounda = pygame.mixer.Sound('/Users/marichuanne/Desktop/clockGUI/trumpet.wav') 
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
            if stopwatch_counter_num == -1:     #stopwatch starts if counter at -1
                stopwatch_label='Starting...'
            else:
                stopwatch_time = datetime.fromtimestamp(stopwatch_counter_num)  #if stopwatch started, output will be counting up in hr:m:s format
                stopwatch_time_now = stopwatch_time.strftime('%H:%M:%S')
                stopwatch_label = str(stopwatch_time_now)
            label.config(text=stopwatch_label)
            label.after(1000, count)    #adds 1second/1000milliseconds to time
            stopwatch_counter_num += 1 
    count() #will continue to run until stopped/reset

def stopwatch(work):
    if work == 'start':     #start button, will start stopwatch, allowed to stop & reset
        global stopwatch_running
        stopwatch_running = True
        stopwatch_start.config(state='disabled')
        stopwatch_stop.config(state='enabled')
        stopwatch_reset.config(state='enabled')
        stopwatch_counter(stopwatch_label)
    elif work == 'stop':    #stop button, will pause/stop stopwatch, allowed to start & reset
        stopwatch_running = False
        stopwatch_start.config(state='enabled')
        stopwatch_stop.config(state='disabled')
        stopwatch_reset.config(state='enabled')
    elif work == 'reset':   #reset button, will turn counter back to zero
        global stopwatch_counter_num
        stopwatch_running = True
        stopwatch_counter_num = -1
        stopwatch_label.config(state='Stopwatch')
        stopwatch_start.config(state='enabled')
        stopwatch_stop.config(state='enabled')
        stopwatch_reset.config(state='disabled')


def timer_counter(label):
    def count():
        global timer_running
        if timer_running:
            global timer_counter_num
            if timer_counter_num == 60000:      #if input time is reached, wav file will play and timer resets
                timer_label='Time is up!'
                pygame.mixer.init()
                sounda = pygame.mixer.Sound('/clockGUI/trumpet.wav') 
                sounda.play()
                pygame.mixer.fadeout(10000)
                timer_running = False
                timer('reset')
            else:
                timer_time = datetime.fromtimestamp(timer_counter_num)
                timer_time_now = timer_time.strftime('%H:%M:%S')
                timer_label = timer_time_now
                timer_counter_num -= 1      #timer will subtract 1 second from user's input every time
            label.config(text=timer_label)
            label.after(1000, count)
    count()

def timer(work):
    if work == 'start':
        global timer_running, timer_counter_num
        timer_running = True
        if timer_counter_num == 60000:
            timer_time = timer_input.get()
            hrs,mins,secs = timer_time.split(':')
            mins = int(mins) + (int(hrs) * 60)
            secs = int(secs) + (mins * 60)
            timer_counter_num = timer_counter_num + secs    #Displays the amount of time left from the user's input
        timer_counter(timer_label)
        timer_start.config(state='disabled')
        timer_stop.config(state='enabled')
        timer_reset.config(state='enabled')
        timer_input.delete(0,END)
    elif work == 'stop':
        timer_running = False
        timer_start.config(state='enabled')
        timer_stop.config(state='disabled')
        timer_reset.config(state='enabled')
    elif work == 'reset':
        timer_running = False
        timer_counter_num = 60000
        timer_start.config(state='enabled')
        timer_stop.config(state='disabled')
        timer_reset.config(state='disabled')
        timer_input.config(state='enabled')
        timer_label.config(text='Timer')


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
timer_input = Entry(timer_tab, font='calibiri 15 bold')
timer_input.pack(anchor='center')
timer_instructions_label = Label(timer_tab, font='calibri 10 bold', text='Enter Timer Time.\nFormat: 00:00:00')
timer_instructions_label.pack(anchor='s')
timer_label = Label(timer_tab, font='calibri 40 bold', text='Timer')
timer_label.pack(anchor='center')
timer_start = Button(timer_tab, text='Start', command=lambda:timer('start'))
timer_start.pack(anchor='center')
timer_stop = Button(timer_tab, text='Stop', state='disabled',command=lambda:timer('stop'))
timer_stop.pack(anchor='center')
timer_reset = Button(timer_tab, text='Reset', state='disabled', command=lambda:timer('reset'))
timer_reset.pack(anchor='center')

tabs_control.pack(expand= 1, fill='both')


clock()
window.mainloop()

# Written by Colton Magnant
# Adapted from Henry Smith's Journal program: https://github.com/HenrySmith3/Journal
# Checklist adapted from Mind Journal Jotter

from tkinter import *
from tkinter import ttk
from datetime import date, timedelta
import random
import os

class Journal():
    def __init__(self, root):

        self.dt = date.today() # Extract today's date for default view

        # Create and pack frames
        self.dateFrame = Frame(root)
        self.dateFrame.pack(side=TOP)
        self.checkFrame = Frame(root)
        self.checkFrame.pack(side=TOP)
        self.mainFrame = Frame(root)
        self.mainFrame.pack(side=TOP)

        # Here starts the date frame
        ttk.Button(self.dateFrame, text="<<", command = self.weekBack).grid(row=0, column=0)
        ttk.Button(self.dateFrame, text="<", command = self.dayBack).grid(row=0, column=1)
        self.dt_label = Label(self.dateFrame, text=str(self.dt))
        self.dt_label.grid(row=0, column=2)
        ttk.Button(self.dateFrame, text=">", command = self.dayFore).grid(row=0, column=3)
        ttk.Button(self.dateFrame, text=">>", command = self.weekFore).grid(row=0, column=4)
        ttk.Button(self.dateFrame, text="Save", command = self.onSave).grid(row=0, column=5)

        # Here starts the checkbox frame
        Label(self.checkFrame, text="Feeling?").grid(row=0, column=0, sticky=E)

        self.pixel = PhotoImage(width=1, height=1)
        Button(self.checkFrame, text="Clear Checks", image=self.pixel, width=70, height=7, compound='c', command=self.clearChecks).grid(row=1, column=0, sticky=E)
        
        col=1
        self.var_positive = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Positive', variable=self.var_positive).grid(row=0, column=col, sticky=W)
        self.var_happy = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Happy', variable=self.var_happy).grid(row=1, column=col, sticky=W)
        self.var_glad = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Glad', variable=self.var_glad).grid(row=2, column=col, sticky=W)
        self.var_worried = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Worried', variable=self.var_worried).grid(row=3, column=col, sticky=W)
        self.var_insecure = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Insecure', variable=self.var_insecure).grid(row=4, column=col, sticky=W)
        self.var_confused = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Confused', variable=self.var_confused).grid(row=5, column=col, sticky=W)
        self.var_proud = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Proud', variable=self.var_proud).grid(row=6, column=col, sticky=W)
        self.var_safe = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Safe', variable=self.var_safe).grid(row=7, column=col, sticky=W)

        col=2
        self.var_hopeful = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Hopeful', variable=self.var_hopeful).grid(row=0, column=col, sticky=W)
        self.var_stressed = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Stressed', variable=self.var_stressed).grid(row=1, column=col, sticky=W)
        self.var_bored = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Bored', variable=self.var_bored).grid(row=2, column=col, sticky=W)
        self.var_tired = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Tired', variable=self.var_tired).grid(row=3, column=col, sticky=W)
        self.var_hurt = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Hurt', variable=self.var_hurt).grid(row=4, column=col, sticky=W)
        self.var_eager = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Eager', variable=self.var_eager).grid(row=5, column=col, sticky=W)
        self.var_angry = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Angry', variable=self.var_angry).grid(row=6, column=col, sticky=W)
        self.var_excited = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Excited', variable=self.var_excited).grid(row=7, column=col, sticky=W)

        col=3
        self.var_nervous = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Nervous', variable=self.var_nervous).grid(row=0, column=col, sticky=W)
        self.var_tense = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Tense', variable=self.var_tense).grid(row=1, column=col, sticky=W)
        self.var_irritated = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Irritated', variable=self.var_irritated).grid(row=2, column=col, sticky=W)
        self.var_disappointed = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Disappointed', variable=self.var_disappointed).grid(row=3, column=col, sticky=W)
        self.var_content = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Content', variable=self.var_content).grid(row=4, column=col, sticky=W)
        self.var_negative = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Negative', variable=self.var_negative).grid(row=5, column=col, sticky=W)
        self.var_annoyed = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Annoyed', variable=self.var_annoyed).grid(row=6, column=col, sticky=W)
        self.var_inspired = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Inspired', variable=self.var_inspired).grid(row=7, column=col, sticky=W)

        col=4
        self.var_anxious = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Anxious', variable=self.var_anxious).grid(row=0, column=col, sticky=W)
        self.var_determined = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Determined', variable=self.var_determined).grid(row=1, column=col, sticky=W)
        self.var_grateful = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Grateful', variable=self.var_grateful).grid(row=2, column=col, sticky=W)
        self.var_unhappy = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Unhappy', variable=self.var_unhappy).grid(row=3, column=col, sticky=W)
        self.var_frustrated = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Frustrated', variable=self.var_frustrated).grid(row=4, column=col, sticky=W)
        self.var_furious = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Furious', variable=self.var_furious).grid(row=5, column=col, sticky=W)
        self.var_calm = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Calm', variable=self.var_calm).grid(row=6, column=col, sticky=W)
        self.var_strong = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Strong', variable=self.var_strong).grid(row=7, column=col, sticky=W)

        col=5
        self.var_neutral = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Neutral', variable=self.var_neutral).grid(row=0, column=col, sticky=W)
        self.var_regretful = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Regretful', variable=self.var_regretful).grid(row=1, column=col, sticky=W)
        self.var_lonely = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Lonely', variable=self.var_lonely).grid(row=2, column=col, sticky=W)
        self.var_low = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Low', variable=self.var_low).grid(row=3, column=col, sticky=W)
        self.var_confident = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Confident', variable=self.var_confident).grid(row=4, column=col, sticky=W)
        self.var_restless = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Restless', variable=self.var_restless).grid(row=5, column=col, sticky=W)
        self.var_relieved = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Relieved', variable=self.var_relieved).grid(row=6, column=col, sticky=W)
        self.var_scared = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Scared', variable=self.var_scared).grid(row=7, column=col, sticky=W)

        col=6
        self.var_trapped = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Trapped', variable=self.var_trapped).grid(row=0, column=col, sticky=W)
        self.var_alive = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Alive', variable=self.var_alive).grid(row=1, column=col, sticky=W)
        self.var_guilty = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Guilty', variable=self.var_guilty).grid(row=2, column=col, sticky=W)
        self.var_bitter = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Bitter', variable=self.var_bitter).grid(row=3, column=col, sticky=W)
        self.var_shocked = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Shocked', variable=self.var_shocked).grid(row=4, column=col, sticky=W)
        self.var_sad = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Sad', variable=self.var_sad).grid(row=5, column=col, sticky=W)
        self.var_energetic = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Energetic', variable=self.var_energetic).grid(row=6, column=col, sticky=W)
        self.var_overwhelmed = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Overwhelmed', variable=self.var_overwhelmed).grid(row=7, column=col, sticky=W)

        col=7
        self.var_unsure = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Unsure', variable=self.var_unsure).grid(row=0, column=col, sticky=W)
        self.var_crushed = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Crushed', variable=self.var_crushed).grid(row=1, column=col, sticky=W)
        self.var_defeated = IntVar()
        ttk.Checkbutton(self.checkFrame, text='Defeated', variable=self.var_defeated).grid(row=2, column=col, sticky=W)

        self.checksDict = {'var_positive':self.var_positive, 'var_happy':self.var_happy, 'var_glad':self.var_glad, 'var_worried':self.var_worried, 'var_insecure':self.var_insecure, 'var_confused':self.var_confused, 'var_proud':self.var_proud, 'var_safe':self.var_safe, 'var_hopeful':self.var_hopeful, 'var_stressed':self.var_stressed, 'var_bored':self.var_bored, 'var_tired':self.var_tired, 'var_hurt':self.var_hurt, 'var_eager':self.var_eager, 'var_angry':self.var_angry, 'var_excited':self.var_excited, 'var_nervous':self.var_nervous, 'var_tense':self.var_tense, 'var_irritated':self.var_irritated, 'var_disappointed':self.var_disappointed, 'var_content':self.var_content, 'var_negative':self.var_negative, 'var_annoyed':self.var_annoyed, 'var_inspired':self.var_inspired, 'var_anxious':self.var_anxious, 'var_determined':self.var_determined, 'var_grateful':self.var_grateful, 'var_unhappy':self.var_unhappy, 'var_frustrated':self.var_frustrated, 'var_furious':self.var_furious, 'var_calm':self.var_calm, 'var_strong':self.var_strong, 'var_neutral':self.var_neutral, 'var_regretful':self.var_regretful, 'var_lonely':self.var_lonely, 'var_low':self.var_low, 'var_confident':self.var_confident, 'var_restless':self.var_restless, 'var_relieved':self.var_relieved, 'var_scared':self.var_scared, 'var_trapped':self.var_trapped, 'var_alive':self.var_alive, 'var_guilty':self.var_guilty, 'var_bitter':self.var_bitter, 'var_shocked':self.var_shocked, 'var_sad':self.var_sad, 'var_energetic':self.var_energetic, 'var_overwhelmed':self.var_overwhelmed, 'var_unsure':self.var_unsure, 'var_crushed':self.var_crushed, 'var_defeated':self.var_defeated}

        # Here starts the main frame
        Label(self.mainFrame, text='Main Task:').grid(row=0, column=0, sticky=NE)
        self.main_txt = Text(self.mainFrame, height=2, width=120, wrap=WORD)
        self.main_txt.bind("<Tab>", focus_next_window)
        self.main_txt.grid(row=0, column=1, sticky=W)

        Label(self.mainFrame, text='Previous Main:').grid(row=1, column=0, sticky=NE)
        self.prev_main = Label(self.mainFrame, text='', wraplength=800, justify=LEFT)
        self.prev_main.grid(row=1, column=1, sticky=W)

        Label(self.mainFrame, text='Review of Previous:').grid(row=2, column=0, sticky=NE)
        self.review_txt = Text(self.mainFrame, height=2, width=120, wrap=WORD)
        self.review_txt.bind("<Tab>", focus_next_window)
        self.review_txt.grid(row=2, column=1, sticky=W)

        Label(self.mainFrame, text='Worked Well and Why:').grid(row=3, column=0, sticky=NE)
        self.well_txt = Text(self.mainFrame, height=3, width=120, wrap=WORD)
        self.well_txt.bind("<Tab>", focus_next_window)
        self.well_txt.grid(row=3, column=1, sticky=W)

        Label(self.mainFrame, text='Not Well and Why:').grid(row=4, column=0, sticky=NE)
        self.unwell_txt = Text(self.mainFrame, height=2, width=120, wrap=WORD)
        self.unwell_txt.bind("<Tab>", focus_next_window)
        self.unwell_txt.grid(row=4, column=1, sticky=W)

        Label(self.mainFrame, text='Other Comments:').grid(row=5, column=0, sticky=NE)
        self.other_txt = Text(self.mainFrame, height=15, width=120, wrap=WORD)
        self.other_txt.bind("<Tab>", focus_next_window)
        self.other_txt.grid(row=5, column=1, sticky=W)

        ttk.Button(self.mainFrame, text='Random Prompt:', command=self.randomPrompt).grid(row=6, column=0, sticky=NE)
        self.prompt_txt = Text(self.mainFrame, height=15, width=120, wrap=WORD)
        self.prompt_txt.bind("<Tab>", focus_next_window)
        self.prompt_txt.grid(row=6, column=1, sticky=W)

        # Run the redraw function to pull in existing data if there is any
        self.redraw()

    def onSave(self):
        today = str(self.dt) # Get date string for current filename
        # Set up dictionary of all data
        save_dict = {}
        # Bring in check boxes
        for check in self.checksDict:
            if self.checksDict[check].get():
                save_dict[check] = 1
        # Bring in text boxes
        save_dict['main_txt'] = self.main_txt.get("1.0",'end-1c')
        save_dict['prevrev_txt'] = self.review_txt.get("1.0",'end-1c')
        save_dict['well_txt'] = self.well_txt.get("1.0",'end-1c')
        save_dict['unwell_txt'] = self.unwell_txt.get("1.0",'end-1c')
        save_dict['other_txt'] = self.other_txt.get("1.0",'end-1c')
        save_dict['prompt_txt'] = self.prompt_txt.get("1.0",'end-1c')
        # Write dictionary
        f = open(today + '.jrn', 'w')
        f.write(str(save_dict))
        f.close()

    def randomPrompt(self):
        self.prompt_txt.delete('1.0', END)
        prompt_list = ['What does your dream life look like?', 'What does your ideal day look like?', 'Where do you see yourself in 6 months, 1 year, 5 years, 10 years?', "What do you know today that you didn't know a year ago?", "In this moment, what are four things you're thankful for?", "What limiting beliefs are holding you back from your dream life?", "What distractions are hindering your productivity?", "What actions can you take today to simplify your life?", "When do you feel most in tune with yourself?", "If you could talk to anyone dead or alive, who would it be and why?", "List your top 10 goals to complete by the end of the year.", "Who do you look up to the most and why?", "If someone else described you, what do you think they'd say and why?", "What does happiness mean to you?", "How have you changed in the last 5 years?", "If today was your last day, what would you do?", "If you could give advice to your younger self, what would you say?", "How do you spend your Sundays?", "What do you need more of in your life?", "If you could have any three things in the world, what would they be?", "Describe in detail what 5 years from now looks like?", "What are 10 things you love about yourself and why?"]
        prompt_list += ["What activities set your soul on fire?", "How can you feel more fulfilled in your life?", "If you couldn't fail, what would you do?", "If you could go anywhere in the world, where would it be and why?", "What's your dream job?", "What are some places you've enjoyed visiting?", "What is a hobby you would like to pursue?", "When did you last read a book and why?", "What's a secret habit or thing you enjoy?", "Write a food or movie review.", "Plan, in detail, how to build something.", "Where would you like to go on a road trip?", "What do you love about your local area?", "When have you been couragious?", "What is your favorite memory?", "From beginning to end, how would you spend your last day?", "How did the universe come into being?", "Do humans decide to be good?", "If you could change one thing in your life...", "Do you believe in ghosts?", "How do you define art?", "Are you a pacifist?", "Was math created or discovered?", "Is morality relative?", "Is time-travel possible?", "Are you an optimist or a pessimist?", "Are you an extrovert or introvert and why?", "Would you ever consider minimalism?", "If someone wrote a biography about you, what would the 'blurb' be?", "What things make you angry?", "Are you good or bad at forgiveness?", "If 10-year-old you saw you, what would he think?", "If you went to a bar as someone else, who would you be?", "What really inspires you to create?", "What's the biggest problem you're facing now?", "Where is your mental 'Happy Place'?", "If you had too much money, how would you spend your time?", "What was the best day of your life so far?", "How does music influence you?", "When do you feel most like 'you'?", "Are you superstitious?", "What is your personal motto?", "What would be your theme song?"]
        prompt_list += ["Define manliness.", "Find one positive habit you would like to implement and plan it.", "Pick a bad habit that you would like to eliminate and plan it.", "Write a memoir of your life so far.", "Reflect on your journal from the last week.", "Reflect on your journal from the last month.", "Where are you in a hero's journey?", "Try stream of consciousness writing.", "Come up with your own 'Cabinet of invisible couneslors'.", "Memento Mori, remember that you are mortal. Does death scare you?"]
        prompt = random.choice(prompt_list)
        self.prompt_txt.insert('1.0', prompt)


    def clearChecks(self):
        for check in self.checksDict:
            self.checksDict[check].set(0)

    def redraw(self):
        self.clearChecks()
        self.main_txt.delete('1.0', END)
        self.review_txt.delete('1.0', END)
        self.well_txt.delete('1.0', END)
        self.unwell_txt.delete('1.0', END)
        self.other_txt.delete('1.0', END)
        self.prompt_txt.delete('1.0', END)
        self.dt_label.configure(text=str(self.dt))
        self.prev_main.config(text=self.getPrevMain())
        # Load current data from appropriate file
        files = os.listdir()
        td = str(self.dt) + '.jrn'
        if td in files:
            f = open(td, 'r')
            td_dict = eval(f.readline())
            f.close()
            # Pull in checks
            for key in td_dict:
                if key in self.checksDict:
                    self.checksDict[key].set(1)
            # Pull in texts
            if 'main_txt' in td_dict:
                self.main_txt.insert('1.0', td_dict['main_txt'])

            if 'prevrev_txt' in td_dict:
                self.review_txt.insert('1.0', td_dict['prevrev_txt'])

            if 'well_txt' in td_dict:
                self.well_txt.insert('1.0', td_dict['well_txt'])

            if 'unwell_txt' in td_dict:
                self.unwell_txt.insert('1.0', td_dict['unwell_txt'])

            if 'other_txt' in td_dict:
                self.other_txt.insert('1.0', td_dict['other_txt'])

            if 'prompt_txt' in td_dict:
                self.prompt_txt.insert('1.0', td_dict['prompt_txt'])


    def dayBack(self):
        self.onSave()
        self.dt -= timedelta(days=1)
        self.redraw()

    def weekBack(self):
        self.onSave()
        self.dt -= timedelta(days=7)
        self.redraw()

    def dayFore(self):
        self.onSave()
        self.dt += timedelta(days=1)
        self.redraw()

    def weekFore(self):
        self.onSave()
        self.dt += timedelta(days=7)
        self.redraw()

    def getPrevMain(self):
        files = os.listdir() # Pull list of files in current folder.
        ys = str(self.dt - timedelta(days=1)) + '.jrn' # Get string of yesterday's date for filename.
        if ys in files: # If yesterday's file exists
            # Read the contents of ys in as a dictionary
            f = open(ys, 'r')
            prev_dict = eval(f.readline())
            f.close()
            if 'main_txt' in prev_dict:
                main_txt = prev_dict['main_txt'] # Extract the Main Task as main_tsk
            else:
                main_txt = ''
            return(main_txt)
        else:
            return('')
    
def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")

root = Tk()
app = Journal(root)
root.wm_title("Journal")
root.mainloop()

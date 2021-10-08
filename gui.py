#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'

import tkinter as tk
import main as expert


class Application(tk.Frame):

    def __init__(self, master=None):
        master = tk.Tk()
        super().__init__(master)
        master.minsize(width=240, height=180)
        # self.pack()
        self.create_widgets(master)
        self.grid_widgets()
        self.grid()

    def create_widgets(self, master):
        self.labelInput = tk.Label(self, text='Road conditions')
        self.safety = tk.BooleanVar()
        self.lanes = tk.StringVar()
        self.lane = tk.StringVar()
        self.visibility = tk.StringVar()
        self.checkbuttonSafeDistance = tk.Checkbutton(
            self, text='100 meters from the vehicle ahead', variable=self.safety)
        self.radiobuttonNoneLanes = tk.Radiobutton(
            self, text='Unknown number of lanes', variable=self.lanes)
        self.radiobuttonTwoLanes = tk.Radiobutton(
            self, text='Two lanes in the same direction', variable=self.lanes, value='Two lanes')
        self.radiobuttonThreeLanes = tk.Radiobutton(
            self, text='Three lanes in the same direction', variable=self.lanes, value='Three lanes')
        self.radiobuttonNoneLane = tk.Radiobutton(
            self, text='Unknown lane', variable=self.lane)
        self.radiobuttonLeftLane = tk.Radiobutton(
            self, text='Left lane', variable=self.lane, value='Left lane')
        self.radiobuttonMiddleLane = tk.Radiobutton(
            self, text='Center Lane', variable=self.lane, value='Middle lane')
        self.radiobuttonRightLane = tk.Radiobutton(
            self, text='Right Lane', variable=self.lane, value='Right lane')
        self.labelVisibility = tk.Label(self, text='Visibility is lower than:')
        self.radiobuttonNoneVisibility = tk.Radiobutton(
            self, text='without', variable=self.visibility)
        self.radiobutton50Visibility = tk.Radiobutton(
            self, text='50m', variable=self.visibility, value='Visibility 50 meters')
        self.radiobutton100Visibility = tk.Radiobutton(
            self, text='100m', variable=self.visibility, value='Visibility 100 meters')
        self.radiobutton200Visibility = tk.Radiobutton(
            self, text='200m', variable=self.visibility, value='Visibility 200 meters')
        self.buttonRun = tk.Button(self, text='To monitor...', command=self.run)
        self.labelOutput = tk.Label(self, text='Monitoring conclusion', justify='left')
        self.labelMax = tk.Label(
            self, text='Top speed: ', anchor='w')
        self.labelMin = tk.Label(
            self, text='Minimum speed: ', anchor='w')
        self.labelAdvice = tk.Label(self, anchor='w')

    def grid_widgets(self):
        self.labelInput.grid(column=0, row=0)
        self.checkbuttonSafeDistance.grid(column=0, row=1)
        self.radiobuttonNoneLanes.grid(column=0, row=2)
        self.radiobuttonTwoLanes.grid(column=1, row=2)
        self.radiobuttonThreeLanes.grid(column=2, row=2)
        self.radiobuttonNoneLane.grid(column=0, row=3)
        self.radiobuttonLeftLane.grid(column=1, row=3)
        self.radiobuttonMiddleLane.grid(column=2, row=3)
        self.radiobuttonRightLane.grid(column=3, row=3)
        self.labelVisibility.grid(column=0, row=4)
        self.radiobuttonNoneVisibility.grid(column=1, row=4)
        self.radiobutton200Visibility.grid(column=2, row=4)
        self.radiobutton100Visibility.grid(column=3, row=4)
        self.radiobutton50Visibility.grid(column=4, row=4)
        self.buttonRun.grid(column=0, row=5, pady=4)
        self.labelOutput.grid(column=0, row=6)
        self.labelMax.grid(column=0, row=7, columnspan=4)
        self.labelMin.grid(column=0, row=8, columnspan=4)
        self.labelAdvice.grid(column=0, row=9, columnspan=4)

    def get_facts(self):
        facts = ['Freeway']
        if self.safety.get():
            facts.append('Safety distance 100 meters')
        if self.lanes.get():
            facts.append(self.lanes.get())
        if self.lane.get():
            facts.append(self.lane.get())
        if self.visibility.get():
            facts.append(self.visibility.get())
        return facts

    def run(self):
        facts = self.get_facts()
        rules = expert.import_rules()
        Max, Min, Advice = expert.test_one_case(rules, facts)
        self.labelMax['text'] = 'Top speed: ' + str(Max) + 'km/h'
        self.labelMin['text'] = 'Minimum speed: ' + str(Min) + 'km/h'
        print(self.labelMax['text'])
        print(self.labelMin['text'])
        self.labelAdvice['text'] = ''
        if len(Advice) > 0:
            t = ''
            if 'Open lights' in Advice:
                t += 'Turn on various warning lights '
            if 'Leave ASAP' in Advice:
                t += 'Leave the highway as soon as possible at the nearest exit'
            self.labelAdvice['text'] = 'Driving advice: ' + t
            print(self.labelAdvice['text'])
        print()

if __name__ == '__main__':
    app = Application()
    app.master.title('Highway speed monitoring expert system')
    app.mainloop()

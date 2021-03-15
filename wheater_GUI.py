from tkinter import *
import wheater

class App:
    def __init__(self, parent):
        self.mainFrame = Frame(master = parent)
        self.mainFrame.after(1000 * 300, self.refresh)
        self.mainFrame.pack()

        self.cityString = StringVar()
        self.cityInput = Entry(master = self.mainFrame, textvariable = self.cityString)
        self.cityInput.bind("<Return>", self.connectCity)
        self.cityInput.pack(pady = 10)
        self.cities = wheater.loadCities()
        self.renderCities()

    def renderCities(self):
        self.cities = wheater.loadCities()
        if self.cities is not None:
            for key in self.cities.keys():
                city = self.cities[key]
                self.frame = Frame(master = self.mainFrame)

                temp = f'The Temperature is {city["temp"]}°C currently.'
                wind = f'Wind speed is {city["wind"]} km/h'
                humidity = f'Humidity is {city["humidity"]}%'

                Label(master= self.frame, text = key, font = "Consolas", padx=10).pack(side = "left")
                Label(master = self.frame, text = f'{temp}\n{wind}\n{humidity}', font = ("Consolas"), padx=10, pady=10).pack(side = "right")
                self.frame.pack()

                
    def connectCity(self, event):
        wheater.addCity(self.cityString.get())
        self.refresh()

    def disconnectCity(self, event):
        wheater.removeCity()

    def refresh(self):
        self.mainFrame.destroy()
        self.__init__(root)

root = Tk()
root.title("Wheater App")
app = App(root)
root.mainloop()
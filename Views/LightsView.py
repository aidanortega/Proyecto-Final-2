from tkinter import Tk, N, S, E, W, Label
from Views.ToggleLightsButton import ToggleLightsButton
class LightsView(Tk):
    class Constants:
        title = "Control de Luces"
        heigth = 300
        width = 300
        center = N + S + E + W

        @classmethod
        def size(cls):
            return "{}x{}".format(cls.width, cls.heigth)

    def __init__(self, toogle_handler = None, tap_handler = None):
        super().__init__()
        self.__toogle_handler = toogle_handler
        self.title(self.Constants.title)
        self.geometry(self.Constants.size())

        self.__configure_grid()

        self.__bedroom_one_label = Label(self, text="Room\nOne", relief="sunken")
        self.__bedroom_one_label.grid(row=0, column=0, sticky=self.Constants.center)
        self.__bedroom_one_toogle = ToggleLightsButton(self, "Bedroom One", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__bedroom_one_toogle.grid(row=1, column=0, sticky=self.Constants.center)

        self.__bedroom_two_label = Label(self, text="Room\nTwo", relief="sunken")
        self.__bedroom_two_label.grid(row=0, column=1, sticky=self.Constants.center)
        self.__bedroom_two_toogle = ToggleLightsButton(self, "Bedroom Two", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__bedroom_two_toogle.grid(row=1, column=1, sticky=self.Constants.center)

        self.__living_label = Label(self, text="Living\nroom", relief="sunken")
        self.__living_label.grid(row=0, column=2, sticky=self.Constants.center)
        self.__living_toogle = ToggleLightsButton(self, "Living room", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__living_toogle.grid(row=1, column=2, sticky=self.Constants.center)

        self.__dining_label = Label(self, text="Dining\nroom", relief="sunken")
        self.__dining_label.grid(row=0, column=3, sticky=self.Constants.center)
        self.__dining_toogle = ToggleLightsButton(self, "Dining room", action=self.__did_tap, tap_toggle_handler=tap_handler)
        self.__dining_toogle.grid(row=1, column=3, sticky=self.Constants.center)


    def __configure_grid(self):
        self.grid_rowconfigure(0, weight=self.Constants.heigth//2)
        self.grid_rowconfigure(1, weight=self.Constants.heigth//2)
        for column_index in range(4):
            self.grid_columnconfigure(column_index, weight=self.Constants.width//4)

    def __did_tap(self, sender):
        if self.__toogle_handler is None: return
        if sender == "Bedroom One": id = 1
        elif sender == "Bedroom Two": id = 2
        elif sender == "Living room": id = 3
        elif sender == "Dining room": id = 4
        self.__toogle_handler(id)
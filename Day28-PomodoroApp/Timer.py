from tkinter import Canvas, Tk


class Timer:
    def __init__(self, canvas, text_id, window):
        self.__minute = 0
        self.__second = 0
        self.__running = False
        self.__check_mark = 0
        self.canvas = canvas
        self.text_id = text_id
        self.window = window

    @property
    def check_mark(self):
        return self.__check_mark

    def update_timer(self):
        if self.__running:
            self.__second += 1

            if self.__second == 60:
                self.__second = 0
                self.__minute += 1

            # print(f'{self.__minute}:{self.__second}')

            # update the text on canvas
            self.canvas.itemconfig(self.text_id, text=f'{self.__minute:02}:{self.__second:02}')

            if self.__minute == 0 and self.__second == 3:
                self.__check_mark += 1
                return

            # update after every 1000ms (1 second)
            self.window.after(1000, self.update_timer)

    def start(self, canvas, text_id, window):
        if not self.__running:
            self.__running = True
            self.update_timer()

    def reset(self, canvas, text_id, window):
        self.__running = False
        self.__minute = 0
        self.__second = 0
        canvas.itemconfig(text_id, text='00:00')

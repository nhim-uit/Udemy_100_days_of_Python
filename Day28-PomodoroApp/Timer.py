from CONSTANTS import *


class Timer:
    def __init__(self, canvas, text_id, window):
        self.__minute = 0
        self.__second = 0
        self.__running = False
        self.__check_mark = 0
        self.__reps = 0
        self.canvas = canvas
        self.text_id = text_id
        self.window = window

    def update_timer(self, check_mark_lb, title_lb):
        if self.__running:
            self.__second += 1

            if self.__second == SECOND_PER_MINUTE:
                self.__second = 0
                self.__minute += 1

            # update the text on canvas
            self.canvas.itemconfig(self.text_id, text=f'{self.__minute:02}:{self.__second:02}')

            if self.__reps % 2 == 0:
                self.pomodoro(title_lb)

                # config label
                check_mark_lb.config(text=self.__check_mark * '✔')

            else:
                self.break_time(title_lb)

            # update after every 1000ms (1 second)
            self.window.after(1000, self.update_timer, check_mark_lb, title_lb)

    def start(self, check_mark_lb, title_lb):
        if not self.__running:
            self.__running = True
            self.update_timer(check_mark_lb, title_lb)

    def reset(self, canvas, text_id):
        self.__running = False
        self.__minute = 0
        self.__second = 0
        canvas.itemconfig(text_id, text='00:00')

    def pomodoro(self, title_lb):
        title_lb.config(text='Work', fg=GREEN)

        if self.__minute == WORK_MIN and self.__second == 0:
            self.__check_mark += 1

            self.__minute = 0
            self.__second = 0
            self.__reps += 1

    def break_time(self, title_lb):
        title_lb.config(text='Break', fg=PINK)
        if self.__reps % LONG_BREAK_REPS == 0:
            title_lb.config(fg=BLUE)
            if self.__minute == LONG_BREAK_MIN and self.__second == 0:
                self.reset_minute_second()

        elif self.__minute == SHORT_BREAK_MIN and self.__second == 0:
            self.reset_minute_second()

    def reset_minute_second(self):
        self.__minute = 0
        self.__second = 0
        self.__reps += 1


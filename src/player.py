import pygame

class Player():
    def __init__(self):
        self.correct_chars = set()
        self.wrong_chars = set()
        self.ready = False
        self.finished = False

    def set_ready(self, isReady):
        self.ready = isReady

    def get_ready(self):
        return self.ready

    def get_finished(self):
        return self.finished
    
    def set_finished(self, finished):
        self.guesses = finished
    
    def add_correct(self, char):
        self.correct_chars.add(char)

    def get_correct(self):
        return len(self.correct_chars)

    def get_wrong(self):
        return len(self.wrong_chars)

    def __str__(self):
        return f"Ready: {self.get_ready()} | Finished: {self.get_finished()} | Correct: {self.get_correct()} | Wrong: {self.get_wrong()}"
    
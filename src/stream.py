from abc import ABC, abstractmethod
from pynput.keyboard import Controller

class Stream(ABC):
    @abstractmethod
    def output(self):
        pass
    @abstractmethod
    def close(self):
        pass

class PlainStream(Stream):
    def __init__(self):
        pass

    def output(self, input_str):
        print(input_str, end="", flush=True)
        return
    
    def close(self):
        print("\n")
        return

class KeyboardStream:
    def __init__(self):
        self.keyboard = Controller()

    def output(self, input_str):
        self.keyboard.type(input_str)
        return
    
    def close(self):
        return
    
class MarkfownStream:
    GREEN = '\033[32m'
    NORMAL = '\033[0m'

    def __init__(self):
        self.color_mode = False
        self.back_quotes = []
        self.last_char = None

    def output(self, input_str):
        for char in input_str:
            # Check for back quotes
            if char == '`':
                if self.color_mode==False:
                    self.back_quotes.append(char)
                else:
                    if len(self.back_quotes)>0:
                        self.back_quotes.pop()
            else:
                if char == '\n' and self.last_char == '`' and not self.color_mode:
                    continue
                if len(self.back_quotes):
                    self.color_mode = True
                    print(self.GREEN+char, end="", flush=True)
                else:
                    self.color_mode = False
                    print(self.NORMAL+char, end="", flush=True)
            self.last_char = char
        return

    def close(self):
        print(self.NORMAL+"\n")
        return

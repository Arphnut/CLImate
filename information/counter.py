from .message import Message
from styler import Styler

# In order to solve issue #3

s = Styler()


class Counter(Message):
    """
    A counter component, displaying the number of iteration done so far.
    If the final number of iterations is already known in advance, the 'ProgressBar' class should be used.

    Parameters:
    -----------
    text (str): A string displaying the text to display to explain the use of the counter.
    stop_condition (boolean):  It's value is 'False' as long as the task is not finished,
                               and 'True' once it is over.
    count (str): The initial value of the counter.
    """

    def __init__(self, text, stop_condition=False, count=0):
        self.text = text
        self.stop_condition = stop_condition
        self.count = count
        Message.__init__(self, Message.tags.progress,
                         text + " {}".format(self.count), "\r")

        self.display()

    def display(self):
        """ Display the Counter"""
        self.info = self.text + " {}".format(self.count)
        Message.display(self)

    def increment(self, stop=False, step=1):
        """ Increment the number of the count by 'step'"""
        if stop:
            self.stop_condition = True
        self.count += 1
        if self.stop_condition:
            self.end = "\n"
        self.display()

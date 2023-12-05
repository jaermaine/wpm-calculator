class Calculate:

    def __init__(self, initial_time, resting_time, word_count):
        self.initial = initial_time
        self.rest = resting_time
        self.count = word_count
        self.attempt = (resting_time - initial_time) / 60

    def get_wpm(self):
        return str(round(self.count / self.attempt, 2))

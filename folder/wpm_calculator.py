class Calculate:

    def __init__(self, initial_time, resting_time, word_count):
        self.initial = initial_time
        self.rest = resting_time
        self.count = word_count
        self.attempt = round(resting_time - initial_time)

    def get_wpm(self):
        return round((self.count / 4.7) * 60 / self.attempt)

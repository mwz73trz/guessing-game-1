class GuessingGame():
    last_guess = None
    last_result = None

    #number to be guessed
    def __init__(self, answer):
        self.answer = answer
    #Users guess. return low, high, or correct
    def guess(self, user_guess):
        self.user_guess = user_guess
        if self.user_guess < self.answer:
            self.last_guess = self.user_guess
            return "low"
        elif self.user_guess > self.answer:
            self.last_guess = self.user_guess
            return "high"
        else:
            self.last_guess = self.user_guess
            return "correct"
    #if the last guess was correct return true else false
    def solved(self):
        if self.last_guess == self.answer:
            return True
        else:
            return False


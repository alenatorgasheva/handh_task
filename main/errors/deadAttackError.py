class DeadAttackError(Exception):
    def __init__(self, text):
        self.txt = text

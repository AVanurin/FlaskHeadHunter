
class Profile:
    def __init__(self, i, f, l, a, s, j):
        self.id = i
        self.fname = f
        self.lname = l
        self.age = a
        self.sex = s
        self.job = j

    def __str__ (self):
        return f"Резюме пользователя {self.fname, self.lname}"
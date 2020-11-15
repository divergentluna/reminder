import datetime


class Task(object):
    def __init__(self, description, link, picture_path, date, time, priority):
        self.description = description
        self.link = link
        self.picture_path = picture_path
        self.date = date
        self.time = time
        self.priority = priority

    def __del__(self):
        pass

    def edit(self):
        pass

    def snooze(self):
        pass

    def dismiss(self):
        pass


class SubTask(Task):
    def __init__(self):
        super.__init__()


class Group(object):
    pass
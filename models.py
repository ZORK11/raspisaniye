from datetime import datetime

class Lesson():
    lesson_id: int
    lesson_start: datetime
    lesson_end: datetime

    def __init__(self, lesson_id, lesson_start, lesson_end):
        self.lesson_id = lesson_id
        self.lesson_start = lesson_start
        self.lesson_end = lesson_end

class Conflict():
    room_id: int
    first: Lesson
    second: Lesson
    def __init__(self, room_id, first, second):
        self.room_id = room_id
        self.first = first
        self.second = second
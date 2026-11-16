from datetime import datetime, timedelta


class Lesson:
    lesson_id: int
    lesson_start: datetime
    lesson_end: datetime

    def __init__(self, lesson_id: int, lesson_start: datetime, lesson_end: datetime):
        self.lesson_id = lesson_id
        self.lesson_start = lesson_start
        self.lesson_end = lesson_end

class Conflict:
    room_id: int
    first: Lesson
    second: Lesson
    overlap_time: timedelta

    def __init__(self, room_id: int, first: Lesson, second: Lesson, overlap_time: timedelta):
        self.room_id = room_id
        self.first = first
        self.second = second
        self.overlap_time = overlap_time

class Room:
    room_id: int
    capacity: int
    def __init__(self, room_id, capacity: int):
        self.capacity = capacity
        self.room_id = room_id

class Teacher:
    teacher_id: int
    fio: str
    def __init__(self, teacher_id: int, fio: str):
        self.teacher_id = teacher_id
        self.fio = fio

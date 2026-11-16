import csv
from collections import defaultdict
from datetime import datetime
from models import Lesson, Conflict

def parse_room_csv(filename: str):
    rooms = defaultdict(list)
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            start_time = datetime.strptime(f"{row['date']} {row['start_time']}", '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strptime(f"{row['date']} {row['end_time']}", '%Y-%m-%d %H:%M:%S')
            if start_time >= end_time:
                continue
            lesson = Lesson(lesson_id=int(row['lesson_id']), lesson_start=start_time, lesson_end=end_time)
            rooms[row['room_id']].append(lesson)
    return dict(rooms)

def sort_rooms(rooms: dict):
    for room in rooms:
        rooms[room] = sorted(rooms[room], key=lambda lesson: lesson.lesson_start)
    return rooms



def find_room_conflict(rooms: dict):
    conflicts = []
    sorted_rooms = sort_rooms(rooms)
    for room in sorted_rooms:
        for i in range(len(sorted_rooms[room])-1):
            if sorted_rooms[room][i].lesson_end>sorted_rooms[room][i+1].lesson_start:
                conflict = Conflict(room_id=room,
                                    first = sorted_rooms[room][i],
                                    second=sorted_rooms[room][i+1],
                                    overlap_time=sorted_rooms[room][i].lesson_end-sorted_rooms[room][i+1].lesson_start)
                conflicts.append(conflict)
    return conflicts
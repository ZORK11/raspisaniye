import csv
from collections import defaultdict
from datetime import datetime

def parse_room_csv(filename: str):
    rooms = defaultdict(list)
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lesson_data = {
                'lesson_id': int(row['lesson_id']),
                'start_datetime': datetime.strptime(f"{row['date']} {row['start_time']}", '%Y-%m-%d %H:%M:%S'),
                'end_datetime': datetime.strptime(f"{row['date']} {row['end_time']}", '%Y-%m-%d %H:%M:%S'),
            }
            rooms[row['room_id']].append(lesson_data)
    return dict(rooms)

def sort_rooms(rooms: dict):
    for room in rooms:
        rooms[room] = sorted(rooms[room], key=lambda lesson: lesson['start_datetime'])
    return rooms

def find_room_conflict(rooms: dict):
    conflicts = []
    sorted_rooms = sort_rooms(rooms)
    for room in sorted_rooms:
        for i in range(len(sorted_rooms[room])-1):
            if sorted_rooms[room][i]['end_datetime']>sorted_rooms[room][i+1]['start_datetime']:
                conflicts.append({'room_id': room,
                            'first_lesson_id': sorted_rooms[room][i]['lesson_id'],
                            'first_lesson_start': sorted_rooms[room][i]['start_datetime'],
                            'first_lesson_end': sorted_rooms[room][i]['end_datetime'],
                            'second_lesson_id': sorted_rooms[room][i+1]['lesson_id'],
                            'second_lesson_start': sorted_rooms[room][i+1]['start_datetime'],
                            'second_lesson_end': sorted_rooms[room][i+1]['end_datetime']})
    return conflicts


import csv
from collections import defaultdict
from datetime import datetime
from models import Lesson, Conflict

def parse_csv(filename: str, group_by):
    grouped = defaultdict(list)
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            start = datetime.strptime(f"{row['date']} {row['start_time']}", '%Y-%m-%d %H:%M:%S')
            end = datetime.strptime(f"{row['date']} {row['end_time']}", '%Y-%m-%d %H:%M:%S')
            if start >= end:
                continue
            lesson = Lesson(lesson_id=int(row['lesson_id']), lesson_start=start, lesson_end=end, teacher_id=int(row['teacher_id']))
            grouped[row[group_by]].append(lesson)
    return dict(grouped)


def sort_by_start(grouped: dict):
    for _id in grouped:
        grouped[_id] = sorted(grouped[_id], key=lambda lesson: lesson.lesson_start)
    return grouped

def find_room_conflict(grouped_data: dict):
    conflicts = []
    sorted_data = sort_by_start(grouped_data)
    for _id in sorted_data:
        for i in range(len(sorted_data[_id])-1):
            if sorted_data[_id][i].lesson_end>sorted_data[_id][i+1].lesson_start:
                conflict = Conflict(room_id=_id,
                                    first = sorted_data[_id][i],
                                    second=sorted_data[_id][i+1],
                                    overlap_time=sorted_data[_id][i].lesson_end-sorted_data[_id][i+1].lesson_start)
                conflicts.append(conflict)
    return conflicts


import json
import re
from collections import defaultdict
import math
from School import School
from Student import Student


def main():
    schools, students = read_json("input.json")
    students.sort(key=lambda x: x.id)
    res = []

    for school in schools:
        if not students:
            break
        students.sort(key=lambda x: allocate_students_based_on_weightage(school, x))
        curr = defaultdict(list)
        for _ in range(school.maxAllocation):
            curr[school.name].append(students.pop().id)
        res.append(curr)

        with open("output.json", "w") as fp:
            json_string = json.dumps(res, indent=2, separators=(",", ": "))
            json_string = json_string.replace("\n      ", "").replace("\n    ]", "]")

            fp.write(json_string)


def allocate_students_based_on_weightage(school, student):
    distance_score = normalise_school_distance(
        compute_school_distance(
            school_coords=school.location, student_coords=student.homeLocation
        )
    )
    alumni_score = 1 if is_alumni(school=school, student=student) else 0
    volunteer_score = 1 if is_volunteer(school=school, student=student) else 0

    overall_score = 0.5 * distance_score + 0.3 * alumni_score + 0.2 * volunteer_score

    return overall_score


def read_json(file_path):
    """
    Reads a JSON file and returns the data.

    :param file_path: str - Path to the input JSON file.
    :return: dict - Parsed JSON data.
    """
    with open(file_path, "r") as f:
        data = json.load(f)
        all_schools = []
        all_students = []
        school_data = data["schools"]
        student_data = data["students"]
        for school in school_data:
            all_schools.append(School(**school))
        for student in student_data:
            all_students.append(Student(**student))

    return all_schools, all_students


def process_data(data):
    """
    Processes the data read from the JSON file.

    :param data: dict - JSON data to process.
    :return: None
    """
    print(data)


def compute_school_distance(school_coords, student_coords):
    return math.sqrt(
        math.pow(school_coords[0] - student_coords[0], 2)
        + math.pow(school_coords[1] - student_coords[1], 2)
    )


def normalise_school_distance(distance):
    return 1 / (distance + 1)


def is_alumni(student, school):
    return student.alumni and school.name == student.alumni


def is_volunteer(student, school):
    return student.volunteer and school.name == student.volunteer


if __name__ == "__main__":
    main()

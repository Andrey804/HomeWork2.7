import random
import faker
from datetime import datetime
from random import randint
from database.db import session
from database.models import Group, Teacher, Subject, Student, Score


NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 3
NUMBER_SCORES = 20


def generate_fake_data(number_groups, number_subjects, number_students, number_teachers, number_scores) -> tuple:
    subjects = ['Алгебра', 'Геометрія', 'Фізика', 'Англійська мова', 'Українська мова', 'Фізкультура', 'Хімія',
                'Біологія', 'Мова програмування Python', 'Веб-дизайн', 'Мова програмування С++']
    groups = ['AD-101', 'AD-102', 'AD-103', 'AD-104', 'AD-105', 'AD-106', 'AD-107']

    fake_students = []  # тут зберігатимемо імена студентів та вчителів
    fake_teachers = []  # тут зберігатимемо імена студентів та вчителів
    fake_scores = []  # тут зберігатимемо оцінки

    fake_data = faker.Faker('uk_UA')

    # Згенеруємо групи у кількості number_groups
    fake_groups = (random.sample(groups, k=number_groups))

    # Згенеруємо предмети у кількості number_subjects
    fake_subjects = (random.sample(subjects, k=number_subjects))

    # Згенеруємо імена у кількості number_students + number_teachers
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Згенеруємо імена у кількості number_students + number_teachers
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    # Згенеруємо оцінки у кількості number_scores
    for _ in range(number_scores):
        fake_scores.append(fake_data.random_int(1, 12))

    return fake_groups, fake_subjects, fake_students, fake_teachers, fake_scores


def prepare_data(groups, subjects, students, teachers, scores) -> list:
    all_requests = []

    for group in groups:
        all_requests.append(Group(name=group))

    for teacher in teachers:
        all_requests.append(Teacher(name=teacher))

    for subject in subjects:
        all_requests.append(Subject(name=subject, teacher_id=randint(1, NUMBER_TEACHERS)))

    for student in students:
        all_requests.append(Student(name=student, group_id=randint(1, NUMBER_GROUPS)))

    for num_student in range(1, NUMBER_STUDENTS + 1):
        for score in scores:
            submission_date = datetime(2021, datetime.now().month - 1, randint(1, 30)).date()
            all_requests.append(Score(student_id=num_student, subject_id=randint(1, NUMBER_SUBJECTS), score=score,
                                         score_date=submission_date))

    return all_requests


def insert_data_to_db(all_requests) -> None:
    session.add_all(all_requests)
    session.commit()


if __name__ == "__main__":
    insert_data_to_db(prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SCORES)))

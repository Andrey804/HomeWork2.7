from sqlalchemy import select
from database.db import session
from sqlalchemy.sql import func, desc, and_
from database.models import Group, Subject, Student, Score


def select_1():
    # query = session.execute(select(Student.name)
    #                         .join(Score)
    #                         .group_by(Student.id)
    #                         .order_by(func.avg(Score.score))
    #                         .limit(5))
    # for res in query:
    #     print(res.name)

    q = session.query(Student.name, func.round(func.avg(Score.score), 2).label('avg_score')) \
        .select_from(Score).join(Student).group_by(Student.id).order_by(desc('avg_score')).limit(5).all()
    print(q)


def select_2():
    # query = session.execute(select(Student.name, func.round(func.avg(Score.score), 2).label('avg_score'))
    #                         .join(Score)
    #                         .filter(Score.subject_id == 1)
    #                         .group_by(Student.id)
    #                         .order_by(desc('avg_score'))
    #                         .limit(1))
    # for res in query:
    #     print(res.name, res.avg_score)

    q = session.query(Student.name, func.round(func.avg(Score.score), 2).label('avg_score'))\
        .select_from(Score).join(Student)\
        .filter(Score.subject_id == 1)\
        .group_by(Student.id)\
        .order_by(desc('avg_score'))\
        .limit(1).all()
    print(q)


def select_3():
    # query = session.execute(select(Student.group_id, func.round(func.avg(Score.score), 2).label('avg_score'))
    #                         .join(Score)
    #                         .filter(Score.subject_id == 1)
    #                         .group_by(Student.group_id)
    #                         .order_by(Student.group_id))
    # for res in query:
    #     print(res.group_id, res.avg_score)

    q = session.query(Student.group_id, func.round(func.avg(Score.score), 2).label('avg_score'))\
        .select_from(Score).join(Student)\
        .filter(Score.subject_id == 1)\
        .group_by(Student.group_id)\
        .order_by(Student.group_id).all()
    print(q)


def select_4():
    # query = session.execute(select(func.round(func.avg(Score.score), 2).label('avg_score')))
    # for res in query:
    #     print(res.avg_score)

    q = session.query(func.round(func.avg(Score.score), 2).label('avg_score'))\
        .select_from(Score).all()
    print(q)


def select_5():
    # query = session.execute(select(Subject.name).filter(Subject.teacher_id == 1))
    # for res in query:
    #     print(res.name)

    q = session.query(Subject.name)\
        .select_from(Subject)\
        .filter(Subject.teacher_id == 1).all()
    print(q)


def select_6():
    # query = session.execute(select(Student.name)
    #                         .join(Group)
    #                         .filter(Student.group_id == 1))
    # for res in query:
    #     print(res.name)

    q = session.query(Student.name)\
        .select_from(Student).join(Group)\
        .filter(Student.group_id == 1).all()
    print(q)


def select_7():
    # query = session.execute(select(Student.name, Score.score)
    #                         .join(Score)
    #                         .filter(and_(Student.group_id == 1,
    #                                      Score.subject_id == 1))
    #                         .order_by(Student.name, Score.score))
    # for res in query:
    #     print(res.name, res.score)

    q = session.query(Student.name, Score.score)\
        .select_from(Student).join(Score)\
        .filter(and_(Student.group_id == 1,
                     Score.subject_id == 1))\
        .order_by(Student.name, Score.score).all()
    print(q)


def select_8():
    # query = session.execute(select(Subject.name, func.round(func.avg(Score.score), 2).label('avg_score'))
    #                         .join(Score)
    #                         .filter(Subject.teacher_id == 1)
    #                         .group_by(Subject.id))
    # for res in query:
    #     print(res.name, res.avg_score)

    q = session.query(Subject.name, func.round(func.avg(Score.score), 2).label('avg_score'))\
        .select_from(Subject).join(Score)\
        .filter(Subject.teacher_id == 1)\
        .group_by(Subject.id).all()
    print(q)


def select_9():
    # query = session.execute(select(Subject.name)
    #                         .join(Score)
    #                         .filter(Score.student_id == 1)
    #                         .group_by(Subject.id))
    # for res in query:
    #     print(res.name)

    q = session.query(Subject.name)\
        .select_from(Subject).join(Score)\
        .filter(Score.student_id == 1)\
        .group_by(Subject.id).all()
    print(q)


def select_10():
    # query = session.execute(select(Subject.name)
    #                         .join(Score)
    #                         .filter(and_(Score.student_id == 1,
    #                                      Subject.teacher_id == 1))
    #                         .group_by(Subject.id))
    # for res in query:
    #     print(res.name)

    q = session.query(Subject.name)\
        .select_from(Subject).join(Score)\
        .filter(and_(Score.student_id == 1,
                     Subject.teacher_id == 1))\
        .group_by(Subject.id).all()
    print(q)


def select_11():
    # query = session.execute(select(func.round(func.avg(Score.score), 2).label('avg_score'))
    #                         .join(Subject)
    #                         .filter(and_(Score.student_id == 1,
    #                                      Subject.teacher_id == 1)))
    # for res in query:
    #     print(res.avg_score)

    q = session.query(func.round(func.avg(Score.score), 2).label('avg_score'))\
        .select_from(Subject).join(Score)\
        .filter(and_(Score.student_id == 1,
                     Subject.teacher_id == 1)).all()
    print(q)


def select_12():
    # query = session.execute(select(Student.name, Score.score, Score.score_date)
    #                         .join(Score)
    #                         .filter(and_(Student.group_id == 1,
    #                                      Score.subject_id == 1,
    #                                      Score.score_date == (select(func.max(Score.score_date))
    #                                                           .select_from(Student).join(Score)
    #                                                           .filter(and_(Student.group_id == 1,
    #                                                                        Score.subject_id == 1))
    #                                                           .scalar_subquery())
    #                                      ))
    #                         )
    # for res in query:
    #     print(res.score_date, res.name, res.score)

    subq = (select(func.max(Score.score_date))
            .select_from(Student).join(Score)
            .filter(and_(Student.group_id == 1,
                         Score.subject_id == 1))
            .scalar_subquery())
    q = session.query(Score.score_date, Student.name, Score.score)\
        .select_from(Student).join(Score)\
        .filter(and_(Student.group_id == 1,
                     Score.subject_id == 1,
                     Score.score_date == subq)).all()
    print(q)


if __name__ == "__main__":
    select_12()

import pandas as pd


def schedule_with_students(roomslots, activities, courses):
    df_students_count = pd.DataFrame(columns=["Course name", "Student count"])
    for course in list(courses.values()):
        students_tutorial = course.get_students()
        students_practicum = course.get_students()
        # df_students_count = df_students_count.append({
        #     "Course name": course,
        #     "Student count": course.get_num_of_students()},
        #     ignore_index=True)
        for activity in course.get_activities():
            if activity.get_kind() == "Lecture":
                activity.set_students(course.get_students())
            if activity.get_kind() == "Tutorial" and not activity.get_students():
                maximum_students = activity.get_max_stud()
                if len(course.get_students()) <= maximum_students:
                    activity.set_students(course.get_student())
    # schedule students to activities


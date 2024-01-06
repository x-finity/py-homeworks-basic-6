class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # global student_list
        # student_list.append(self)

    def rate_lec(self, mentor, course, grade: int):
        if grade > 0 and grade <= 10:
            if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
                if course in mentor.grades:
                    mentor.grades[course] += [grade]
                else:
                    mentor.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Оценка должна быть от 1 до 10'
    def get_average_grade(self):
        grades_list = []
        for course_grades in self.grades.values():
            grades_list += course_grades
        return round(sum(grades_list) / len(grades_list), 1)
    # def course_avg_grade(self, course):
    #     grade_sum = 0
    #     for student in student_list:
    #         if course in student.courses_in_progress or course in student.finished_courses:
    #             grade_sum += sum(student.grades[course])
    #     print(f'Средняя оценка за домашние задания по курсу {course}: {round(grade_sum / len(student_list), 1)}')
    def course_avg_grade(self, course, *students):
        grade_sum = 0
        grades_count = 0
        for student in students:
            if isinstance(student, Student) and course in student.courses_in_progress or course in student.finished_courses:
                grade_sum += sum(student.grades[course])
                grades_count += len(student.grades[course])
        print(f'Средняя оценка за домашние задания по курсу {course}: {round(grade_sum / grades_count, 1)}')

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def get_average_grade(self):
        grades_list = []
        for course_grades in self.grades.values():
            grades_list += course_grades
        return round(sum(grades_list) / len(grades_list), 1)
    def course_avg_grade(self, course):
        return round(sum(self.grades[course]) / len(self.grades[course]), 1)
    def course_avg_grade(self, course, *lecturers):
        grade_sum = 0
        grades_count = 0
        for lecturer in lecturers:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
                grade_sum += sum(lecturer.grades[course])
                grades_count += len(lecturer.grades[course])
        print(f'Средняя оценка за лекции по курсу {course}: {round(grade_sum / grades_count, 1)}')
    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}'

class Reviewer(Mentor):
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student_list = []
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('Sam', 'Smith', 'your_gender')
best_student.courses_in_progress += ['Python','Git']
best_student2.courses_in_progress += ['Java','Git']
best_student.finished_courses += ['Введение в программирование']
best_student2.finished_courses += ['Машинопись']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor2 = Reviewer('Once', 'Toldme')
cool_mentor.courses_attached += ['Python']
cool_mentor2.courses_attached += ['Java']

cool_lecturer = Lecturer('No', 'Name')
cool_lecturer2 = Lecturer('Yes', 'Surname')
cool_lecturer.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['Java']

best_student.rate_lec(cool_lecturer, 'Python', 10)
best_student.rate_lec(cool_lecturer, 'Python', 9)
best_student.rate_lec(cool_lecturer, 'Python', 1)
best_student2.rate_lec(cool_lecturer2, 'Java', 8)
best_student2.rate_lec(cool_lecturer2, 'Java', 9)
best_student2.rate_lec(cool_lecturer2, 'Java', 4)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 6)
cool_mentor2.rate_hw(best_student2, 'Java', 9)
cool_mentor2.rate_hw(best_student2, 'Java', 5)
cool_mentor2.rate_hw(best_student2, 'Java', 9)

print(best_student,"\n")
print(best_student2,"\n")

print(cool_mentor,"\n")
print(cool_mentor2,"\n")

print(cool_lecturer,"\n")
print(cool_lecturer2,'\n')

print(cool_lecturer < cool_lecturer2)
print(best_student < best_student2)
print()
# best_student.course_avg_grade('Python')
# best_student2.course_avg_grade('Java')
best_student.course_avg_grade('Python', best_student, best_student2)
best_student.course_avg_grade('Java', best_student, best_student2)
print()
cool_lecturer.course_avg_grade('Python', cool_lecturer, cool_lecturer2)
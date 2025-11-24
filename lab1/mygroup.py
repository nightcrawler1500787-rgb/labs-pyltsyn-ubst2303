groupmates = [
    {
        "name": "Андрей",
        "surname": "Пыльцын",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Марат",
        "surname": "Орлов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Иван",
        "surname": "Будников",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Анна",
        "surname": "Тарасова",
        "exams": ["Математика", "Физика", "Химия"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Илья",
        "surname": "Левченко",
        "exams": ["Биология", "География", "Литература"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Артем",
        "surname": "Сиренко",
        "exams": ["Экономика", "Право", "Социология"],
        "marks": [5, 5, 4]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def filter_students_by_average(students, min_average):
    """
    Фильтрует студентов по среднему баллу
    
    Args:
        students: список студентов
        min_average: минимальный средний балл для фильтрации
    
    Returns:
        список студентов с средним баллом выше заданного
    """
    filtered_students = []
    
    for student in students:
        # Вычисляем средний балл студента
        average_mark = sum(student["marks"]) / len(student["marks"])
        
        # Если средний балл выше заданного, добавляем студента в результат
        if average_mark > min_average:
            filtered_students.append(student)
    
    return filtered_students

# Основная программа
if __name__ == "__main__":
    print("Все студенты группы:")
    print_students(groupmates)ы
    print("\n" + "="*80 + "\n")
    
    try:
        # Запрашиваем у пользователя минимальный средний балл
        min_average = float(input("Введите минимальный средний балл для фильтрации: "))
        
        # Фильтруем студентов
        filtered_students = filter_students_by_average(groupmates, min_average)
        
        print(f"\nСтуденты со средним баллом выше {min_average}:")
        if filtered_students:
            print_students(filtered_students)
        else:
            print("Нет студентов, удовлетворяющих условию фильтрации.")
            
    except ValueError:
        print("Ошибка: введите числовое значение для среднего балла.")

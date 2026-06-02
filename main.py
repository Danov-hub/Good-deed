import random
from circular_list import CircularDoublyLinkedList


def load_students_from_file(filename):
    students_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                name = line.strip()
                if name:
                    students_list.append(name)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None
    
    if not students_list:
        print("Ошибка: Файл пуст или не содержит имён.")
        return None
    
    return students_list


def play_game(students_list, rounds):
    game_list = CircularDoublyLinkedList()
    for name in students_list:
        game_list.append(name)
    
    current_student = game_list.get_head()
    
    print("\n" + "="*60)
    print("ИГРА НАЧАЛАСЬ!")
    print("="*60)
    
    for round_num in range(1, rounds + 1):
        step_value = random.randint(-10, 10)
        if step_value > 0:
            direction = "по часовой стрелке"
            steps = step_value
            clockwise_move = True
        elif step_value < 0:
            direction = "против часовой стрелки"
            steps = abs(step_value)
            clockwise_move = False
        else:
            direction = "ноль шагов"
            steps = 0
            clockwise_move = True
            
        if steps > 0:
            current_student = game_list.get_student_by_offset(
                current_student, steps, clockwise_move
            )
        current_student.rating += 1
        
        print(f"\n--- Раунд {round_num} ---")
        print(f"Выпавшее число: {step_value} ({direction})")
        print(f"Доброе дело сделал: {current_student.name}")
        print(f"Рейтинг ученика после дела: {current_student.rating}")
        
        if step_value > 0:
            next_student = game_list.get_neighbor(current_student, clockwise=True)
        elif step_value < 0:
            next_student = game_list.get_neighbor(current_student, clockwise=False)
        else:
            next_student = current_student
        current_student = next_student
    
    print("\n" + "="*60)
    print("ИГРА ЗАВЕРШЕНА!")
    print("="*60)
    return game_list


def show_results(game_list):
    sorted_students = game_list.sort_by_rating_desc()
    
    print("\nИтоговый рейтинг учеников:")
    print("-" * 50)
    print(f"{'№':<4} {'Фамилия':<25} {'Рейтинг':<10}")
    print("-" * 50)
    
    for idx, (name, rating) in enumerate(sorted_students, 1):
        print(f"{idx:<4} {name:<25} {rating:<10}")
    print("-" * 50)


def main():
    filename = "students.txt"
    
    students_list = load_students_from_file(filename)
    if students_list is None:
        print("Программа завершена из-за ошибки загрузки данных.")
        return
    
    print(f"Загружено учеников: {len(students_list)}")
    print("Список учеников:", ", ".join(students_list))
    
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Начать игру")
        print("2. Выйти из программы")
        print("-"*50)
        
        choice = input("Выберите действие (1-2): ").strip()
        if choice == '1':
            while True:
                try:
                    rounds_input = input("Введите количество раундов игры: ").strip()
                    rounds = int(rounds_input)
                    if rounds <= 0:
                        print("Ошибка: количество раундов должно быть положительным числом.")
                        continue
                    break
                except ValueError:
                    print("Ошибка: введите целое число.")
            
            game_list = play_game(students_list, rounds)
            show_results(game_list)        
            input("\nНажмите Enter, чтобы вернуться в меню...")
        elif choice == '2':
            print("До свидания!")
            break 
        else:
            print("Ошибка: выберите пункт 1 или 2.")

if __name__ == "__main__":
    main()

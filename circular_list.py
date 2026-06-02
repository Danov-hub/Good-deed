import random

class Node:
    def __init__(self, name):
        self.name = name
        self.rating = 0
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, name):
        new_node = Node(name)
        
        if self.head is None:
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size += 1

    def get_student_by_offset(self, start_node, steps, clockwise=True):
        current = start_node
        for _ in range(steps):
            if clockwise:
                current = current.next
            else:
                current = current.prev
        return current

    def get_neighbor(self, node, clockwise=True):
        return node.next if clockwise else node.prev

    def get_all_students_with_ratings(self):
        if self.head is None:
            return []
        result = []
        current = self.head
        for i in range(self.size):
            result.append((current.name, current.rating))
            current = current.next
        return result

    def sort_by_rating_desc(self):
        students = self.get_all_students_with_ratings()
        if not students:
            return []
        students_with_indices = [(name, rating, idx) for idx, (name, rating) in enumerate(students)]
        students_with_indices.sort(key=lambda x: (-x[1], x[2]))
        return [(name, rating) for name, rating, idx in students_with_indices]

    def get_head(self):
        return self.head
    
    def display_all(self):
        if self.head is None:
            print("Список пуст")
            return
        
        current = self.head
        for i in range(self.size):
            print(f"{current.name} (рейтинг: {current.rating})")
            current = current.next

#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};

void addStudent(Student*& students, int& size) {
    students = (Student*)realloc(students, (size + 1) * sizeof(Student));
    cout << "Enter ID: ";
    cin >> students[size].id;
    cout << "Enter Name: ";
    cin >> students[size].name;
    cout << "Enter CGPA: ";
    cin >> students[size].cgpa;
    size++;
}

void displayStudents(Student* students, int size) {
    cout << "\nID\tName\tCGPA\n";
    for (int i = 0; i < size; i++)
        cout << students[i].id << "\t" << students[i].name << "\t" << students[i].cgpa << endl;
}

void bubbleSortByName(Student* students, int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (strcmp(students[j].name, students[j + 1].name) > 0) {
                swap(students[j], students[j + 1]);
            }
        }
    }
}

void selectionSortByCGPA(Student* students, int size, bool ascending = true) {
    for (int i = 0; i < size - 1; i++) {
        int target = i;
        for (int j = i + 1; j < size; j++) {
            if ((ascending && students[j].cgpa < students[target].cgpa) ||
                (!ascending && students[j].cgpa > students[target].cgpa))
                target = j;
        }
        swap(students[i], students[target]);
    }
}

int main() {
    Student* students = nullptr;
    int size = 0, choice;

    do {
        cout << "\n1. Add Student\n2. Display\n3. Sort by Name\n4. Sort by CGPA (Asc)\n5. Sort by CGPA (Desc)\n6. Exit\nChoice: ";
        cin >> choice;

        switch (choice) {
            case 1: addStudent(students, size); break;
            case 2: displayStudents(students, size); break;
            case 3: bubbleSortByName(students, size); break;
            case 4: selectionSortByCGPA(students, size, true); break;
            case 5: selectionSortByCGPA(students, size, false); break;
        }
    } while (choice != 6);

    free(students);
    return 0;
}

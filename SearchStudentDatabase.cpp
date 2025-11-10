#include <iostream>
#include <cstring>  // for strcmp
#include <cstdlib>  // for malloc, realloc, free
using namespace std;

// Structure to store student details
struct Student {
    int id;
    char name[50];
    float cgpa;
};

// Function to add a new student
void addStudent(Student*& students, int& size) {
    students = (Student*)realloc(students, (size + 1) * sizeof(Student));  // expand memory
    
    cout << "\nEnter Student ID: ";
    cin >> students[size].id;
    cout << "Enter Student Name: ";
    cin.ignore();
    cin.getline(students[size].name, 50);
    cout << "Enter Student CGPA: ";
    cin >> students[size].cgpa;

    size++;
    cout << "Student added successfully!\n";
}

// Function to display all students
void displayStudents(Student* students, int size) {
    cout << "\n--- Student Records ---\n";
    for (int i = 0; i < size; i++) {
        cout << "ID: " << students[i].id
             << " | Name: " << students[i].name
             << " | CGPA: " << students[i].cgpa << endl;
    }
}

// Linear Search by ID
void linearSearch(Student* students, int size, int id) {
    for (int i = 0; i < size; i++) {
        if (students[i].id == id) {
            cout << "\nRecord Found (Linear Search):\n";
            cout << "ID: " << students[i].id << " | Name: " << students[i].name << " | CGPA: " << students[i].cgpa << endl;
            return;
        }
    }
    cout << "\nRecord not found (Linear Search).\n";
}

// Sort Students by ID (for Binary Search)
void sortStudents(Student* students, int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (students[j].id > students[j + 1].id) {
                Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }
}

// Binary Search by ID
void binarySearch(Student* students, int size, int id) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (students[mid].id == id) {
            cout << "\nRecord Found (Binary Search):\n";
            cout << "ID: " << students[mid].id << " | Name: " << students[mid].name << " | CGPA: " << students[mid].cgpa << endl;
            return;
        } else if (students[mid].id < id)
            low = mid + 1;
        else
            high = mid - 1;
    }
    cout << "\nRecord not found (Binary Search).\n";
}

// Main Function
int main() {
    Student* students = NULL;
    int size = 0, choice, id;

    while (true) {
        cout << "\n--- MENU ---";
        cout << "\n1. Add Student";
        cout << "\n2. Display All Students";
        cout << "\n3. Linear Search by ID";
        cout << "\n4. Binary Search by ID";
        cout << "\n5. Exit";
        cout << "\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addStudent(students, size);
                break;
            case 2:
                displayStudents(students, size);
                break;
            case 3:
                cout << "Enter ID to search: ";
                cin >> id;
                linearSearch(students, size, id);
                break;
            case 4:
                sortStudents(students, size); // sort before binary search
                cout << "Enter ID to search: ";
                cin >> id;
                binarySearch(students, size, id);
                break;
            case 5:
                free(students);
                cout << "Exiting...";
                return 0;
            default:
                cout << "Invalid choice!";
        }
    }
}
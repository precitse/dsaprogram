#include <iostream>
#include <cstring>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};

int main() {
    Student students[100];
    int size = 0, choice;

    do {
        cout << "\n1.Add 2.Display 3.Sort Name 4.Sort CGPA Asc 5.Sort CGPA Desc 6.Exit\nChoice: ";
        cin >> choice;

        if(choice == 1) {
            cout << "ID: "; cin >> students[size].id;
            cout << "Name: "; cin >> students[size].name;
            cout << "CGPA: "; cin >> students[size].cgpa;
            size++;
        }
        else if(choice == 2) {
            cout << "\nID\tName\tCGPA\n";
            for(int i=0;i<size;i++)
                cout << students[i].id << "\t" << students[i].name << "\t" << students[i].cgpa << endl;
        }
        else if(choice == 3) { // Bubble sort by name
            for(int i=0;i<size-1;i++)
                for(int j=0;j<size-i-1;j++)
                    if(strcmp(students[j].name, students[j+1].name)>0)
                        swap(students[j], students[j+1]);
        }
        else if(choice == 4) { // Selection sort CGPA Asc
            for(int i=0;i<size-1;i++){
                int min_idx=i;
                for(int j=i+1;j<size;j++)
                    if(students[j].cgpa<students[min_idx].cgpa) min_idx=j;
                swap(students[i], students[min_idx]);
            }
        }
        else if(choice == 5) { // Selection sort CGPA Desc
            for(int i=0;i<size-1;i++){
                int max_idx=i;
                for(int j=i+1;j<size;j++)
                    if(students[j].cgpa>students[max_idx].cgpa) max_idx=j;
                swap(students[i], students[max_idx]);
            }
        }

    } while(choice != 6);
}

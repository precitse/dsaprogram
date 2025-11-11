#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

struct Student {
    int id;
    char name[50];
    float cgpa;
};

void addStudent(Student*& s, int& n) {
    s = (Student*)realloc(s, (n + 1) * sizeof(Student));
    cout << "\nEnter Student ID: "; cin >> s[n].id;
    cin.ignore();
    cout << "Enter Student Name: "; cin.getline(s[n].name, 50);
    cout << "Enter Student CGPA: "; cin >> s[n].cgpa;
    n++; cout << "Student added successfully!\n";
}

void displayStudents(Student* s, int n) {
    cout << "\n--- Student Records ---\n";
    for(int i=0;i<n;i++)
        cout << "ID: " << s[i].id << " | Name: " << s[i].name << " | CGPA: " << s[i].cgpa << endl;
}

void linearSearch(Student* s, int n, int id) {
    for(int i=0;i<n;i++)
        if(s[i].id==id) {
            cout << "\nRecord Found (Linear Search):\n";
            cout << "ID: " << s[i].id << " | Name: " << s[i].name << " | CGPA: " << s[i].cgpa << endl;
            return;
        }
    cout << "\nRecord not found (Linear Search).\n";
}

void sortStudents(Student* s, int n) {
    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-i-1;j++)
            if(s[j].id > s[j+1].id) swap(s[j], s[j+1]);
}

void binarySearch(Student* s, int n, int id) {
    int l=0,h=n-1;
    while(l<=h) {
        int m=(l+h)/2;
        if(s[m].id==id) {
            cout << "\nRecord Found (Binary Search):\n";
            cout << "ID: " << s[m].id << " | Name: " << s[m].name << " | CGPA: " << s[m].cgpa << endl;
            return;
        }
        else if(s[m].id<id) l=m+1;
        else h=m-1;
    }
    cout << "\nRecord not found (Binary Search).\n";
}

int main() {
    Student* s=NULL; int n=0,choice,id;
    while(true) {
        cout << "\n--- MENU ---\n1.Add Student\n2.Display All\n3.Linear Search\n4.Binary Search\n5.Exit\nChoice: ";
        cin >> choice;
        switch(choice) {
            case 1: addStudent(s,n); break;
            case 2: displayStudents(s,n); break;
            case 3: cout<<"Enter ID: "; cin>>id; linearSearch(s,n,id); break;
            case 4: sortStudents(s,n); cout<<"Enter ID: "; cin>>id; binarySearch(s,n,id); break;
            case 5: free(s); cout<<"Exiting..."; return 0;
            default: cout<<"Invalid choice!";
        }
    }
}

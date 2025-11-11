#include <iostream>
using namespace std;

#define SIZE 5

class CircularQueue {
    int front, rear, arr[SIZE];
public:
    CircularQueue() { front = rear = -1; }

    void enqueue(int x) {
        if ((rear + 1) % SIZE == front) { 
            cout << "Queue Overflow\n"; 
            return; 
        }
        if (front == -1) front = 0;
        rear = (rear + 1) % SIZE;
        arr[rear] = x;
        cout << x << " inserted\n";
    }

    void dequeue() {
        if (front == -1) { 
            cout << "Queue Underflow\n"; 
            return; 
        }
        cout << arr[front] << " deleted\n";
        if (front == rear) front = rear = -1; 
        else front = (front + 1) % SIZE;
    }

    void display() {
        if (front == -1) { cout << "Queue is empty\n"; return; }
        cout << "Queue: ";
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear) break;
            i = (i + 1) % SIZE;
        }
        cout << endl;
    }
};

int main() {
    CircularQueue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.display();
    q.dequeue();
    q.display();
    q.enqueue(40);
    q.enqueue(50);
    q.enqueue(60); // Overflow
    q.display();
}

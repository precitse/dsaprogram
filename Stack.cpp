#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
using namespace std;

// =====================
// Stack Implementation using Linked List
// =====================
class Node {
public:
    char data;
    Node* next;
    Node(char d) {
        data = d;
        next = NULL;
    }
};

class Stack {
    Node* top;
public:
    Stack() {
        top = NULL;
    }

    void push(char x) {
        Node* temp = new Node(x);
        temp->next = top;
        top = temp;
    }

    char pop() {
        if (isEmpty()) return '\0';
        Node* temp = top;
        char val = temp->data;
        top = top->next;
        delete temp;
        return val;
    }

    char peek() {
        if (isEmpty()) return '\0';
        return top->data;
    }

    bool isEmpty() {
        return top == NULL;
    }
};

// =====================
// Helper Functions
// =====================
int precedence(char c) {
    if (c == '^') return 3;
    else if (c == '*' || c == '/') return 2;
    else if (c == '+' || c == '-') return 1;
    else return -1;
}

bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

// =====================
// INFIX → POSTFIX
// =====================
string infixToPostfix(string infix) {
    Stack s;
    string postfix = "";
    
    for (int i = 0; i < infix.length(); i++) {
        char ch = infix[i];
        
        // If operand, add to result
        if (isalnum(ch))
            postfix += ch;
        
        // If '(', push to stack
        else if (ch == '(')
            s.push(ch);
        
        // If ')', pop until '('
        else if (ch == ')') {
            while (!s.isEmpty() && s.peek() != '(')
                postfix += s.pop();
            s.pop(); // remove '('
        }
        
        // If operator
        else if (isOperator(ch)) {
            while (!s.isEmpty() && precedence(s.peek()) >= precedence(ch))
                postfix += s.pop();
            s.push(ch);
        }
    }
    
    // Pop all remaining operators
    while (!s.isEmpty())
        postfix += s.pop();
    
    return postfix;
}

// =====================
// INFIX → PREFIX
// =====================
string infixToPrefix(string infix) {
    reverse(infix.begin(), infix.end());
    
    // Swap '(' with ')' after reversing
    for (int i = 0; i < infix.length(); i++) {
        if (infix[i] == '(') infix[i] = ')';
        else if (infix[i] == ')') infix[i] = '(';
    }

    string postfix = infixToPostfix(infix);
    reverse(postfix.begin(), postfix.end());
    return postfix;
}

// =====================
// MAIN FUNCTION
// =====================
int main() {
    string infix;
    cout << "Enter infix expression: ";
    cin >> infix;

    cout << "\nPostfix Expression: " << infixToPostfix(infix);
    cout << "\nPrefix Expression : " << infixToPrefix(infix);

    return 0;
}

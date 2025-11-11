#include <iostream>
#include <algorithm>
using namespace std;

struct Node {
    char data;
    Node* next;
} *top = NULL;

void push(char x) {
    Node* t = new Node;
    t->data = x;
    t->next = top;
    top = t;
}
char pop() {
    if (!top) return '\0';
    char x = top->data;
    Node* t = top;
    top = top->next;
    delete t;
    return x;
}
int prec(char c) {
    if (c == '+' || c == '-') return 1;
    if (c == '*' || c == '/') return 2;
    return 0;
}

string infixToPostfix(string exp) {
    string out = "";
    for (char c : exp) {
        if (isalnum(c)) out += c;
        else if (c == '(') push(c);
        else if (c == ')') {
            while (top && top->data != '(') out += pop();
            pop();
        } else {
            while (top && prec(top->data) >= prec(c)) out += pop();
            push(c);
        }
    }
    while (top) out += pop();
    return out;
}

string infixToPrefix(string exp) {
    reverse(exp.begin(), exp.end());
    for (char &c : exp) {
        if (c == '(') c = ')';
        else if (c == ')') c = '(';
    }
    string post = infixToPostfix(exp);
    reverse(post.begin(), post.end());
    return post;
}

int main() {
    string infix;
    cout << "Enter infix: ";
    cin >> infix;
    cout << "Postfix: " << infixToPostfix(infix) << endl;
    cout << "Prefix: " << infixToPrefix(infix);
}2+3*5-4

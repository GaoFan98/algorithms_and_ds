#include <iostream>
#include<cstring>
#include <stack>
#include <map>

using namespace std;

class Node
{
private:
    /* data */
public:
    char data;
    Node* next;
};

class Stack
{
private:
    Node* top;
public:
    Stack();
    ~Stack();
    void push(char x);
    char pop();
    char peek(int index);
    int isEmpty();
    int isFull();
    char stackTop();
};

Stack::Stack() {
    top = nullptr;
}

Stack::~Stack() {
    Node* p = top;
    while (top){
        top = top->next;
        delete p;
        p = top;
    }
}

void Stack::push(char x) {
    Node* t = new Node;
    if (t == nullptr){
        cout << "Stack Overflow!" << endl;
    } else {
        t->data = x;
        t->next = top;
        top = t;
    }
}

char Stack::pop() {
    Node* p;
    char x = -1;
    if (top == nullptr){
        cout << "Stack Underflow!" << endl;
    } else {
        p = top;
        x = p->data;
        top = top->next;
        delete p;
    }
    return x;
}

int Stack::isFull() {
    Node* t = new Node;
    int r = t ? 1 : 0;
    delete t;
    return r;
}
 
int Stack::isEmpty() {
    return top ? 0 : 1;
}

char Stack::stackTop() {
    if (top){
        return top->data;
    }
    return -1;
}

char Stack::peek(int index) {
    if (isEmpty()){
        return -1;
    } else {
        Node* p = top;
 
        for (int i=0; p != nullptr && i<index-1; i++){
            p = p->next;
        }
 
        if (p != nullptr){
            return p->data;
        } else {
            return -1;
        }
    }
}

int isBalancedPar(char* exp){
    Stack stk;
 
    for (int i=0; i<strlen(exp); i++){
        if (exp[i] == '('){
            stk.push(exp[i]);
        } else if (exp[i] == ')'){
            if (stk.isEmpty()){
                return false;
            } else {
                stk.pop();
            }
        }
    }
    return stk.isEmpty() ? true : false;
}

int isBalancedAll(char* exp){
    // Create map
    map<char, char> mapping;
    mapping['}'] = '{';
    mapping[')'] = '(';
    mapping[']'] = '[';
 
    // Create map iterator
    map<char, char>::iterator itr;
 
    // Create stack
    stack<char> stk;
 
    for (int i=0; i<strlen(exp); i++){
        if (exp[i] == '{' || exp[i] == '[' || exp[i] == '('){
            stk.push(exp[i]);
        } else if (exp[i] == '}' || exp[i] == ']' || exp[i] == ')'){
            if (stk.empty()){
                return false;
            } else {
                char temp = stk.top();
                itr = mapping.find(exp[i]);
                if (temp == itr->second){  // itr->first is key, itr->second is value
                    stk.pop();
                } else {
                    return false;
                }
            }
        }
    }
    return stk.empty() ? true : false;
}
 
int main() {
 
    char E[] = "((a+b)*(c-d))";
    cout << isBalancedPar(E) << endl;
 
    char F[] = "((a+b)*(c-d)))";
    cout << isBalancedPar(F) << endl;
 
    char G[] = "(((a+b)*(c-d))";
    cout << isBalancedPar(G) << endl;
 
    return 0;
}
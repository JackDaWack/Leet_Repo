#include <iostream>
#include "add_two_numbers.cpp"
using namespace std;

//Copilot generated test code.

int main() {
    // Create first number: 342 represented as 2 -> 4 -> 3
    ListNode* l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);

    // Create second number: 465 represented as 5 -> 6 -> 4
    ListNode* l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);

    // Add the two numbers
    ListNode* result = add_two_numbers(l1, l2);

    // Print the result
    cout << "Result: ";
    while (result != NULL) {
        cout << result->val << " ";
        result = result->next;
    }
    cout << endl;

    return 0;
}
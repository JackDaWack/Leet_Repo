#include <math.h>
#include <iostream>

//Copilot generated code for list node structure.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//Non-Ai generated code.
//Helper function to convert ListNode to int.
int ln2int(ListNode* ln){
    int result = 0;
    int place = 0;
    while (ln->next != NULL){
        result = result + ln->val * (pow(10,place));
        ln = ln->next;
        place++;
    }
    return result;
}
//Main solution.
ListNode* add_two_numbers(ListNode* l1, ListNode* l2) {
    int sum = ln2int(l1) + ln2int(l2);
    ListNode* solution = new ListNode(0);
    ListNode* curr = solution;
    while (sum > 0){
        curr->val = sum % 10;
        sum = sum / 10;
        curr->next = new ListNode(0);
        curr = curr->next;
        if (sum < 10){
            curr->val = sum;
            sum = 0;
        }
    }
    return solution;
}
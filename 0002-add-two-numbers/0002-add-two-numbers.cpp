/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        int sum=0;
        ListNode* first=l1;
        ListNode* second=l2;
        ListNode* node=new ListNode(0);
        ListNode* head=node;
        while(first!=nullptr || second!=nullptr ||carry!=0 )
        {
            sum=carry;
            if (first!=nullptr)
            {
                sum=sum+first->val;
                first=first->next;

            }
            if(second!=nullptr)
            {
                sum=sum+second->val;
                second=second->next;
            }
            carry=sum/10;
            head->next=new ListNode(sum%10);
            head=head->next;

        }
        ListNode* result=node->next;
        delete node;
        return result;
    }
};
        


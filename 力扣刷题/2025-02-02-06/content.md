# 「每日一题」力扣 234 回文链表

你好啊，我是蓝莓，今天是每日一题的第 50 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[234 回文链表](https://leetcode.cn/problems/palindrome-linked-list/description/)





## 题目描述

给你一个单链表的头节点 `head` ，请你判断该链表是否为

回文链表

。如果是，返回 `true` ；否则，返回 `false` 。



 

**示例 1：**

![img](content.assets/pal1linked-list.jpg)

```
输入：head = [1,2,2,1]
输出：true
```

**示例 2：**

![img](content.assets/pal2linked-list.jpg)

```
输入：head = [1,2]
输出：false
```

 

**提示：**

- 链表中节点数目在范围`[1, 105]` 内
- `0 <= Node.val <= 9`

 

**进阶：**你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？





## 实现

**思路**

- 这个题目和 `143 重排链表` 的做法非常相似，代码我都是直接复制过来的，做了一些简单的修改
- 可以参考 `143` 号题目的代码





**C++ 代码实现**

```c++
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
    bool isPalindrome(ListNode* head) {
        
        // 只有一个节点的情况直接返回 true 即可
        if( head->next == nullptr ) {
            return true;
        }

        ListNode* dummyHead = new ListNode(-1, head);

        ListNode* preSlow = dummyHead;
        ListNode* slow = head;
        ListNode* fast = head;

        while( fast != nullptr && fast->next != nullptr ) {
            preSlow = slow;
            slow = slow->next;
            fast = fast->next->next;
        }

        preSlow->next = nullptr;
        delete dummyHead;

        ListNode* head1 = head;
        ListNode* head2 = reverseList(slow);

        ListNode* cur1 = head1;
        ListNode* cur2 = head2;

        while( cur1 != nullptr && cur2 != nullptr ) {
            if( cur1->val != cur2->val ) {
                return false;
            }

            cur1 = cur1->next;
            cur2 = cur2->next;
        }

        return true;
    }

    ListNode* reverseList(ListNode* head) {
        // head 表示需要翻转的链表头节点
        // 返回值为翻转后的链表头结点

        ListNode* dummyHead = new ListNode(-1, head);

        ListNode* pre = dummyHead;
        ListNode* cur = head;

        while( cur != nullptr ) {
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }

        dummyHead->next->next = nullptr;

        delete dummyHead;
        return pre;
    }
};
```


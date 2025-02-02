# 「每日一题」力扣 19 删除链表的倒数第 N 个结点

你好啊，我是蓝莓，今天是每日一题的第 48 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[19 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/)





## 题目描述

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

 

**示例 1：**

![img](content.assets/remove_ex1.jpg)

```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

**示例 2：**

```
输入：head = [1], n = 1
输出：[]
```

**示例 3：**

```
输入：head = [1,2], n = 1
输出：[1]
```

 

**提示：**

- 链表中结点的数目为 `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

 

**进阶：**你能尝试使用一趟扫描实现吗？





## 实现

**思路**

- 最简单的思路是先遍历一遍链表看看有几个节点，然后计算出倒数第 n 个节点正着数是第几个
- 另外一种只需要遍历一遍的方法是使用两个指针，分别为 `slow` 和 `fast` ，我们让这两个指针之间空出一定的距离后再让它们两个同时向后移动，这样当 `fast` 走到底的时候，我们就可以通过 `slow` 找到倒数第 `n` 个节点是谁了





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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummyHead = new ListNode(-1, head);
        ListNode* slow = dummyHead;
        ListNode* fast = head;
        
        // 让 fast 和 slow 之间相差 n 个节点（包括 fast 指向的节点本身）
        for( int i = 0 ; i < n ; i++ ) {
            fast = fast->next;
        }

        // 这时候让 slow 和 fast 同时移动
        // 当 fast 到尾的时候 slow 刚好指向需要被删除的节点的前一个节点
        while( fast != nullptr ) {
            slow = slow->next;
            fast = fast->next;
        }

        // 在逻辑上删除节点
        slow->next = slow->next->next;

        ListNode* newHead = dummyHead->next;
        delete dummyHead;

        return newHead;
    }
};
```

 
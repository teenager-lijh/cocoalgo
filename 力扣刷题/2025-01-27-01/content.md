# 「每日一题」力扣 328 奇偶链表

你好啊，我是蓝莓，今天是每日一题的第 37 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[328 奇偶链表](https://leetcode.cn/problems/odd-even-linked-list/description/)





## 题目描述

给定单链表的头节点 `head` ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。

**第一个**节点的索引被认为是 **奇数** ， **第二个**节点的索引为 **偶数** ，以此类推。

请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

你必须在 `O(1)` 的额外空间复杂度和 `O(n)` 的时间复杂度下解决这个问题。

 

**示例 1:**

![img](content.assets/oddeven-linked-list.jpg)

```
输入: head = [1,2,3,4,5]
输出: [1,3,5,2,4]
```

**示例 2:**

![img](content.assets/oddeven2-linked-list.jpg)

```
输入: head = [2,1,3,5,6,4,7]
输出: [2,3,6,7,1,5,4]
```

 

**提示:**

- `n == ` 链表中的节点数
- `0 <= n <= 104`
- `-106 <= Node.val <= 106`





## 实现

**思路**

- 这个题目和 `86 分隔链表` 非常相似
- 同样的，使用两个虚拟头结点来存储对应类别的节点
- 遍历原始的链表，不停的摘下一个元素然后放在对应分类的链表中
- 最后将两个链表进行合并即可





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
    ListNode* oddEvenList(ListNode* head) {
        ListNode* oddHead = new ListNode(-1, nullptr);
        ListNode* evenHead = new ListNode(-1, nullptr);

        ListNode* oddCur = oddHead;
        ListNode* evenCur = evenHead;

        ListNode* cur = head;
        bool isOdd = true;

        while( cur != nullptr ) {
            ListNode* next = cur->next;

            if( isOdd ) {
                oddCur->next = cur;
                oddCur = cur;
            } else {
                evenCur->next = cur;
                evenCur = cur;
            }

            cur->next = nullptr;
            cur = next;
            isOdd = !isOdd;
        }

        ListNode* res = nullptr;

        if( oddHead->next != nullptr ) {
            res = oddHead->next;
        }

        if( res == nullptr ) {
            res = evenHead->next;
        } else {
            oddCur->next = evenHead->next;
        }

        return res;
    }
};
```


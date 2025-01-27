# 「每日一题」力扣 86 分隔链表

你好啊，我是蓝莓，今天是每日一题的第 35 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[86 分割链表](https://leetcode.cn/problems/partition-list/description/)





## 题目描述

给你一个链表的头节点 `head` 和一个特定值 `x` ，请你对链表进行分隔，使得所有 **小于** `x` 的节点都出现在 **大于或等于** `x` 的节点之前。

你应当 **保留** 两个分区中每个节点的初始相对位置。

 

**示例 1：**

![img](content.assets/partition.jpg)

```
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
```

**示例 2：**

```
输入：head = [2,1], x = 2
输出：[1,2]
```

 

**提示：**

- 链表中节点的数目在范围 `[0, 200]` 内
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`





## 实现

**思路**

- 题目要求的我们将链表分割成两部分
- （1）比 x 小的部分
- （2）比 x 大或者等于的部分
- 对于这两个部分，我们可以新建两个虚拟头结点，然后遍历原始链表，每次遍历到的节点都将它从原始链表上摘下来放在对应分类的虚拟头结点所在的链表尾部，最后将两个新的链表进行合并即可
- 这样一来，不仅可以在一轮遍历中完成链表分割，而且保持了元素的相对顺序





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
    ListNode* partition(ListNode* head, int x) {

        if( head == nullptr ) {
            return head;
        }

        ListNode* lessHead = new ListNode(-1, nullptr);
        ListNode* greatHead = new ListNode(-1, nullptr);

        ListNode* lessCur = lessHead;
        ListNode* greatCur = greatHead;

        ListNode* cur = head;
        while( cur != nullptr ) {
            ListNode* next = cur->next;

            if( cur->val >= x ) {
                greatCur->next = cur;
                greatCur = cur;
            } else {
                // cur->val < x
                lessCur->next = cur;
                lessCur = cur;
            }
            
            cur->next = nullptr;
            cur = next;
        }

        ListNode* res = nullptr;

        if( lessHead->next != nullptr ) {
            res = lessHead->next;
        }

        if( res != nullptr ) {
            lessCur->next = greatHead->next;
        } else {
            res = greatHead->next;
        }

        return res;
    }
};
```


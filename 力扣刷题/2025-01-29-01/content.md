# 「每日一题」力扣 21 合并两个有序链表

你好啊，我是蓝莓，今天是每日一题的第 42 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[21 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/description/)





## 题目描述

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

**示例 1：**

![img](content.assets/merge_ex1.jpg)

```
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
```

**示例 2：**

```
输入：l1 = [], l2 = []
输出：[]
```

**示例 3：**

```
输入：l1 = [], l2 = [0]
输出：[0]
```

 

**提示：**

- 两个链表的节点数目范围是 `[0, 50]`
- `-100 <= Node.val <= 100`
- `l1` 和 `l2` 均按 **非递减顺序** 排列





## 实现

**思路**

- 这个题目的做法和归并排序中归并的做法很像，在归并的过程中主要分为两种情况
- （1）两个链表都不为空，这时候选择其中值较小的节点挂在最终链表的尾部
- （2）其中一个链表为空，另一个链表不为空，这时候就直接无脑的将不为空的那个链表的所有节点都挂在最终链表的末尾即可





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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* cur1 = list1;
        ListNode* cur2 = list2;

        ListNode* dummy = new ListNode(-1, nullptr);
        ListNode* cur = dummy;

        while( cur1 || cur2 ) {
            if( cur1 && cur2 ) {
                if( cur1->val < cur2->val ) {
                    cur->next = cur1;
                    cur = cur1;
                    cur1 = cur1->next;
                } else {
                    cur->next = cur2;
                    cur = cur2;
                    cur2 = cur2->next;
                }
            } else if( cur1 ) {
                cur->next = cur1;
                cur = cur1;
                cur1 = cur1->next;
            } else {
                // cur2 != nullptr
                cur->next = cur2;
                cur = cur2;
                cur2 = cur2->next;
            }
        }

        cur->next = nullptr;

        cur = dummy->next;
        delete dummy;

        return cur;
    }
};
```


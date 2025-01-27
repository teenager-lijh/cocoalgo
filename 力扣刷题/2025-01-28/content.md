# 「每日一题」力扣 203 移除链表元素

你好啊，我是蓝莓，今天是每日一题的第 40 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[203 移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/description/)





## 题目描述

给你一个链表的头节点 `head` 和一个整数 `val` ，请你删除链表中所有满足 `Node.val == val` 的节点，并返回 **新的头节点** 。

 

**示例 1：**

![img](content.assets/removelinked-list.jpg)

```
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
```

**示例 2：**

```
输入：head = [], val = 1
输出：[]
```

**示例 3：**

```
输入：head = [7,7,7,7], val = 7
输出：[]
```

 

**提示：**

- 列表中的节点数目在范围 `[0, 104]` 内
- `1 <= Node.val <= 50`
- `0 <= val <= 50`





## 实现

**思路**

- 使用 `pre` 指向当前正在遍历的前一个节点（为了逻辑上一致，使用了虚拟头结点的技巧）
- 使用 `cur` 遍历链表，分为两种情况
- （1）当前节点要删除，那么 `pre` 不需要移动，只需要让 `cur` 移动一下即可
- （2）当前节点不需要删除，那么 `pre` 和 `cur` 都向前移动一次





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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode(-1, head);

        ListNode* pre = dummy;
        ListNode* cur = head;

        while( cur != nullptr ) {
            if( cur->val == val ) {
                pre->next = cur->next;
                cur = pre->next;
            } else {
                pre = cur;
                cur = cur->next;
            }
        }

        return dummy->next;
    }
};
```
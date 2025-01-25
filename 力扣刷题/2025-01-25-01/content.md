# 「每日一题」力扣 92 反转链表 II

你好啊，我是蓝莓，今天是每日一题的第 34 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[92 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/description/)





## 题目描述

给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 **反转后的链表** 。

 

**示例 1：**

![img](content.assets/rev2ex2.jpg)

```
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
```

**示例 2：**

```
输入：head = [5], left = 1, right = 1
输出：[5]
```

 

**提示：**

- 链表中节点数目为 `n`
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

 

**进阶：** 你可以使用一趟扫描完成反转吗？





## 实现

**思路 1**

- 比较简单的思路是，我们先遍历一遍链表来寻找几个关键的节点
- 然后再对中间部分的链表进行翻转，随后调整关键位置的指向





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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummyHead = new ListNode(-1, head);

        // 找到 left 和 right 代表的节点
        ListNode* leftPre = nullptr;  // left 的前一个节点
        ListNode* leftNode = nullptr;  // left 节点
        ListNode* rightNode = nullptr;  // right 节点
        ListNode* rightNext = nullptr;  // right 后一个节点

        ListNode* pre = dummyHead;  // 遍历过程中的前一个节点
        ListNode* cur = head;  // 遍历过程中的后一个节点

        // 寻找节点
        int counter = 1;
        while( cur != nullptr ) {
            if( counter == left ) {
                leftPre = pre;
                leftNode = cur;
            }
            
            if( counter == right ) {
                rightNode = cur;
                rightNext = cur->next;
            }

            pre = cur;
            cur = cur->next;
            counter++;
        }

        cur = leftNode;
        pre = leftPre;
        // 翻转链表
        while( cur != rightNext ) {
            ListNode* next = cur->next;

            cur->next = pre;
            pre = cur;
            cur = next;
        }

        // 调整翻转后的中间部分的链表指向关系
        leftNode->next = rightNext;
        leftPre->next = rightNode;

        return dummyHead->next;
    }
};
```





**思路 2**

- 在第一种方法中，我们遍历了两次链表才把问题解决
- 其实核心问题是要确定，在什么范围内才翻转链表？
- 根据题目描述，我们要在给定的范围内才需要对链表进行翻转
- 那就是这样的一个范围 `counter >= left && counter <= right`； 其中 `counter` 代表当前是第几个节点



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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummyHead = new ListNode(-1, head);

        // 找到 left 和 right 代表的节点
        ListNode* leftPre = nullptr;  // left 的前一个节点
        ListNode* leftNode = nullptr;  // left 节点
        ListNode* rightNode = nullptr;  // right 节点
        ListNode* rightNext = nullptr;  // right 后一个节点

        ListNode* pre = dummyHead;  // 遍历过程中的前一个节点
        ListNode* cur = head;  // 遍历过程中的后一个节点

        int counter = 1;
        while( cur != nullptr ) {
            ListNode* next = cur->next;

            if( counter == left ) {
                leftPre = pre;
                leftNode = cur;
            }

            if( counter == right ) {
                rightNode = cur;
                rightNext = next;
            }

            // 如果在给定范围内 那就翻转链表
            if( counter >= left && counter <= right ) {
                cur->next = pre;
            }

            // 移动到下一个节点
            pre = cur;
            cur = next;
            counter++;
        }

        // 调整指针的指向
        leftPre->next = rightNode;
        leftNode->next = rightNext;
        
        return dummyHead->next;
    }
};
```


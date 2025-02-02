# 「每日一题」力扣 143 重排链表

你好啊，我是蓝莓，今天是每日一题的第 49 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[143 重排链表](https://leetcode.cn/problems/reorder-list/description/)





## 题目描述

给定一个单链表 `L` 的头节点 `head` ，单链表 `L` 表示为：

```
L0 → L1 → … → Ln - 1 → Ln
```

请将其重新排列后变为：

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

**示例 1：**

![img](content.assets/1626420311-PkUiGI-image.png)

```
输入：head = [1,2,3,4]
输出：[1,4,2,3]
```

**示例 2：**

![img](content.assets/1626420320-YUiulT-image.png)

```
输入：head = [1,2,3,4,5]
输出：[1,5,2,4,3]
```

 

**提示：**

- 链表的长度范围为 `[1, 5 * 104]`
- `1 <= node.val <= 1000`





## 实现

**思路**

- 我们可以使用 `slow` 和 `fast` 指针来把原来的整个链表一分为二
- `slow` 指针每次只移动一个位置
- `fast` 指针每次移动两个位置
- 你可以自己手动模拟一下奇数个节点和偶数个节点的情况下 `slow` 指针最后移动到了哪个位置上
- 在我的代码实现中，`slow` 指针最后指向的是整个链表右侧那一半链表的头结点（而且如果是奇数的话，右侧的链表总是比左侧的链表多一个节点的）
- 好了，这样一来，我们只需要翻转右半部分的链表，然后将这两个链表按照题目要求的顺序拼接成为一个新的链表就可以了
- 最后要注意的一点是：我们要再设置一个 `preSlow` 指针用来指向左半部分链表的最后一个节点，然后将它的 `next` 指向 `nullptr`





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
    void reorderList(ListNode* head) {

        if(head->next == nullptr) {
            return;
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

        ListNode* dummyHead1 = new ListNode(-1, head);
        ListNode* dummyHead2 = new ListNode(-1, reverseList(slow));

        ListNode* cur = dummyHead;
        ListNode* cur1 = dummyHead1->next;
        ListNode* cur2 = dummyHead2->next;
        
        bool isCur1 = true;
        while( cur1 != nullptr && cur2 != nullptr ) {
            if(isCur1) {
                cur->next = cur1;
                cur = cur1;
                cur1 = cur1->next;
            } else {
                cur->next = cur2;
                cur = cur2;
                cur2 = cur2->next;
            }
            isCur1 = !isCur1;
        }

        // 一定是左半部分的链表先被用完
        // 我们需要把用半部分的链表的剩余部分拼接上去
        cur->next = cur2;

        delete dummyHead;
        delete dummyHead1;
        delete dummyHead2;
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


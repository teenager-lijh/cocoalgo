# 「每日一题」力扣 24 两两交换链表中的节点

你好啊，我是蓝莓，今天是每日一题的第 43 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[24 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/description/)





## 题目描述

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

**示例 1：**

![img](content.assets/swap_ex1.jpg)

```
输入：head = [1,2,3,4]
输出：[2,1,4,3]
```

**示例 2：**

```
输入：head = []
输出：[]
```

**示例 3：**

```
输入：head = [1]
输出：[1]
```

 

**提示：**

- 链表中节点的数目在范围 `[0, 100]` 内
- `0 <= Node.val <= 100`





## 实现

**思路**

- 使用三个指针 `prePre` 指针即将要交换的那两个元素的前一个元素
- `pre` 指向需要交换的两个元素的第一个元素
- `cur` 指向需要交换的两个元素的第二个元素
- 接下来就按照正常逻辑完成代码就行





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
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummyHead = new ListNode(-1, nullptr);

        if( head == nullptr || head->next == nullptr ) {
            return head;
        }

        ListNode* prePre = dummyHead;
        ListNode* pre = head;
        ListNode* cur = pre->next;

        while( true ) {
            ListNode* next = cur->next;

            // 交换节点
            prePre->next = cur;
            cur->next = pre;
            pre->next = next;

            // 为下一次交换做准备
            // 看看 pre 能不能更新
            prePre = pre;
            if(pre->next != nullptr ) {
                pre = pre->next;
            } else {
                // 如果 pre 更新后为空那就不需要再继续下去了
                break;
            }

            // 看看 cur 能不能更新
            if( pre->next != nullptr ) {
                cur = pre->next;
            } else {
                // 如果 cur 更新后为空 说明凑不够两个元素了
                break;
            }
        }

        cur = dummyHead->next;
        delete dummyHead;

        return cur;
    }
};
```


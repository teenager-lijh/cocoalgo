# 「每日一题」力扣 206 反转链表

你好啊，我是蓝莓，今天是每日一题的第 33 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[206 反转链表](https://leetcode.cn/problems/reverse-linked-list/description/)





## 题目描述

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

 

**示例 1：**

![img](content.assets/rev1ex1.jpg)

```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

**示例 2：**

![img](content.assets/rev1ex2.jpg)

```
输入：head = [1,2]
输出：[2,1]
```

**示例 3：**

```
输入：head = []
输出：[]
```

 

**提示：**

- 链表中节点的数目范围是 `[0, 5000]`
- `-5000 <= Node.val <= 5000`

 

**进阶：**链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？





## 实现

**思路**

- 这是一个和链表相关的简单题
- 为了更容易的反转链表，我们引入一个虚拟头结点，这样能简化代码的逻辑，省掉很多的边界处理





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
    ListNode* reverseList(ListNode* head) {
		//如果链表为空则直接返回 空
        if( head == nullptr ) {
            return head;
        }
		
        // 创建一个虚拟头结点 让它的 next 指向真正的头结点 head
        ListNode* dummyHead = new ListNode(-1, head);
		
        // pre 表示当前遍历到的节点的前一个节点
        ListNode* pre = dummyHead;
        // cur 表示当前正要修改 next 指向的节点
        ListNode* cur = head;
		
        // 若 cur 已经为 nullptr 说明遍历结束
        while( cur != nullptr ) {
            // 记录 cur 指向的下一个节点
            ListNode* next = cur->next;
			
            // 让 cur 指向前一个节点 pre
            cur->next = pre;
            // 为下一轮循环做准备
            // 分别将 pre 和 cur 向后移动一下
            pre = cur;
            cur = next;
        }
		
        // 其实这个时候 整个链表的翻转已经结束了
        // 但是 最一开始的 head 节点已经成为了尾节点
        // 它应该指向 nullptr 才对
        // 恰巧我们记得 dummyHead 是指向最开始的 head 节点的
        // 我们通过它来修改 head 的 next 的指向
        // 当然你也可以直接通过 head 来修改
        dummyHead->next->next = nullptr;
		
        // 此时的 pre 正好就是翻转链表后的头结点
        return pre;
    }
};
```


# 「每日一题」力扣 25 K 个一组翻转链表

你好啊，我是蓝莓，今天是每日一题的第 44 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[25 K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/description/)





## 题目描述

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

**示例 1：**

![img](content.assets/reverse_ex1.jpg)

```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```

**示例 2：**

![img](content.assets/reverse_ex2.jpg)

```
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```

 

**提示：**

- 链表中的节点数目为 `n`
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

 

**进阶：**你可以设计一个只用 `O(1)` 额外内存空间的算法解决此问题吗？





## 实现

**思路**

- 同样是翻转链表，只是这次是以 k 个节点为一组进行翻转
- 在我们翻转一整个链表的时候，我们预先已经知道的信息是 `头结点`、`尾节点的下一个节点 nullptr`
- 在我们知道了这两个节点后，我们就可以创建一个 `虚拟节点` 来简化代码的逻辑
- 但是每个以 k 个为一组的节点的头结点，我们是不知道的，所以我们最重要的任务其实是找到每一组的 `头结点` 和 `尾节点的下一个节点` ，那么剩下的代码逻辑就可以直接复用之前写过的逻辑了
- 关于寻找 k 个节点为一组的头节点是很简单的，第一组的头结点就是整个链表的头节点
- 我们使用 `cur` 指针，让 `cur` 向后移动 `k` 次，那么 `cur` 指向的就是第一组的 ``尾节点的下一个节点`，并且此时的 `cur` 也是第二组的头节点
- 还有重要的一点是，我们该如何检查是不是能够凑出 `k` 个节点呢？比如你看题目中的最后两个节点无法凑出 `3` 个节点为一组的情况是不需要反转的，在这里我有两个方法
- （1）就像代码里写的那样，如果我们在向后移动 `k` 次的过程中，循环都没执行完 ，`cur`就已经指向 `nullptr` 了，这说明肯定是凑不够了，已经没法再向后移动了
- （2）第二种情况，我们在执行循环的时候定义了一个变量 `i`，你可以把这个变量定义在循环的外部，这样，你可以在结束循环后检查一下变量 `i` 是不是刚好等于 `k` ？如果不等于的话，那说明是没有移动够 `k` 次就由于 `cur` 指向了 `nullptr` 而停了下来
- 最后我们只需要判断一下，如果凑够了 `k` 个节点就直接复用以前的反转链表的逻辑就行了
- 如果没有凑够那一定是因为 `cur` 指向了空，我们什么都不用做，整个算法也就结束了





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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummyHead = new ListNode(-1, head);

        // pre 指向需要反转的局部链表的头结点的前一个节点
        ListNode* pre = dummyHead;
        // 使用 cur 向后遍历 k 个节点 指向需要反转的局部链表的最后一个节点的下一个节点
        ListNode* cur = head;

        while( cur != nullptr ) {

            bool ok = true;  // 在寻找过程中 如果无法凑够 k 个节点则标记为 false
            for( int i = 0 ; i < k ; i++ ) {
                if( cur == nullptr ) {
                    // 无法再凑够 k 个了
                    ok = false;
                    break;
                }

                cur = cur->next;
            }

            // 如果凑够了 k 个节点那么就翻转它
            if(ok) {
                // 当前的头节点便是翻转后的尾节点
                ListNode* newEnd = pre->next;
                // 维护指针的指向
                pre->next = reverseList(pre->next, cur);
                // 让尾节点指向翻转前的尾节点的下一个节点
                newEnd->next = cur;
                // 那么反转后的尾节点就是 cur 的前一个节点
                pre = newEnd;
            }
        }

        cur = dummyHead->next;
        delete dummyHead;

        return cur;
    }

    ListNode* reverseList(ListNode* head, ListNode* end) {
        // head 表示需要翻转的链表头节点
        // end 表示需要翻转的链表的尾节点的下一个节点
        // 返回值为翻转后的链表头结点

        ListNode* dummyHead = new ListNode(-1, head);

        ListNode* pre = dummyHead;
        ListNode* cur = head;

        while( cur != end ) {
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }

        delete dummyHead;
        return pre;
    }
};
```


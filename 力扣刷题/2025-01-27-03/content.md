# 「每日一题」力扣 445 两数相加 II

你好啊，我是蓝莓，今天是每日一题的第 39 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[445 两数相加 II](https://leetcode.cn/problems/power-of-two/description/)





## 题目描述

给你两个 **非空** 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

**示例1：**

![img](https://pic.leetcode-cn.com/1626420025-fZfzMX-image.png)

```
输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]
```

**示例2：**

```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]
```

**示例3：**

```
输入：l1 = [0], l2 = [0]
输出：[0]
```

 

**提示：**

- 链表的长度范围为` [1, 100]`
- `0 <= node.val <= 9`
- 输入数据保证链表代表的数字无前导 0

 

**进阶：**如果输入链表不能翻转该如何解决？





## 实现

**思路**

- 在做加减法的时候，肯定是要从权重最低的位开始计算
- 为了模拟这个计算过程，我们需要将链表进行翻转（虽然题目说要求不翻转，但是用栈其实都是一样的逻辑，只是没有了维护指针指向的开销而已）
- 所以在代码中实现了 `reverseList` 函数用来翻转链表，返回值为翻转后的链表头结点





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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if( l1 == nullptr ) {
            return l2;
        }

        if( l2 == nullptr ) {
            return l1;
        }

        // 翻转 l1 和 l2 链表
        ListNode* num1 = reverseList(l1);
        ListNode* num2 = reverseList(l2);

        // 创建一个虚拟头结点 dummy 用来相加结果的链表
        ListNode* dummy = new ListNode(-1, nullptr);
        // cur1 和 cur2 分别在 num1 和 num2 链表上滑动
        ListNode* cur1 = num1;
        ListNode* cur2 = num2;

        // 用来表示下一轮的进位上的值
        int carry = 0;

        // carry != 0 表示 如果最后一次相加还产生了进位 还是要继续添加节点
        while( cur1 != nullptr || cur2 != nullptr || carry != 0 ) {
            if( cur1 != nullptr ) {
                carry += cur1->val;
                cur1 = cur1->next;
            }

            if( cur2 != nullptr ) {
                carry += cur2->val;
                cur2 = cur2->next;
            }

            // carry % 10 为当前位置的值
            // carry / 10 为下一位的进位值
            ListNode* newNode = new ListNode( carry % 10, dummy->next);
            dummy->next = newNode;

            carry = carry / 10;
        }

        ListNode* res = dummy->next;
        delete dummy;

        return res;
    }
    
    // 翻转非空链表
    ListNode* reverseList(ListNode* head) {
        ListNode* dummy = new ListNode(-1, head);

        ListNode* pre = dummy;
        ListNode* cur = head;

        while( cur != nullptr ) {
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }

        dummy->next->next = nullptr;

        delete dummy;
        return pre;
    }
};
```


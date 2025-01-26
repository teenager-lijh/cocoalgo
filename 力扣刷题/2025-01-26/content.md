# 「每日一题」力扣 83 删除排序链表中的重复元素

你好啊，我是蓝莓，今天是每日一题的第 35 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[83 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/)





## 题目描述

给定一个已排序的链表的头 `head` ， *删除所有重复的元素，使每个元素只出现一次* 。返回 *已排序的链表* 。

 

**示例 1：**

![img](content.assets/list1.jpg)

```
输入：head = [1,1,2]
输出：[1,2]
```

**示例 2：**

![img](content.assets/list2.jpg)

```
输入：head = [1,1,2,3,3]
输出：[1,2,3]
```

 

**提示：**

- 链表中节点数目在范围 `[0, 300]` 内
- `-100 <= Node.val <= 100`
- 题目数据保证链表已经按升序 **排列**





## 实现

**思路**

- 题目已经保证了链表中存储的元素是按照升序排列的
- （1）使用 `pre` 指向当前遍历的节点的前一个
- （2）使用 `cur` 只想当前正在遍历的节点，如果 `cur` 节点的值和 `pre` 节点的值是一样的，那么就从链表中删除 `cur` 节点，并修改 `pre` 节点的 `next` 指针，否则说明当前节点是不重复的





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
    ListNode* deleteDuplicates(ListNode* head) {

        if( head == nullptr ) {
            return head;
        }

        ListNode* pre = head;
        ListNode* cur = head->next;

        while( cur != nullptr ) {
            if( pre->val == cur->val ) {
                pre->next = cur->next;
                cur = pre->next;
            } else {
                pre = cur;
                cur = cur->next;
            }
        }

        return head;
    }
};
```


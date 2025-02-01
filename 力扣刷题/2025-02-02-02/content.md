# 「每日一题」力扣 148 排序链表

你好啊，我是蓝莓，今天是每日一题的第 46 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[148 排序链表](https://leetcode.cn/problems/sort-list/description/)





## 题目描述

给你链表的头结点 `head` ，请将其按 **升序** 排列并返回 **排序后的链表** 。



 

**示例 1：**

![img](content.assets/sort_list_1.jpg)

```
输入：head = [4,2,1,3]
输出：[1,2,3,4]
```

**示例 2：**

![img](content.assets/sort_list_2.jpg)

```
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
```

**示例 3：**

```
输入：head = []
输出：[]
```

 

**提示：**

- 链表中节点的数目在范围 `[0, 5 * 104]` 内
- `-105 <= Node.val <= 105`

 

**进阶：**你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？





## 实现

**思路**

- 对于 **147 对链表进行插入排序** 题目，按照要求我们直接在链表上使用了插入排序
- 但是对于当前这个题目而言，插入排序的时间复杂度是 `O(N^2)` 级别的时间复杂度 不满足要求
- 相对来说，常见的排序算法，如 `快速排序`、`归并排序` 来讲，`归并排序` 是更适合在 链表上使用的
- 接下来就看一下，如何在链表作为数据结构的基础上实现归并排序
- 归并排序有两种实现方式
- （1）自顶向下的递归方式来实现
- （2）自底向上的方式来实现
- 在这篇文章中，我们来看看自底向上的方式怎么实现，主要有这么几方面实现的要点
- （1）自底向上的实现过程中需要明确从每一次归并的两个子链表的长度是多大？对于每一个将要归并的链表而言，它们必须是有序的才能被正确归并，所以 `subSize` 的大小应该是从 `1` 开始，也就是第一轮归并过程中，我们把相邻的每个元素看成一个单独的链表，归并成长度为 `2` 的链表；但是 `subSize` 最大应该增长到多少就要停止了 ？可以想象一下，如果一个链表的长度为 `n` 那么我们从中间切一刀，如果 `subSize` 刚好是 `n/2` 的话，那么我们只需要再归并一次就行了，但是 `subSize` 每次都是成倍增长的，可能不会刚好增长到 `n/2`，或许上一次的 `subSize = 2n/5` 那么下一次的 `subSize` 就等于 `4n/5` ； 所以 `subSize` 如果一旦大于等于 `n` ，那么就一定已经完成归并了；记住 `subSize` 指的是归并的两个链表中的单个链表的长度，所以归并的元素最大的量是 `2subSize`
- （2）所以非常明确，应该有一层循环来处理每一轮归并过程中 `subSize` 的增长变化
- （3）在每一轮的 `subSize` 确定后，我们如何归并？重要的是如何一步一步的找到所有成对出现的相邻的长度为 `subSize` 的链表；在这里我们使用 `head1` 来指向需要归并的第一个链表的头，使用 `head2` 来指向需要归并的第二个链表的头；使用 `cur` 来遍历整个大的链表，很容易我们可以知道 `head1` 就是 `cur` 还没有移动时所指向的节点，所以我们一开始就能确定第一组的 `head1` 是谁了。这时候我们让 `cur` 向后移动 `subSize` 个节点，我们通过 `cur` 节点的前一个节点 `pre` 可以知道 `head1` 链表的最后一个节点是谁，为了方便，我们让 `head1` 最后一个节点的 `next` 指向 `nullptr` ，而且此时 `cur` 指向的正是 `head2` 这个节点；接着我们再让 `cur` 移动 `subSize` 个节点，使用同样的方法，`pre` 指向的正是 `head2` 的最后一个节点，我们也让 `head2` 的最后一个节点指向 `nullptr` ；最后我们写一个 `merge` 函数来归并这两个链表就行了；
- （4）在归并链表的时候，我们归并后的链表需要和 `head1` 前面的那部分衔接上，所以我们需要单独记录 `head1` 的前一个节点 `preHead1`
- （5）当我们完成一组归并后，此时的 `preHead1` 和 `pre` 都应该指向归并完成的链表的最后一个节点，因为这个节点正是下一次寻找 `head1` 的前一个节点，而且这个节点也正是 `cur` 当前所指向的节点的前一个节点；完了让链表衔接上，我们还应该让归并完成的链表的最后一个节点指向当前的 `cur` 节点（别忘了，我们之前为了 merge 过程的方便给人家改成指向 nullptr 了）；接着我们所有的变量就又回到了最初的定义





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
    ListNode* sortList(ListNode* head) {
        int size = 0;

        for( ListNode* cur = head ; cur != nullptr ; cur = cur->next ) {
            size ++;
        }

        ListNode* dummyHead = new ListNode(-1, head);

        // 当 subSize 大于 size / 2 的时候，只需要再进行最后一轮归并就结束了
        for( int subSize = 1 ; subSize < size ; subSize += subSize ) {
            
            ListNode* pre = dummyHead;
            ListNode* cur = dummyHead->next;

            while( cur != nullptr ) {
                // 每完成一轮循环就要完成一组的归并
                ListNode* preHead1 = pre;
                ListNode* head1 = cur;
                // 跳过前半部分
                for( int i = 0 ; i < subSize && cur != nullptr ; i++ ) {
                    pre = cur;
                    cur = cur->next;
                }
                pre->next = nullptr;  // 截断 head1 链表

                ListNode* head2 = cur;
                // 跳过第二部分
                for( int i = 0 ; i < subSize && cur != nullptr ; i++ ) {
                    pre = cur;
                    cur = cur->next;
                }
                pre->next = nullptr;  // 截断 head2 链表

                // 合并两个链表 pre 指向合并后的链表的最后一个节点
                pre = mergeList(preHead1, head1, head2);
                pre->next = cur;  // 将链表链接在一起
            }
        }

        return dummyHead->next;
    }

    ListNode* mergeList(ListNode* dummyHead, ListNode* head1, ListNode* head2) {
        // 返回 合并后链表的最后一个节点

        ListNode* cur = dummyHead;

        ListNode* cur1 = head1;
        ListNode* cur2 = head2;

        // 一定是有一个链表被先放完的
        while( cur1 != nullptr && cur2 != nullptr ) {
            if( cur1->val < cur2->val) {
                cur->next = cur1;
                cur1 = cur1->next;
            } else {
                cur->next = cur2;
                cur2 = cur2->next;
            }
            cur = cur->next;
        }

        if( cur1 != nullptr ) {
            cur->next = cur1;
        } else if( cur2 != nullptr ) {
            cur->next = cur2;
        }

        while( cur->next != nullptr ) {
            cur = cur->next;
        }

        return cur;
    }
};
```

 
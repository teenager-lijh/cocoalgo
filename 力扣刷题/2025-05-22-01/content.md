# 「每日一题」力扣 103 二叉树的锯齿形层序遍历

你好啊，我是蓝莓，今天是每日一题的第 56 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[103 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/)





## 题目描述

给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
```

**示例 2：**

```
输入：root = [1]
输出：[[1]]
```

**示例 3：**

```
输入：root = []
输出：[]
```

 

**提示：**

- 树中节点数目在范围 `[0, 2000]` 内
- `-100 <= Node.val <= 100`





## 实现

**思路**

- 这个题目和 102 以及 107 题目依然是相似的
- 当前题目的代码，直接沿用了 107 号题目的代码，仅仅在代码最后的交换顺序的部分做出了简单的修改
- 我们依然是先按照正常的广度优先遍历的方式遍历二叉树
- 遍历完成后，我们去改变 `res` 数组中某些层的顺序，从而满足题目的要求





**C++ 代码实现**

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> q;

        if( root == nullptr ) {
            return res;
        }

        int level = 0;
        q.push(root);

        while( !q.empty() ) {
            int size = q.size();
            res.push_back(vector<int>());
            
            for( int i = 0 ; i < size ; i++ ) {
                TreeNode* front = q.front();
                q.pop();
                
                if( front->left ) {
                    q.push(front->left);
                }

                if( front->right ) {
                    q.push(front->right);
                }

                res[level].push_back(front->val);
            }

            ++level;
        }

        for( int i = 1 ; i < level ; i+=2 ) {
            int sz = res[i].size();
            int half = sz / 2;
            for( int j = 0 ; j < half ; j++ ) {
                swap(res[i][j], res[i][sz-j-1]);
            }
        }

        return res;
    }
};
```


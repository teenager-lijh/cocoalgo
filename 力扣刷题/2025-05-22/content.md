# 「每日一题」力扣 107 二叉树的层序遍历 II

你好啊，我是蓝莓，今天是每日一题的第 55 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[107 二叉树的层序遍历 II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/description/)





## 题目描述

给你二叉树的根节点 `root` ，返回其节点值 **自底向上的层序遍历** 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

 

**示例 1：**

![img](content.assets/tree1.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：[[15,7],[9,20],[3]]
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
- `-1000 <= Node.val <= 1000`





## 实现

**思路**

- 这是一个力扣的中等题
- 这是数据结构中的二叉树广度优先基础方法
- 这个题目和 102 号题目是非常相似的
- 在 102 号题目，我们已经知道如何把每二叉树每一层的值给遍历出来了
- 在当前这个题目中，它要求我们按照正常的广度优先遍历的相反的顺序将每一层的节点的值输出
- 那么，我们只需要按照 102 号题目的方法遍历，然后将代码中 res 数组颠倒一下顺序即可





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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
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

        int half = level / 2;
        for( int i = 0 ; i < half ; i++ ) {
            swap(res[i], res[level-i-1]);
        }

        return res;
    }
};
```


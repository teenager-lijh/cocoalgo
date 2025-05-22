# 「每日一题」力扣 199 二叉树的右视图

你好啊，我是蓝莓，今天是每日一题的第 57 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[199 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/description/)





## 题目描述

给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

**示例 1：**

**输入：**root = [1,2,3,null,5,null,4]

**输出：**[1,3,4]

**解释：**

![img](content.assets/tmpd5jn43fs-1.png)

**示例 2：**

**输入：**root = [1,2,3,4,null,null,null,5]

**输出：**[1,3,4,5]

**解释：**

![img](content.assets/tmpkpe40xeh-1.png)

**示例 3：**

**输入：**root = [1,null,3]

**输出：**[1,3]

**示例 4：**

**输入：**root = []

**输出：**[]

 

**提示:**

- 二叉树的节点个数的范围是 `[0,100]`
- `-100 <= Node.val <= 100` 





## 实现

**思路**

- 这个题目和 107 题目依然是相似的
- 当前题目的代码，直接沿用了 107 号题目的代码
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
    vector<int> rightSideView(TreeNode* root) {
        vector<vector<int>> res;
        vector<int> view;
        queue<TreeNode*> q;

        if( root == nullptr ) {
            return view;
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

        for( int i = 0 ; i < res.size() ; i++ ) {
            view.push_back(res[i][res[i].size()-1]);
        }

        return view;
    }
};
```


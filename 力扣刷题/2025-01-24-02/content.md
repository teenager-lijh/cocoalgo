# 「每日一题」力扣 447 回旋镖的数量

你好啊，我是蓝莓，今天是每日一题的第 30 天。

**题目清单**：[一起刷力扣](https://blueberry-universe.cn/lc/index.html)

**引用力扣题目**：[447 回旋镖的数量](https://leetcode.cn/problems/number-of-boomerangs/description/)





## 题目描述

给定平面上 `n` 对 **互不相同** 的点 `points` ，其中 `points[i] = [xi, yi]` 。**回旋镖** 是由点 `(i, j, k)` 表示的元组 ，其中 `i` 和 `j` 之间的欧式距离和 `i` 和 `k` 之间的欧式距离相等（**需要考虑元组的顺序**）。

返回平面上所有回旋镖的数量。

 

**示例 1：**

```
输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
```

**示例 2：**

```
输入：points = [[1,1],[2,2],[3,3]]
输出：2
```

**示例 3：**

```
输入：points = [[1,1]]
输出：0
```

 

**提示：**

- `n == points.length`
- `1 <= n <= 500`
- `points[i].length == 2`
- `-104 <= xi, yi <= 104`
- 所有点都 **互不相同**





## 实现

**思路**

- 在这里要考虑的是对于每一个三元组中的点 `point[i]` 来说，只要我们计算出所有其它的点到这个点的距离然后按照距离对其他所有的点进行归类就可以
- 归类后，我们通过遍历所有不同的距离中收集到的不同的点，我们计算一下，这些点使用排列的方式放在 `j` 和 `k` 的位置有多少种排列的方式
- 如果某类距离中收集到的点的数量为 `k` 那么根据排列的计算方法，我们可以知道有 `k * (k-1)` 中摆放方法





**C++ 代码实现**

```c++
class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        // 对于每一个点 point[i]
        // 计算出其它所有的点到这个点的欧拉距离为 dist 的顶点数量
        vector<unordered_map<int, int>> record(points.size());

        for( int i = 0 ; i < points.size() ; i++ ) {
            for( int j = 0 ; j < points.size() ; j++ ) {
                int dist = distance(points[i], points[j]);
                record[i][dist]++;
            }
        }

        int counter = 0;

        for( int i = 0 ; i < points.size() ; i++ ) {
            for( auto iter = record[i].begin() ; iter != record[i].end() ; iter++ ) {
                int k = iter->second;
                counter += k * (k-1);
            }
        }

        return counter;
    }

    int inline distance(vector<int>& p1, vector<int>& p2) {
        int a = p1[0] - p2[0];
        int b = p1[1] - p2[1];
        return a * a + b * b;
    }
};
```


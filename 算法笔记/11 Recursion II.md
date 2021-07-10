# Recursion II

## [Spiral Order Traverse I](https://app.laicode.io/app/problem/121?plan=3)

>Traverse an N * N 2D array in spiral order clock-wise starting from the top left corner. Return the list of traversal sequence.
>
>**Assumptions**
>
>- The 2D array is not null and has size of N * N where N >= 0
>
>**Examples**
>
>{ {1,  2,  3},
>
> {4,  5,  6},
>
> {7,  8,  9} }
>
>the traversal sequence is [1, 2, 3, 6, 9, 8, 7, 4, 5]

![image-20210710102114862](11 Recursion II.assets/image-20210710102114862.png)



```java
public class Solution {
	public List<Integer> spiral(int[][] matrix) {
        
    }
}
```







## [N Queens](https://app.laicode.io/app/problem/233?plan=3)

>Get all valid ways of putting N Queens on an N * N chessboard so that no two Queens threaten each other.
>
>**Assumptions**
>
>- N > 0
>
>**Return**
>
>- A list of ways of putting the N Queens
>- Each way is represented by a list of the Queen's y index for x indices of 0 to (N - 1)
>
>**Example**
>
>N = 4, there are two ways of putting 4 queens:
>
>[1, 3, 0, 2] --> the Queen on the first row is at y index 1, the Queen on the second row is at y index 3, the Queen on the third row is at y index 0 and the Queen on the fourth row is at y index 2.
>
>[2, 0, 3, 1] --> the Queen on the first row is at y index 2, the Queen on the second row is at y index 0, the Queen on the third row is at y index 3 and the Queen on the fourth row is at y index 1.
>
>N皇后问题，输出的List<Integer> **index表示皇后放的行数，值表示列数**。

![image-20210709214456416](Recursion II.assets/image-20210709214456416.png)

用Recursion DFS来做，分出八层，每层叉出8个叉。每一层决定Qi应该放到哪一行，叉出来的叉表示放到那一列。

所以要用for循环叉出来的叉数调用DFS

**Base case:** The last row is done

**RR:** iff position(i, j) valid, go to the next row 

**Time** = O(8^8 * 8) 优化为O(n!) 第一层n个node, 第二层n - 1个node, 一直到最后所以是n! 

![image-20210709231455179](11 Recursion II.assets/image-20210709231455179.png)

```java
public class NQueens {
    public List<List<Integer>> nqeens(int n) {
        List<List<Integer>> result = new ArrayList<>(); //所有结果汇总
        List<Integer> cur = new ArrayList<>(); //每一次的结果
        helper(n, cur, result);
        return result;
    }
    private void helper(int n, List<Integer> cur, List<List<Integer>> result) {
        if (cur.size() == n) { //base case 
            result.add(new ArrayList<>(cur));
            return;
        }
        for (int i = 0; i < n; i++) { //i 按照recursion tree里是列的位置，先是i = 0, 第0列一直递归下去
            if (valid(cur, i)) { //只有valid的时候才进入recursion tree分支
                cur.add(i);
                helper(n, cur, result); //cur 会自己增加
                cur.remove(cur.size() - 1);
            }
        }
    }
    private boolean valid(List<Integer> cur, int column) {
        int row = cur.size(); //得到当前行
        for (int i = 0; i <  row; i++) { //需要遍历走过的所有行数
            if (cur.get(i) == column || Math.abs(cur.get(i) - column) == row - i) { //cur.get(i) == column 某一行上的值和column同一列不行， 
                return false;
            }
        }
        return true;
    }
}
```







## [Reverse Linked List In Pairs](https://app.laicode.io/app/problem/35?plan=3)





## [String Abbreviation Matching](https://app.laicode.io/app/problem/292?plan=3)







## [Store Number Of Nodes In Left Subtree](https://app.laicode.io/app/problem/646?plan=3)







## [Lowest Common Ancestor I](https://app.laicode.io/app/problem/126?plan=3)





## [Spiral Order Traverse II](https://app.laicode.io/app/problem/122?plan=3)





## [Reverse Binary Tree Upside Down](https://app.laicode.io/app/problem/178?plan=3)
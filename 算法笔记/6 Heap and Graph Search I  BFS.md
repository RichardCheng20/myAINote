# Heap and Graph Search I : BFS 9/1
## K Smallest In Unsorted Array
Find the K smallest numbers in an unsorted integer array A. The returned numbers should be in ascending order.

Assumptions

A is not null
K is >= 0 and smaller than or equal to size of A
Return

an array with size K containing the K smallest numbers in ascending order
Examples

A = {3, 4, 1, 2, 5}, K = 3, the 3 smallest numbers are {1, 2, 3}

- 使用Maxheap maxheap里面放k个元素,遍历array然后和里面k个元素里的最大值比较,比最大值小的就放到maxheap里

```java
public class Solution {
	public int[] kSmallest(int[] array, int k) {
		if (array.length == 0 || k == 0) {
			return new int[0];
		}
		PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(k, new Comparator<Integer>(){
			@Override
			public int compare(Integer a, Integer b) {
				if (a.equals(b)) {
					return 0;
				}
				return a > b ? -1 : 1;
			}
		});
		for (int i = 0; i < array.length; i++) {
			if (i < k) { //先加入k个元素
				maxHeap.offer(array[i]);
			} else if (array[i] < maxHeap.peek()) {
				maxHeap.poll();
				maxHeap.offer(array[i]);
			}
		}
		int[] result = new int[k];
		for (int i = k - 1; i >= 0; i--) {
			result[i] = maxHeap.poll();
		}
		return result;
	}
}
```

## Get Keys In Binary Tree Layer By Layer
Get the list of list of keys in a given binary tree layer by layer. Each layer is represented by a list of keys and the keys are traversed from left to right.

Examples

      		 5
    
     	 /    \
    
    	3        8
      /   \        \
    
     1     4        11

the result is [ [5], [3, 8], [1, 4, 11] ]

Corner Cases

What if the binary tree is null? Return an empty list of list in this case.


```java
public class Solution {
	public List<List<Integer>> layerByLayer(TreeNode root) {
		List<List<Integer>> list = new ArrayList<>();
		if (root == null) {
			return list;
		}
		Queue<TreeNode> queue = new ArrayDeque<>();
		queue.offer(root);
		while (!queue.isEmpty()) {
			List<Integer> curLayer = new ArrayList<>();
			int size = queue.size(); //相当于一个墙 只打印上一层的所有节点
			for (int i = 0; i < size; i++) {
				TreeNode cur = queue.poll();
				curLayer.add(cur.key);
				if (cur.left != null) {
					queue.offer(cur.left);
				}
				if (cur.right != null) {
					queue.offer(cur.right);
				}
			}
			list.add(curLayer);
		}
		return list;
	}
}
```

## Bipartite
Determine if an undirected graph is bipartite. A bipartite graph is one in which the nodes can be divided into two groups such that no nodes have direct edges to other nodes in the same group.

Examples

1  --   2

    /   

3  --   4

is bipartite (1, 3 in group 1 and 2, 4 in group 2).

1  --   2

    /   |

3  --   4

is not bipartite.

Assumptions

The graph is represented by a list of nodes, and the list of nodes is not null.

```java
public class GraphNode {
	public int key;
	public List<GraphNode> neighbors;
	public GraphNode(int key) {
		this.key = key;
		this.neighbors = new ArrayList<GraphNode>();
	}
}

public class Solution {
  public boolean isBipartite(List<GraphNode> graph) {
    // write your solution here
    HashMap<GraphNode, Integer> visited = new HashMap<GraphNode, Integer>();
    // 对于每一个node作为起始点开始遍历
    for (GraphNode node : graph) {
      if (!BFS(node, visited)) { //不是bipatite
        return false;
      }
    }
    return true;
  }
  //BFS来遍历所有的节点,然后0 1来标记颜色
  private boolean BFS(GraphNode node, HashMap<GraphNode, Integer> visited) {
    if (visited.containsKey(node)) {
      return true;
    }
    Queue<GraphNode> queue = new ArrayDeque<GraphNode>();
    queue.offer(node); // 1 先放入第一个node到queue
    visited.put(node, 0); //2 标记为0
    while (!queue.isEmpty()) { //3 bfs遍历条件
      GraphNode cur = queue.poll();
      int curGroup = visited.get(cur);
      int neiGroup = curGroup == 0 ? 1 : 0; //4 标记curGroup和neiGroup
      for (GraphNode nei : cur.neighbors) {
        if (!visited.containsKey(nei)) {
          visited.put(nei, neiGroup);
          queue.offer(nei); 
        } else if (visited.get(nei) != neiGroup) {
          return false;
        }
      }
    }
    return true;
  }
}
```

## Check If Binary Tree Is Completed
 使用bfs遍历,定义一个flag一旦出现没有孩子的时候flag就为true
```java
public class Solution {
	public boolean isCompleted(TreeNode root) {
		if (root == null) {
			return true;
		}
		Queue<TreeNode> queue = new ArrayDeque<TreeNode>();
		queue.offer(root);
		boolean flag = false;
		while (!queue.isEmpty()) {
			TreeNode cur = queue.poll();
			if (cur.left == null) {
				flag = true;
			} else if (flag) {
				return false;
			} else {
				queue.offer(cur.left);
			}

			if (cur.right == null) {
				flag = true;
			} else if (flag) {
				return false;
			} else {
				queue.offer(cur.right);
			}
		}
		return true;
	}
 }
```

## Kth Smallest Number In Sorted Matrix
Given a matrix of size N x M. For each row the elements are sorted in ascending order, and for each column the elements are also sorted in ascending order. Find the Kth smallest number in it.

Assumptions

the matrix is not null, N > 0 and M > 0
K > 0 and K <= N * M
Examples

{ {1,  3,   5,  7},

  {2,  4,   8,   9},

  {3,  5, 11, 15},

  {6,  8, 13, 18} }

the 5th smallest number is 4
the 8th smallest number is 6

-  题目中的矩阵行和列都是递增的, 利用这个特点定义一个visited矩阵,然后遍历某元素右边和下面的元素 然后加入到大小为k的minpq里. 最后取出pq顶部的元素就是最小值. 因为要加入minHeap的元素是矩阵元素,所以要定义cell.

```java
public class Solution {
	public int kthSmallest(int[][] matrix, int k) {
		int rows = matrix.length;
		int columns = matrix[0].length;
		PriorityQueue<Cell> minHeap = new PriorityQueue<Cell>(k, new Comparator<Cell>(){
			@Override
			public int compare(Cell a, Cell b) {
				if (a.value == b.value) {
					return 0;
				}
				return a.value < b.value ? -1 : 1;
			}
		});
		boolean[][] visited = new boolean[rows][columns];
		minHeap.offer(new Cell(0, 0, matrix[0][0]));
		visited[0][0] = true;
		for (int i = 0; i < k - 1; i++) {
			Cell cur = minHeap.poll();
			if (cur.row + 1 < rows && !visited[cur.row + 1][cur.column]) {
				minHeap.offer(new Cell(cur.row + 1, cur.column, maxtrix[cur.row + 1][cur.column]));
				visited[cur.row + 1][column] = true;
			}
			if (cur.column + 1 < columns && !visited[cur.row][cur.column + 1]) {	
				minHeap.offer(new Cell(cur.row, cur.column + 1, maxtrix[row][column + 1]));
				visited[row][column + 1];
			}
		}
		return minHeap.peek().value;
	}
	static class Cell {
		int row;
		int column;
		int value;
		Cell(int row, int column, int value) {
			this.row = row;
			this.column = column;
			this.value = value;
		}
	}
}
```
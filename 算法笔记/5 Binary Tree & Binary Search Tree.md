# Binary Tree & Binary Search Tree

## Pre-order Traversal Of Binary Tree (recursive)
Implement a recursive, pre-order traversal of a given binary tree, return the list of keys of each node in the tree as it is pre-order traversed.

Examples

​        5

​     /    \

   3        8

  /   \        \

1      4        11

Pre-order traversal is [5, 3, 1, 4, 8, 11]

Corner Cases

What if the given binary tree is null? Return an empty list in this case.
How is the binary tree represented?

We use the level order traversal sequence with a special symbol "#" denoting the null node.

For Example:

The sequence [1, 2, 3, #, #, 4] represents the following binary tree:

​	1

  /   \

 2     3

  /

4

```java
public class Solution {
	public 	List<Integer> preOrder(TreeNode root) {
		List<Integer> res = new ArrayList<>();
		helper(root, res);
		return res;
	}
//1. 确定递归函数的参数和返回值：因为要打印出前序遍历节点的数值，所以参数里需要传入List<Integer>再放节点的数值，除了这一点就不需要在处理什么数据了也不需要有返回值，所以递归函数返回类型就是void
	private void helper(TreeNode root, List<Integer> res) {
//2. 确定终止条件：在递归的过程中，如何算是递归结束了呢，当然是当前遍历的节点是空了，那么本层递归就要要结束了，所以如果当前遍历的这个节点是空，就直接return，代码如下：
		if (root == null) {
			return;
		}
//3. 确定单层递归的逻辑：前序遍历是中左右的循序，所以在单层递归的逻辑，是要先取中节点的数值
		res.add(root.key);
		helper(root.left, res);
		helper(root.right, res);
	}
}
```

## In-order Traversal Of Binary Tree (recursive)

```java
public class Solution {
	public List<Integer> inOrder(TreeNode root) {
		List<Integer> res = new ArrayList<>();
		helper(root, res);
		return res;
	}
	private void helper(TreeNode root, List<Integer> res) {
		if (root == null) {
			return;
		}
		helper(root.left, res);
		res.add(root.key);
		helper(root.right, res);
	}
}
```

## Post-order Traversal Of Binary Tree (recursive)

```java
public class Solution {
	public List<Integer> postOrder(TreeNode root) {
		List<Integer> res = new ArrayList<>();
		helper(root, res);
		return res;
	}
	private void helper(TreeNode root, List<Integer> res) {
		if (root == null) {
			return;
		}
		helper(root.left, res);
		helper(root.right, res);
		res.add(root.key);
	}
}
```

## Height of Binary Tree
Find the height of binary tree.

Examples:

​	5

  /    \

3        8

  /   \        \

1      4        11

The height of above binary tree is 3.

How is the binary tree represented?

We use the level order traversal sequence with a special symbol "#" denoting the null node.

For Example:

The sequence [1, 2, 3, #, #, 4] represents the following binary tree:

​	1

  /   \

 2     3

  /

4                

```java
public class Solution {
	public int findHeight(TreeNode root) {
		if (root == null) {
			return 0;
		}
		return Math.max(findHeight(root.left), findHeight(root.right)) + 1;
	}
}
```

## Check If Binary Tree Is Balanced
Check if a given binary tree is balanced. A balanced binary tree is one in which the depths of every node’s left and right subtree differ by at most 1.

Examples

​	5

  /    \

3        8

  /   \        \

1      4        11

is balanced binary tree,

​		5

​	  /

​	3

  /   \

1      4

is not balanced binary tree.

Corner Cases

What if the binary tree is null? Return true in this case.
How is the binary tree represented?

We use the level order traversal sequence with a special symbol "#" denoting the null node.

For Example:

The sequence [1, 2, 3, #, #, 4] represents the following binary tree:

​	1

  /   \

 2     3

  /

4

    - 递归思想 
    - 判断高度差大于一直接返回false, 然后就是左右都必须是balanced去递归

```java
public class Solution {
	public boolean isBalanced(TreeNode root) {
		if (root == null) {
			return true;
		}
		int leftHeight = getHeight(root.left);
		int rightHeight = getHeight(root.right);
		if (Math.abs(leftHeight - rightHeight) > 1) {
			return false;
		}
		return isBalanced(root.left) && isBalanced(root.right);
	}
	private int getHeight(TreeNode root) {
		if (root == null) {
			return 0;
		}
		return Math.max(getHeight(root.left), getHeight(root.right)) + 1;
	}
}
```

## Symmetric Binary Tree
Check if a given binary tree is symmetric.

Examples

      		  5
    
    	  /    \
    
    	3        3
      /   \    /   \
    
    1      4  4      1

is symmetric.

       		 5
    
     	 /    \
    	
    	3        3
      /   \    /   \
    
    1      4  1      4

is not symmetric.

Corner Cases

What if the binary tree is null? Return true in this case.
How is the binary tree represented?



- isSymmetric(left.left, right.right) && isSymmetric(left.right, right.left)

```java
public class Solution {
	public boolean isSymmetric(TreeNode root) {
		if (root == null) {
			return true;
		}
		return isSymmetric(root.left, root.right);
	}
	private boolean isSymmetric(TreeNode left, TreeNode right) {
		if (left == null && right == null) {
			return true;
		} else if (left == null || right == null) {
			return false;
		} else if (left.key != right.key) {
			return false;
		}
        //isSymmetric(left.left, right.right)  左子树左边
        //isSymmetric(left.right, right.left)  左子数右边
		return isSymmetric(left.left, right.right) && isSymmetric(left.right, right.left);
	}
}
```

## Tweaked Identical Binary Trees
Determine whether two given binary trees are identical assuming any number of ‘tweak’s are allowed. A tweak is defined as a swap of the children of one node in the tree.

Examples

     	   5
    
      	/    \
    
    	3        8
      /   \
    
    1      4

and

        5
    
      /    \
    
    8        3
    
           /   \
    
          1     4

the two binary trees are tweaked identical.


```java
public class Solution {
	public boolean isTweakedIdentical(TreeNode one, TreeNode two) {
		if (one == null && two == null) {
			return true;
		} else if (one == null || two == null) {
			return false;
		} else if (one.key != two.key) {
			return false;
		}
		return isTweakedIdentical(one.left, two.left) && isTweakedIdentical(one.right, two.right) ||
		isTweakedIdentical(one.left, two.right) && isTweakedIdentical(one.right, two.left);
	}
}
```

## Is Binary Search Tree Or Not
Determine if a given binary tree is binary search tree.There should no be duplicate keys in binary search tree.

Assumptions

You can assume the keys stored in the binary search tree can not be Integer.MIN_VALUE or Integer.MAX_VALUE.
Corner Cases

What if the binary tree is null? Return true in this case.

- 一个任何 两个所有
- 定义min, max

```java
public class Solution {
  public boolean isBST(TreeNode root) {
    // Write your solution here
    return isBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
  }

  private boolean isBST(TreeNode root, int min, int max) {
    if (root == null) {
      return true;
    }
    if (root.key <= min || root.key >= max) {
      return false;
    }
    return isBST(root.left, min, root.key) && isBST(root.right, root.key, max);
  }
}
```

## Get Keys In Binary Search Tree In Given Range
Get the list of keys in a given binary search tree in a given range[min, max] in ascending order, both min and max are inclusive.

Examples

        5
    
      /    \
    
    3        8

  /   \        \

 1     4        11

get the keys in [2, 5] in ascending order, result is  [3, 4, 5]

Corner Cases

What if there are no keys in the given range? Return an empty list in this case.

```java
public class Solution {
  public List<Integer> getRange(TreeNode root, int min, int max) {
    // Write your solution here
    List<Integer> list = new ArrayList<Integer>();
    getRange(root, min, max, list);
    return list;
  }
  private void getRange(TreeNode root, int min, int max, List<Integer> list) {
    if (root == null) {
      return;
    }
    //注意这三个if还有顺序要求，BST
    if (root.key > min) {
      getRange(root.left, min, max, list);
    }
    if (root.key >= min && root.key <= max) {
      list.add(root.key);
    }
    if (root.key < max) {
      getRange(root.right, min, max, list);
    }
  }
}
```

## Search In Binary Search Tree
Find the target key K in the given binary search tree, return the node that contains the key if K is found, otherwise return null.

Assumptions

There are no duplicate keys in the binary search tree

```java
public class Solution {
	public TreeNode search(TreeNode root, int key) {
		TreeNode cur = root;
		while (cur != null && cur.key != key) {
			cur = key < cur.key ? cur.left : cur.right;
		}
		return cur;
	}
}
```


## Insert In Binary Search Tree
Insert a key in a binary search tree if the binary search tree does not already contain the key. Return the root of the binary search tree. 有就不插入，没有才插入

Assumptions 

There are no duplicate keys in the binary search tree

If the key is already existed in the binary search tree, you do not need to do anything

Examples

       		5
    
     	 /    \
    
    	3        8
      /   \
    
     1     4

insert 11, the tree becomes

       		5
    
     	 /    \
    
    	3        8
      /   \        \
    
     1     4       11

insert 6, the tree becomes

      		5
    
     	 /    \
    
    	3        8
      /   \     /  \
    
     1     4   6    11

```java
public class Solution {
	public TreeNode insert(TreeNode root, int key) {
		if (root == null) {
			return new TreeNode(key);
		}
		TreeNode cur = root;
		while (cur.key != key) {
			if (key < cur.key) {
				if (cur.left == null) {
					cur.left = new TreeNode(key);
				} 
				cur = cur.left;
			} else {
				if (cur.right == null) {
					cur.right = new TreeNode(key);
				}
				cur = cur.right;
			}
		}
		return root;
	}
}
```

## Delete In Binary Search Tree
Delete the target key K in the given binary search tree if the binary search tree contains K. Return the root of the binary search tree.

Find your own way to delete the node from the binary search tree, after deletion the binary search tree's property should be maintained.

Assumptions

There are no duplicate keys in the binary search tree

The smallest larger node is first candidate after deletion

- 比较绕, 递归

  ![image-20210811172820886](5 Binary Tree & Binary Search Tree.assets/image-20210811172820886.png)

```
   		5

 	 /    \

	3        8
  /   \        \

 1     4       11
 
```

```java
public class Solution {
	public TreeNode delete(TreeNode root, int key) {
		if (root == null) {
			return null;
		}
		if (key == root.key) {
			if (root.left == null) {
				return root.right; //1 左边为空
			} else if (root.right == null) {
				return root.left; // 2 右边为空
			} else if (root.right.left == null) {// 3 右边的左孩子为空
				root.right.left = root.left; 
				return root.right;
			} else { //右边的左孩子不为空,找root右边树的最小值作为new root，冒泡到上面来作为新的root放到中间位置接上被删的root连接的东西才能满足BST
				TreeNode newRoot = rightSmallest(root.right);
				newRoot.left = root.left;
				newRoot.right = root.right;
				return newRoot;
			} 
			if (key < root.key) {
				root.left = delete(root.left, key); //注意这里有等号赋值，表示的是root.left即root的左边直接用递归函数返回值接管了
			} else if (key > root.key) {
				root.right = delete(root.right, key);
			}
			return root;
		}
		private TreeNode rightSmallest(TreeNode root) {
			while (root.left.left != null) {
				root = root.left;
			}
			TreeNode smallest = root.left;
			root.left = root.left.right;
			return smallest;
		}
	}
}
```

## BFS层序遍历

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
			int size = queue.size();
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





## Pre-order Traversal Of Binary Tree (iterative)

Implement an iterative, pre-order traversal of a given binary tree, return the list of keys of each node in the tree as it is pre-order traversed.

Examples

      		5
    
     	 /    \
    
    	3        8
      /   \        \
    
    1      4        11

Pre-order traversal is [5, 3, 1, 4, 8, 11]

Corner Cases

What if the given binary tree is null? Return an empty list in this case.

![image-20210811173818910](5 Binary Tree & Binary Search Tree.assets/image-20210811173818910.png)

```java
public class Solution {
	public List<Integer> preOrder(TreeNode root) {
		List<Integer> preOrder = new ArrayList<Integer>();
		if (root == null) {
			return preOrder;
		}
		Deque<TreeNode> stack = new LinkedList<TreeNode>();
		stack.offerFirst(root);
		while (!stack.isEmpty()) { //用stack来做,循环条件stack不为空
			TreeNode cur = stack.pollFirst();
			//由于stack是后进先出,所以需要先加入右边然后再加左边到stack里
			if (cur.right != null) {
				stack.offerFirst(cur.right);
			}
			if (cur.left != null) {
				stack.offerFirst(cur.left);
			}
			preOrder.add(cur.key);
		}
		return preOrder;
	}
}
```


## In-order Traversal Of Binary Tree (iterative)

```java
public class Solution {
	public List<Integer> inOrder(TreeNode root) {
		List<Integer> inorder = new ArrayList<Integer>();
		Deque<TreeNode> stack = new LinkedList<TreeNode>();
		TreeNode cur = root;
		while (cur != null || !stack.isEmpty()) {
			if (cur != null) { //只要cur不为空,统统把左边的加到stack
				stack.offerFirst(cur);
				cur = cur.left;
			} else {
				cur = stack.pollFirst(); //cur 为空后就从stack里面取出来放到inorder里
				inorder.add(cur.key);
				cur = cur.right; //然后就把cur的右边遍历
			}
		}
		return inorder;
	}
}
```

## Post-order Traversal Of Binary Tree (iterative)
		  5 
		/ 	 \
	   3	  8

postorder result [3, 8, 5]
如果我能得到[5, 8, 3] 然后reverse一下就好了
[5, 8, 3] 由之前的preorder可以试一下, 只是这一次先加左边的

```java
public class Solution {
	public List<Integer> postOrder(TreeNode root) {
		List<Integer> result = new ArrayList<Integer>();
		Deque<TreeNode> preorder = new LinkedList<TreeNode>();
		if (root == null) {
			return result;
		}
		preorder.offerFirst(root);
		while (!preorder.isEmpty()) {
			TreeNode cur = preorder.pollFirst(); //5 
			result.add(cur.key); //res = [5, 
			if (cur.left != null) {
				preorder.offerFirst(cur.left); //preorder = [3, 
			}
			if (cur.right != null) {
				preorder.offerFirst(cur.right);//preorder = [3, 8
			}
		}
	  Collections.reverse(result);
	  return result;
	}
}
```

-------------------------



**如果父节点的数组下表是i，那么它的左孩子就是i \* 2 + 1，右孩子就是 i \* 2 + 2。**

# **递归三要素**

1. **确定递归函数的参数和返回值：** 确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。
2. **确定终止条件base case：** 写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出。
3. **确定单层递归的逻辑recursion rule：** 确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。





#### [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)

    输入：
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    
     输出：
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
1. 递归前序遍历：

```java
public TreeNode invertTree(TreeNode root) {
     if (root == null) {
         return null; //base case
     }
     //使用先序or后序遍历的模板
     swapChildren(root);
     invertTree(root.left);
     invertTree(root.right);
     return root;
}
private void swapChildren(TreeNode root) {
    TreeNode temp = root.left;
    root.left = root.right;
    root.right = temp;
}
```

2. 迭代前序遍历 参考前序遍历后写出来

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        Deque<TreeNode> stack = new LinkedList<>();
        if (root == null) {
            return null;
        }
        stack.offerFirst(root);
        while(!stack.isEmpty()) {
            TreeNode cur = stack.pollFirst();
            if (cur != null) {//前序遍历
                if (cur.right != null) {
                    stack.offerFirst(cur.right);//右
                }
                if (cur.left != null) {
                    stack.offerFirst(cur.left);//左
                }
                stack.offerFirst(cur); //中
                stack.offerFirst(null);
            } else {//开始反转
                //stack.pollFirst(); //Java中offer了null值但是取的时候不能取到null而是第一个数，和C++不同
                cur = stack.pollFirst();
                swapChild(cur);
            }
        }
        return root;
    }
    private void swapChild(TreeNode root) {
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
    }
}
```

3. BFS解决

   也就是层序遍历，层数遍历也是可以翻转这棵树的，因为层序遍历也可以把每个节点的左右孩子都翻转一遍，代码如下：

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        Queue<TreeNode> queue = new ArrayDeque<>(); // 1. 初始化queue
        queue.offer(root); // 2. 先放入第一个root 
        while(!queue.isEmpty()) { //3. 循环条件queue不为空的时候
            TreeNode cur = queue.poll(); //4. 取出来cur 
            swapChild(cur); //5. 进行操作
            if (cur.left != null) { 
                queue.offer(cur.left);
            }
            if (cur.right != null) {
                queue.offer(cur.right);
            } // 6. 添加左右孩子进来
        }
        return root;
    }
    private void swapChild(TreeNode root) {
        TreeNode temp = root.right;
        root.right = root.left;
        root.left = temp;
    }
}
```



#### [559. N 叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/)

>给定一个 N 叉树，找到其最大深度。
>
>最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
>
>N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
>

![image-20210812120017919](5 Binary Tree & Binary Search Tree.assets/image-20210812120017919.png)

1. 递归

```java
class Solution {
    public int maxDepth(Node root) {
        if (root == null) {
            return 0;
        }
        int depth = 0;
        for (int i = 0; i < root.children.size(); i++) {
            depth = Math.max(depth, maxDepth(root.children.get(i)));
        }
        return depth + 1;
    }
}
```

2. BFS

```JAVA
 public int maxDepth(Node root) {
        if (root == null) {
            return 0;
        }
        int depth = 0;
        Queue<Node> queue = new ArrayDeque<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            depth++;
            int size = queue.size();
            for (int i = 0; i < size; i++) { //横向遍历各个节点
                Node cur = queue.poll();
                if (cur.children != null) {
                    queue.addAll(cur.children);
                }
            }
        }
        return depth;
    }
```

#### [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

>给定一个二叉树，找出其最小深度。
>
>最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

![image-20210812161809765](5 Binary Tree & Binary Search Tree.assets/image-20210812161809765.png)



这就重新审题了，题目中说的是：**最小深度是从根节点到最近叶子节点的最短路径上的节点数量。**，注意是**叶子节点**。

什么是==叶子节点==，左右孩子都为空的节点才是叶子节点！

![image-20210812193850572](5 Binary Tree & Binary Search Tree.assets/image-20210812193850572.png)



- 如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度。

- 反之右子树为空，左子树不为空，最小深度是 1 + 左子树的深度。

- 如果左右子树都不为空，返回左右子树深度最小值 + 1

可以看出：**求二叉树的最小深度和求二叉树的最大深度的差别主要在于处理左右孩子不为空的逻辑。**

1. Recursion

```java
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftDepth = minDepth(root.left);
        int rightDepth = minDepth(root.right);
        if (root.left == null) {
            return rightDepth + 1;
        }
        if (root.right == null) {
            return leftDepth + 1;
        }
        // 左右结点都不为null
        return Math.min(leftDepth, rightDepth) + 1;
    }
}
```

2. BFS

```JAVA
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int depth = 0;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int size = queue.size();
            depth++;
            for (int i = 0; i < size; i++) {
                TreeNode cur = queue.poll();
                if (cur.left == null && cur.right == null) {
                    // 是叶子结点，直接返回depth，因为从上往下遍历，所以该值就是最小值
                    return depth;
                }
                if (cur.left != null) {
                    queue.offer(cur.left);
                }
                if (cur.right != null) {
                    queue.offer(cur.right);
                }
            }

        }
        return depth;
    }
}
```

#### [222. 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes/)

给你一棵**完全二叉树** 的根节点 `root` ，求出该树的节点个数。

![image-20210812210955748](5 Binary Tree & Binary Search Tree.assets/image-20210812210955748.png)

1. Recursion

```java
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0; // base case 
        }
        int leftNum = countNodes(root.left);//left 
        int rightNum = countNodes(root.right);//right 
        int sum = leftNum + rightNum + 1; //middle
        return sum;
    }
}
```

2. BFS 

```Java
class Solution {
   public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        int nodeNum = 0;
        while (!queue.isEmpty()) {
            //List<Integer> curLayer = new ArrayList<>();
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode cur = queue.poll();
               // curLayer.add(cur.val);
                if (cur.left != null) {
                    queue.offer(cur.left);
                }
                if (cur.right != null) {
                    queue.offer(cur.right);
                }
            }
            nodeNum += size;
        }
        return nodeNum;
    }
}
```

#### [257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/)

>给定一个二叉树，返回所有从根节点到叶子节点的路径。
>
>**说明:** 叶子节点是指没有子节点的节点。

```
输入:
   1
 /   \
2     3
 \
  5
输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
```


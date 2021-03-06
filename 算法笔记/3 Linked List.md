# 3 Linked List 8.19
## Reverse Linked List (iterative)
Reverse a singly-linked list iteratively.

Examples

L = null, return null
L = 1 -> null, return 1 -> null
L = 1 -> 2 -> 3 -> null, return 3 -> 2 -> 1 -> null

//time = O(n) space = O(1)

首先定义一个cur指针，指向头结点，再定义一个pre指针，初始化为null。


```java
public class Solution {
// 	1 -> 2 -> 3 -> 4 -> 5
//p c	 n
	public ListNode reverse(ListNode head) {
		ListNode prev = null;
		ListNode curr = head;
		while (curr != null) {
			ListNode next = curr.next; //即是定义又是往后遍历
			curr.next = prev; //从头这里破解
			prev = curr; //先指向cur指向的内容
			curr = next; //然后再移动cur 
		}
		return prev;
	}
}
```

## Reverse Linked List (recursive)
//time = o(n)  space = O(n)

```java
public class Solution {
// 	1 -> 2 -> 3 -> 4 -> 5
//	h	
	public 	ListNode reverse(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		//假设返回了新的头 后面的已经反转好了
		ListNode newHead = reverse(head.next); //程序会一直调用到这结束
		head.next.next = head; //相当于2指向了1
		head.next = null;
		return newHead;
	}
}
```

## Middle Node Of Linked List
Find the middle node of a given linked list.

Examples

L = null, return null
L = 1 -> null, return 1
L = 1 -> 2 -> null, return 1
L = 1 -> 2 -> 3 -> null, return 2
L = 1 -> 2 -> 3 -> 4 -> null, return 2

```java
public class Solution {
	public ListNode middleNode(ListNode head) {
		if (head == null) {
			return head;
		}
		ListNode slow = head;
		ListNode fast = head;
		while (fast.next != null && fast.next.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		return slow;
	}
}
```

## Check If Linked List Has A Cycle
Check if a given linked list has a cycle. Return true if it does, otherwise return false.
Assumption:
You can assume there is no duplicate value appear in the linked list.

```java
public class Solution {
	public boolean hasCycle(ListNode head) {
		if (head == null || head.next == null) {
			return false;
		}
		ListNode slow = head;
		ListNode fast = head;
		while (fast.next != null && fast.next.next != null) {
			slow = slow.next;
			fast = fast.next.next;
			if (slow == fast) {
				return true;
			}
		}
		return false;
	}
}
```

## Insert In Sorted Linked List
Insert a value in a sorted linked list.

Examples

L = null, insert 1, return 1 -> null
L = 1 -> 3 -> 5 -> null, insert 2, return 1 -> 2 -> 3 -> 5 -> null

​     cur

L = 1 -> 3 -> 5 -> null, insert 3, return 1 -> 3 -> 3 -> 5 -> null
L = 2 -> 3 -> null, insert 1, return 1 -> 2 -> 3 -> null

```java
public class Solution {
	public ListNode insert(ListNode head, int value) {
		ListNode newNode = new ListNode(value); // 1 先创建好ListNode
		if (head == null || head.value >= value) {
			newNode.next = head;
			return newNode;
		}
		//不能失去对头的控制
		ListNode cur = head;
		while (cur.next != null && cur.next.value < value) {
			cur = cur.next; //这里一直遍历到下一个元素比我这个value大
		}
		//将newNode插入到cur.next的前一个
		newNode.next = cur.next;
		cur.next = newNode;
		return head;
	}
}
```

## Merge Two Sorted Linked Lists
>Merge two sorted lists into one large sorted list.
>
>Examples
>
>L1 = 1 -> 4 -> 6 -> null, L2 = 2 -> 5 -> null, merge L1 and L2 to 1 -> 2 -> 4 -> 5 -> 6 -> null
>L1 = null, L2 = 1 -> 2 -> null, merge L1 and L2 to 1 -> 2 -> null
>L1 = null, L2 = null, merge L1 and L2 to null

```java
public class Solution {
  public ListNode merge(ListNode one, ListNode two) {
    // Write your solution here
    ListNode dummy = new ListNode(0);
    ListNode cur = dummy;
    ListNode cur1 = one;
    ListNode cur2 = two;
    while (cur1 != null && cur2 != null) {
      if (cur1.value < cur2.value) {
        cur.next = cur1;
        cur = cur.next;
        cur1 = cur1.next;
      } else {
        cur.next = cur2;
        cur = cur.next;
        cur2 = cur2.next;
      }
    }
    if (cur1 != null) {
      cur.next = cur1;
      /cur1 = cur1.next;
    }
    if (cur2 != null) {
			cur.next = cur2;
	}
    return dummy.next;
  }
}
```
#### [23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

```java
class Solution {
   public ListNode mergeKLists(ListNode[] lists) {
        ListNode res = null;
        for(ListNode list : lists) {
            res = mergeTwoList(res, list);
        }
        return res;
    }
    private ListNode mergeTwoList(ListNode one, ListNode two) {
        if (one == null) {
            return two;
        }
        if (two == null) {
            return one;
        }
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        ListNode cur1 = one;
        ListNode cur2 = two;
        while (cur1 != null && cur2 != null) {
            if (cur1.val < cur2.val) {
                cur.next = cur1;
                cur = cur.next;
                cur1 = cur1.next;
            } else {
                cur.next = cur2;
                cur = cur.next;
                cur2 = cur2.next;
            }
        }
        if (cur1 != null) {
            cur.next = cur1;
        }
        if (cur2 != null) {
            cur.next = cur2;
        }
        return dummy.next;
    }
}    
/////
方法二 
O(n∗log(k))，n 是所有链表中元素的总和，k 是链表个数。
class Solution {
   public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        PriorityQueue<ListNode> queue = new PriorityQueue<>(lists.length, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                if (o1.val < o2.val) return -1;
                else if (o1.val == o2.val) return 0;
                else return 1;
            }
        });
        ListNode dummy = new ListNode(0);
        ListNode p = dummy;
        for (ListNode node : lists) {
            if (node != null) queue.add(node);
        }
        while (!queue.isEmpty()) {
            p.next = queue.poll();
            p = p.next;
            if (p.next != null) queue.add(p.next);
        }
        return dummy.next;
    }
}

作者：powcai
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/leetcode-23-he-bing-kge-pai-xu-lian-biao-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```







## 41. ReOrder Linked List

Reorder the given singly-linked list N1 -> N2 -> N3 -> N4 -> … -> Nn -> null to be N1- > Nn -> N2 -> Nn-1 -> N3 -> Nn-2 -> … -> null

Examples
L = null, is reordered to null
L = 1 -> null, is reordered to 1 -> null
L = 1 -> 2 -> 3 -> 4 -> null, is reordered to 1 -> 4 -> 2 -> 3 -> null
L = 1 -> 2 -> 3 -> null, is reordred to 1 -> 3 -> 2 -> null

 1 -> 2 -> 3 -> 4 -> null
 4 -> 3 -> 2 -> 1 -> null
关键问题就是找到中点然后反转一半之后merge

 

```java
public class Solution {
	public ListNode reorder(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		ListNode middle = findMiddle(head);
		ListNode one = head; //前一半
		ListNode two = middle.next;
		middle.next = null; //后一半
		ListNode halfReverse = reverse(two);
		return merge(one, halfReverse);
	}
	private ListNode findMiddle(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		ListNode slow = head;
		ListNode fast = head;
		while (fast.next != null && fast.next.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		return slow;
	}
	private ListNode reverse(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		//  1 2 3 4 5 
		//p h n 
		ListNode prev = null;
		while (head != null) {
			ListNode next = head.next;//next一定在while里
			head.next = prev; //到这就反转好了
			prev = head;
			head = next;
		}
		return prev;
	}
	private ListNode merge(ListNode one, ListNode two) {
		ListNode dummy = new ListNode(0);
		ListNode cur = dummy;//将dummy给cur!!!
		while (one != null && two != null) {
			cur.next = one;
			one = one.next;
			cur = cur.next;
			cur.next = two;
			two = two.next;
			cur = cur.next;
		}
		if (one != null) {
			cur.next = one;
		}
		if (two != null) {
			cur.next = two;
		}
		return dummy.next;
	}
 }
```

## Partition Linked List
Given a linked list and a target value T, partition it such that all nodes less than T are listed before the nodes larger than or equal to target value T. The original relative order of the nodes in each of the two partitions should be preserved.

Examples

L = 2 -> 4 -> 3 -> 5 -> 1 -> null, T = 3, is partitioned to 2 -> 1 -> 4 -> 3 -> 5 -> null

curSmall 2 -> 1 

curLarge 4 -> 3 -> 5 

-  根据和target的大小分成两个linkedlist

```java
public class Solution {
 // 2 -> 4 -> 3 -> 5 -> 1
 // h
 // 
	public ListNode partition(ListNode head, int target) {
		if (head == null || head.next == null) {
			return head;
		}
		ListNode small = new ListNode(0);
		ListNode large = new ListNode(0);
		ListNode curSmall = small;
		ListNode curLarge = large;
		while (head != null) {
			if (head.value < target) {
				curSmall.next = head;
				curSmall = curSmall.next;
			} else {
				curLarge.next = head;
				curLarge = curLarge.next;
			}
			head = head.next;
		}
		curSmall.next = large.next;
		curLarge.next = null;
		return small.next;
	}
}
```

## Merge Sort Linked List
Given a singly-linked list, where each node contains an integer value, sort it in ascending order. The merge sort algorithm should be used to solve this problem.

Examples

null, is sorted to null
1 -> null, is sorted to 1 -> null
1 -> 2 -> 3 -> null, is sorted to 1 -> 2 -> 3 -> null
4 -> 2 -> 6 -> -3 -> 5 -> null, is sorted to -3 -> 2 -> 4 -> 5 -> 6

- mergesort核心: 分两半 然后两边sort好后merge basecase就是只有一个元素的时候

```java
public class Solution {
	public ListNode mergeSort(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		ListNode middle = findMiddle(head); //先找到中点
		ListNode middleNext = middle.next;
		middle.next = null;
		ListNode left = mergeSort(head);
		ListNode right = mergeSort(middleNext);//假设两边都已经sort好了
		return merge(left, right);		
	}
	private ListNode findMiddle(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		ListNode slow = head;
		ListNode fast = head;
		while (fast.next != null && fast.next.next != null) {
			slow = slow.next;
			fast = fast.next;
		}
		return slow;
	}
	//谁小移谁
	private ListNode merge(ListNode one, ListNode two) {
		ListNode dummy = new ListNode(0);
		ListNode cur = dummy;
		while (one != null && two != null) {
			if (one.value <= two.value) {
				cur.next = one;
				one = one.next;
			} else {
				cur.next = two;
				two = two.next;
			}
			cur = cur.next;
		}
		if (one != null) {
			cur.next = one;
		} else {
			cur.next = two;
		}
		return dummy.next;
	}
}
```

## Add Two Numbers
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.  

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

2 -> 4 -> 3
5 -> 6 -> 4
7 -> 0 -> 8

- 需要一个进位变量val,进位表示为val / 10, 相加的和为 val % 10

```java
public class Solution {
	public ListNode addTwoNumbers(ListNode a, ListNode b) {
		ListNode dummy = new ListNode(0);
		ListNode cur = dummy;
		int val = 0;
		while(a != null || b != null || val != 0) {
			if (a != null) {
				val += a.value;
				a = a.next;
			} 
			if (b != null) {
				val += b.value;
				b = b.next;
			}
			cur.next = new ListNode(val % 10);
			val = val / 10; //进位
			cur = cur.next;
		}
		return dummy.next;
	}
}
```

## Check If Linked List Is Palindrome
Given a linked list, check whether it is a palindrome.

Examples:

Input:   1 -> 2 -> 3 -> 2 -> 1 -> null

output: true.

Input:   1 -> 2 -> 3 -> null  

output: false.

Requirements:

Space complexity must be O(1)

- 找到中点反转后半部分, 然后撸一遍比较

```java
public class Solution {
	public boolean isPalindrome(ListNode head) {
		if (head == null || head.next == null) {
			return true;
		}
		ListNode middle = findmiddle(head);
		ListNode righthalf = reverse(middle.next);
		while(head != null && righthalf != null) {
			if (head.value != righthalf.value) {
				return false;
			}
			head = head.next;
			righthalf = righthalf.next;
		}
		return true;
	}
	private ListNode findmiddle(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		ListNode slow = head;
		ListNode fast = head.next;
		while (fast.next != null && fast.next.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		return slow;
	}
	private ListNode reverse(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}
		//  1 -> 2 -> 3 -> null  
		//p	h    n 
		ListNode prev = null;
		while (head != null) {
			ListNode next = head.next; //next定义于while里
			head.next = prev; //反转
			prev = head;
			head = next; //往后遍历
		}
		return prev;
	}
 }
```

## Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

-直接撸一遍,需要dummyhead
1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6
		p		h

```java
public class Solution {
	public ListNode removeElements(ListNode head, int val) {
		ListNode dummy = new ListNode(0);
		ListNode prev = dummy;
    dummy.next = head;
		while (head != null) {
			if (head.value == val) {
				prev.next = head.next; //相等满足条件 直接将head去掉
			} else {
				prev = head;
			}
			head = head.next;
		}
		return dummy.next;
	}
}
```

#### [707. 设计链表](https://leetcode-cn.com/problems/design-linked-list/)

```java
 //单链表
class ListNode {
       int val;
       ListNode next;
       ListNode() {}
       ListNode (int val) {
           this.val = val;
       }
    }
class MyLinkedList {

    /** Initialize your data structure here. */
    int size;//size存储链表元素的个数
    ListNode head; //虚拟头结点

    //初始化链表
    public MyLinkedList() {
        size = 0;
        head = new ListNode(0);
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        ListNode currentNode = head;
        //包含一个虚拟头节点，所以查找第 index+1 个节点
        for (int i = 0; i <= index; i++) {
            currentNode = currentNode.next;
        }
        return currentNode.val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        if (index > size) {
            return;
        }
        if (index < 0) {
            index = 0;
        }
        size++;
        ListNode pred = head;
        for (int i = 0; i < index; i++) {
            pred = pred.next;
        }
        ListNode toAdd = new ListNode(val);
        toAdd.next = pred.next;
        pred.next = toAdd;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        size--;
        ListNode pre = head;
        for (int i = 0; i < index; i++) {
            pre = pre.next;
        }
        pre.next = pre.next.next;
    }
}
```

#### [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

>给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。**你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。

![image-20210821135049765](3 Linked List.assets/image-20210821135049765.png)

```
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head; //base case
        }
        ListNode next = head.next;
        ListNode newNode = swapPairs(next.next); //rule 
        
        // 这里进行交换
        next.next = head;
        head.next = newNode;
        return next;
    }
}
```

#### [19. 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

>给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。
>
>**进阶：**你能尝试使用一趟扫描实现吗？
>
>![image-20210821193818616](3 Linked List.assets/image-20210821193818616.png)

让fast先走完n步，然后一样的速度slow再开始走，这样能确保slow和fast之间的距离就是要删掉的倒数距离，直到fast为空，这个时候slow的下个节点就是要被删除的节点。 

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        ListNode slow = dummy;
        ListNode fast = dummy;
        dummy.next = head;
        for (int i = 0; i <= n ; i++) { //fast先跑一段n
            fast = fast.next;
        }
        while (fast != null) { //有了间隔，slow, fast都一起跑
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next; //删除节点
        return dummy.next;
    }
}
```

#### [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

>给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 `null`。
>
>![image-20210821200047264](3 Linked List.assets/image-20210821200047264.png)

假设从头结点到环形入口节点 的节点数为x。 环形入口节点到 fast指针与slow指针相遇节点 节点数为y。 从相遇节点 再到环形入口节点节点数为 z。 如图所示：

![image-20210821200915023](3 Linked List.assets/image-20210821200915023.png)

相遇时： slow指针走过的节点数为: `x + y`， fast指针走过的节点数：` x + y + n (y + z)`，n为fast指针在环内走了n圈才遇到slow指针，（y+z）为 一圈内节点的个数A。

 fast指针走过的节点数 = slow指针走过的节点数 * 2：`(x + y) * 2 = x + y + n (y + z)`

要找环形的入口: `x = (n - 1) (y + z) + z`

先拿n为1的情况来举例，意味着fast指针在环形里转了一圈之后，就遇到了 slow指针了。

公式就化解为 `x = z`，这就意味着，**从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 那么当这两个指针相遇的时候就是 环形入口的节点**。

也就是在相遇节点处，定义一个指针index1，在头结点处定一个指针index2。

让index1和index2同时移动，每次移动一个节点， 那么他们相遇的地方就是 环形入口的节点。

```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {// 有环
                ListNode index1 = fast;
                ListNode index2 = head;
                while (index1 != index2) {
                    index1 = index1.next;
                    index2 = index2.next;
                }
                return index1;
            }
        }
        return null;
    }
}
```

#### [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)

![image-20220124154205581](3%20Linked%20List.assets/image-20220124154205581.png)

![image-20220124154316535](3%20Linked%20List.assets/image-20220124154316535.png)

```java
class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        slow = nums[slow];
        fast = nums[nums[fast]];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        int pre1 = 0; 
        int pre2 = slow;
        while (pre1 != pre2) {
            pre1 = nums[pre1];
            pre2 = nums[pre2];
        }
        return pre1;
    }
}
```



#### [160. 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)

![image-20220120093538670](3%20Linked%20List.assets/image-20220120093538670.png)

![image-20220120093503297](3%20Linked%20List.assets/image-20220120093503297.png)

```java
//方法一 使用hashSet
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> visited = new HashSet<ListNode>(); //listNode前后节点不一样的时候是不一样的
        ListNode dumA = headA;
        while (dumA != null) {
            visited.add(dumA);
            dumA = dumA.next;
        }
        ListNode dumB = headB;
        while(dumB != null) {
            if (visited.contains(dumB)) {
                return dumB;
            }
            dumB = dumB.next;
        }
        return null;
    }
}
////// 方法二 //////////
双指针
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pA = headA;
        ListNode pB = headB;
        if (headA == null || headB == null) {
            return null;
        }
        while (pA != pB) {
            pA = pA == null ? headB : pA.next;
            pB = pB == null ? headA : pB.next;
        }
        return pA;
    }
}
```

#### [82. 删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)

![image-20220315230803689](3%20Linked%20List.assets/image-20220315230803689.png)

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }
        
        ListNode dummy = new ListNode(0, head);

        ListNode cur = dummy;
        while (cur.next != null && cur.next.next != null) {
            if (cur.next.val == cur.next.next.val) {
                int x = cur.next.val;//关键 记录下下一个元素的值
                while (cur.next != null && cur.next.val == x) {
                    cur.next = cur.next.next;
                }
            } else {
                cur = cur.next;
            }
        }

        return dummy.next;
    }
}
```

#### [86. 分隔链表](https://leetcode-cn.com/problems/partition-list/)

![image-20220318122859493](3%20Linked%20List.assets/image-20220318122859493.png)

```java
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode small = new ListNode(0);
        ListNode smallHead = small;
        ListNode large = new ListNode(0);
        ListNode largeHead = large;
        while (head != null) {
            if (head.val < x) {
                small.next = head;
                small = small.next;
            } else {
                large.next = head;
                large = large.next;
            }
            head = head.next;
        }
        large.next = null;
        small.next = largeHead.next;
        return smallHead.next;
    }
}
```

#### [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

![image-20220330170559606](3 Linked List.assets/image-20220330170559606.png)

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || head.next == null) {
            return head;
        }
        int count = 0;
        ListNode cur = head;
        while (cur != null && count != k) {
            cur = cur.next;
            count++;
        }
        if (count == k) {
            cur = reverseKGroup(cur, k);
            while (count-- > 0) {
                ListNode temp = head.next;
                head.next = cur;
                cur = head;
                head = temp;
            }
            head = cur;
        }
        return head;
    }
}
```


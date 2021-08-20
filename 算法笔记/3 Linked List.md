# 3 Linked List 8.19
## Reverse Linked List (iterative)
Reverse a singly-linked list iteratively.

Examples

L = null, return null
L = 1 -> null, return 1 -> null
L = 1 -> 2 -> 3 -> null, return 3 -> 2 -> 1 -> null

//time = O(n) space = O(1)


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
			prev = curr;
			curr = next;
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
		while (fast != null && fast.next.next != null) {
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
		while (fast != null && fast.next != null) {
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








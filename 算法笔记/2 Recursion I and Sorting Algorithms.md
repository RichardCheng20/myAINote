# 2 Recursion I and Sorting Algorithms
## 624. Fibonacci Number Lite
Get the Kth number in the Fibonacci Sequence. (K is 0-indexed, the 0th Fibonacci number is 0 and the 1st Fibonacci number is 1).
Examples
0th fibonacci number is 0
1st fibonacci number is 1
2nd fibonacci number is 1
3rd fibonacci number is 2
6th fibonacci number is 8
Corner Cases
What if K < 0? in this case, we should always return 0.
Is it possible the result fibonacci number is overflowed? We can assume it will not be overflowed when we solve this problem on this online judge, but we should also know that it is possible to get an overflowed number, and sometimes we will need to use something like BigInteger.

```java
//time = O(2^N)
//space = O(n)
public solution {
	public int fibonacci(int k) {
		if (k <= 0) {
			return 0;
		} 
		if (k == 1) {
			return 1;
		}
		return fibonacci(k - 1) + fibonacci(k - 2);
	}
}
```
## 13. a to the power of b
Evaluate a to the power of b, assuming both a and b are integers and b is non-negative.
Examples
power(2, 0) = 1
power(2, 3) = 8
power(0, 10) = 0
power(-2, 5) = -32
Corner Cases
In this question, we assume 0^0 = 1.
What if the result is overflowed? We can assume the result will not be overflowed when we solve this problem on this online judge.

```java
public class Solution {
  public long power(int a, int b) {
  	if (a == 0) {
  		return 0;
  	}
  	if (b == 0) {
  		return 1;
  	}
  	long half = power(a, b/2);
  	return b % 2 == 0 ? half * half : half * half * a;
  }
}
```
## 4. Selection Sort
Given an array of integers, sort the elements in the array in ascending order. The selection sort algorithm should be used to solve this problem.
Examples
{1} is sorted to {1}
{1, 2, 3} is sorted to {1, 2, 3}
{3, 2, 1} is sorted to {1, 2, 3}
{4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
Corner Cases
What if the given array is null? In this case, we do not need to do anything.
What if the given array is of length zero? In this case, we do not need to do anything.
//space O(1) time = O(N^2)
N 个元素做n 轮,选出剩余没有排序的最小值
i作为**遍历数组**的起始位置,i之前都是排好序的
min用于和i交换,是最小元素的index
j用来遍历还没有参与比较的元素
-1 -3 7 4 
-3 -1 7 4 
i
	j
m 

```java
public class Solution {
	public int[] solve(int[] array) {
		if (array == null || array.length <= 1) {
			return array;
		}
		for(int i = 0; i < array.length - 1; i++) {
			int min = i;
			for(int j = i + 1; j < array.length; j++) {
				if (array[j] < array[min]) {
					min = j; //j去找没有遍历里面的最小的
				}
			} 
			swap(array, i, min);
		}
		return array;
	}
	private void swap(int[] array, int i, int j) {
		int temp = array[i];
		array[i] = array[j];
		array[j] = temp;
	}
}
```

## 9. Merge Sort
Given an array of integers, sort the elements in the array in ascending order. The merge sort algorithm should be used to solve this problem.

Examples

{1} is sorted to {1}
{1, 2, 3} is sorted to {1, 2, 3}
{3, 2, 1} is sorted to {1, 2, 3}
{4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
Corner Cases

What if the given array is null? In this case, we do not need to do anything.
What if the given array is of length zero? In this case, we do not need to do anything.

//space = O(n) = O(logn) stack+ O(n) heap 	time = O(nlogn) = O(n) + O(nlogn) 

- 数组分两半,然后sort, 然后merge 根据递归,先一直leftResult到底,然后分割到只有一个元素返回,然后调用Rightresult, 最后两个merge. 
- ![image-20211111171059537](2%20Recursion%20I%20and%20Sorting%20Algorithms.assets/image-20211111171059537.png)

```java
public class Solution {
	public int[] mergeSort(int[] array) {
		if (array.length <= 1 || array == null) {
			return array;
		}
		return mergeSort(array, 0, array.length - 1);
	}
	//假设这一部分已经帮我sort好了左右两半 然后就是需要合并merge
	private int[] mergeSort(int[] array, int left, int right) {
		if (left == right) {
			return new int[] {array[left]};
		}
		int mid = left + (right - left) / 2;
		int[] leftResult = mergeSort(array, left, mid);
		int[] rightResult = mergeSort(array, mid + 1, right);
		return merge(leftResult, rightResult);
	}
	//谁小移谁
	private int[] merge(int[] leftResult, int[] rightResult) {
		int leftIndex = 0;
		int rightIndex = 0;
		int resultIndex = 0;
		while (leftIndex < leftResult.length && rightIndex < rightResult.length) {
			if (leftResult[leftIndex] <= rightResult[rightIndex]) {
				result[resultIndex] = leftResult[leftIndex];
				leftIndex++;
			} else {
				result[resultIndex] = rightResult[rightIndex];
				rightIndex++;
			}
			resultIndex++;
		}
		//post processing
		while (leftIndex < leftResult.length) {
			result[resultIndex] = leftResult[leftIndex];
			leftIndex++;
			resultIndex++;
		} 
		while(rightIndex < rightResult.length) {
			result[resultIndex] = rightResult[rightIndex];
			rightIndex++;
			resultIndex++;
		}
		return result;
	}
} 
```
## 10. Quick Sort
Given an array of integers, sort the elements in the array in ascending order. The quick sort algorithm should be used to solve this problem.

Examples

{1} is sorted to {1}
{1, 2, 3} is sorted to {1, 2, 3}
{3, 2, 1} is sorted to {1, 2, 3}
{4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
Corner Cases

What if the given array is null? In this case, we do not need to do anything.
What if the given array is of length zero? In this case, we do not need to do anything.
[0, i) 小于pivot
[i, j]  未知
(j, n - 1] >= pivot
`time` = o(nlogn) space  = O(n)

```java
public class Solution {
	public int[] quickSort(int[] array) {
		if (array == null || array.length == 0) {
			return array;
		}
		quickSort(array, 0, array.length - 1);
		return array;
	}
	public void quickSort(int[] array, int left, int right) {
		if (left > right) {
			return; //和上题目不同的退出条件
		}
		int pivotPos = partition(array, left, right); //左右两半边分开的index
		quickSort(array, left, pivotPos - 1);
		quickSort(array, pivotPos + 1, right);  //两半分别去sort好 ⚠注意少了一个元素
	}
	
	private int partition(int[] array, int left, int right) {
		int pivotIndex = pivotIndex(left, right);
		int pivot = array[pivotIndex];
		swap(array, pivotIndex, right);
		int leftBound = left;
		int rightBound = right - 1; //右边界由于放了pivot 需要再一次减少一
		while (leftBound <= rightBound) {
			if (array[leftBound] < pivot) {
				leftBound++;
			} else if (array[rightBound] >= pivot) {
				rightBound--;
			} else {
				swap(array, leftBound++, rightBound--);
			}
		}
		//swap back the pivot
		swap(array, leftBound, right);
		return leftBound;	
	} 
	private int pivotIndex(int left, int right) {
		return left + (int)(Math.random() * (right - left + 1));
	}
	private void swap(int[] array, int left, int right) {
		int temp = array[left];
		array[left] = array[right];
		array[right] = temp;
	}
}

```
## 258. Move 0s To The End I
Given an array of integers, move all the 0s to the right end of the array.

The relative order of the elements in the original array`does not need` `to be maintained.

Assumptions:

The given array is not null.
Examples:

{1} --> {1}
{1, 0, 3, 0, 1} --> {1, 3, 1, 0, 0} or {1, 1, 3, 0, 0} or {3, 1, 1, 0, 0}

- 使用左右指针向中间逼近

```java
//time = o(n) space = O(1)
public class Solution {
	public int[] moveZero(int[] array) {
		if (array.length == 0 || array == null) {
			return array;
		}
		int left = 0;
		int right = array.length - 1;
		while (left < right) {
			if (array[right] == 0) {
				right--;
			} else if (array[left] != 0) { //!!!!!=
				left++;
			} else {
				swap(array, left, right);//left, right
			}
		} 
		return array;
	}
 	private void swap(int[] array, int left, int right) {
 		int temp = array[left];
 		array[left] = array[right];
 		array[right] = temp;
 	}
}
```
#### [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

![image-20220123234314245](2%20Recursion%20I%20and%20Sorting%20Algorithms.assets/image-20220123234314245.png)

使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。

右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。

注意到以下性质：

**左指针左边均为非零数；**

**右指针左边直到左指针处均为零。**

因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0;
        int right = 0;
        while (right < nums.length) {
            if (nums[right] != 0) {
                swap(nums, right, left);
                left++;
            } 
            right++;
        }
    }
    private void swap(int[] nums, int right, int left) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
}
```

## 11. Rainbow Sort

Given an array of balls, where the color of the balls can only be Red, Green or Blue, sort the balls such that all the Red balls are grouped on the left side, all the Green balls are grouped in the middle and all the Blue balls are grouped on the right side. (Red is denoted by -1, Green is denoted by 0, and Blue is denoted by 1).

Examples

{0} is sorted to {0}
{1, 0} is sorted to {0, 1}
{1, 0, 1, -1, 0} is sorted to {-1, 0, 0, 1, 1}
Assumptions

The input array is not null.
Corner Cases

What if the input array is of length zero? In this case, we should not do anything as well.
 // -1 -1 0 0 $ $ $ 1 1 
 //       	i      j     k


```java
//time = O(n) space = O(1)
public class Solution {
	public int[] rainbowSort(int[] array) {
		if (array == null || array.length <= 1) {
			return array;
		}
		int i = 0;
		int j = 0;
		int k = array.length - 1;
		while (j <= k) {
			if (array[j] == -1) {
				swap(array, i, j);
				i++;
				j++;
			} else if (array[j] == 0) {
				j++;
			} else {
				swap(array, j, k);
				k--;
			}
		}
		return array;
	}
	private void swap(int[] array, int left, int right) {
		int temp = array[left];
		array[left] = array[right];
		array[right] = temp;
	}
}
```

#### [406. 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/)

![image-20220202194204965](2%20Recursion%20I%20and%20Sorting%20Algorithms.assets/image-20220202194204965.png)

![image-20220202211706709](2%20Recursion%20I%20and%20Sorting%20Algorithms.assets/image-20220202211706709.png)

```java
class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o2[0] - o1[0]);
        List<int[]> queue = new ArrayList<>();
        for (int[] p : people) {
            queue.add(p[1], p);
        }
        return queue.toArray(new int[queue.size()][2]);
    }
}
```
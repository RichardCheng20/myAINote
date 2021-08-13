# Binary Search
## Classical Binary Search
Given a target integer T and an integer array A sorted in ascending order, find the index i such that A[i] == T or return -1 if there is no such index.

Assumptions

There can be duplicate elements in the array, and you can return any of the indices i such that A[i] == T.
Examples

A = {1, 2, 3, 4, 5}, T = 3, return 2
A = {1, 2, 3, 4, 5}, T = 6, return -1
A = {1, 2, 2, 2, 3, 4}, T = 2, return 1 or 2 or 3
Corner Cases

What if A is null or A is of zero length? We should return -1 in this case.
思路：
1. 判断为空或者为长度为0
2. 左右边界while遍历
3. while (left <= right) , mid在里面
			

```java
public class Solution {
	public int binarySearch(int[] array, int target) {
		if (array == null || array.length == 0) {
			return -1;
		}
		int left = 0;
		int right = array.length - 1;
		
		while (left <= right) {
		
			int mid = left + (right - left) / 2;
			
			if (array[mid] == target) {
				return mid;
			} else if (array[mid] < target) {
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		}
		return -1;
	}
}
```
## 267. Search In Sorted Matrix I
Given a 2D matrix that contains integers only, which each row is sorted in an ascending order. The first element of next row is larger than (or equal to) the last element of previous row.

Given a target number, returning the position that the target locates within the matrix. If the target number does not exist in the matrix, return {-1, -1}.

Assumptions:

The given matrix is not null, and has size of N * M, where N >= 0 and M >= 0.
Examples:

matrix = { {1, 2, 3}, {4, 5, 7}, {8, 9, 10} }

target = 7, return {1, 2}

target = 6, return {-1, -1} to represent the target number does not exist in the matrix.
简单! 
思路: 二维矩阵变成一维,二分查找
注意
		int row = mid / cols;
		int col = mid % cols;
		没找到时: return new int[] {-1, -1};

```java
public class Solution {
  public int[] search(int[][] matrix, int target) {
	if (matrix.length == 0 || matrix[0].length == 0) {
		return new int[] {-1, -1};
	}
	int rows = matrix.length;
	int cols = matrix[0].length;
	int left = 0;
	int right = rows * cols - 1;
	while (left <= right) {
		int mid = left + (right - left) / 2;
		int row = mid / cols;
		int col = mid % cols;
		if (matrix[row][col] == target) {
			return new int[] {row, col};
		} else if (matrix[row][col] < target) {
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}
	return new int[] {-1, -1};
}
}
```

##  Closest In Sorted Array
Given a target integer T and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to T.

Assumptions

There can be duplicate elements in the array, and we can return any of the indices with same value.
Examples

A = {1, 2, 3}, T = 2, return 1
A = {1, 4, 6}, T = 3, return 1
A = {1, 4, 6}, T = 5, return 1 or 2
A = {1, 3, 3, 4}, T = 2, return 0 or 1 or 2
Corner Case

What if A is null or A is of zero length? We should return -1 in this case.
- 找最近的,需要满足留有两个元素
  while(left < right - 1)
- 取绝对值

```java
public class Closest {
	public int closest(int[] array, int target) {
		if (array.length == 0 || array == null) {
			return -1;
		}
		int left = 0;
		int right = array.length - 1;
		while (left < right - 1) {
			int mid = left + (right - left) / 2;
			if (array[mid] == target) {
				return mid;
			} else if (array[mid] < target) {
				left = mid;
			} else {
				right = mid;
			}
		}
		if (Math.abs(array[left] - target) < Math.abs(array[right] - target)) {
			return left;
		} else {
			return right;
		}
	}
}
```
## 15. First Occurrence
Given a target integer T and an integer array A sorted in ascending order, find the index of the first occurrence of T in A or return -1 if there is no such index.

Assumptions

There can be duplicate elements in the array.
Examples

A = {1, 2, 3}, T = 2, return 1
A = {1, 2, 3}, T = 4, return -1
A = {1, 2, 2, 2, 3}, T = 2, return 1
Corner Cases

What if A is null or A of zero length? We should return -1 in this case.

- 需要保留两个数
   while (left < right - 1) 
- 最后先检查左边再检查右边

```java
public class Solution {
	public int firstOccur(int[] array, int target) {
		if (array.length == 0 || array == null) {
			return -1;
		}
		int left = 0;
		int right = array.length - 1;
		while (left < right - 1) {
			int mid = left + (right - left) / 2;
			if (array[mid] >= target) {
				right = mid; //先把右边逼近
			} else {
				left = mid;
			}
		}
		if (array[left] == target) {
			return left;
		} else if (array[right] == target) {
			return right;
		}
		return -1;
	} 
}
```

## 16. Last Occurrence
Given a target integer T and an integer array A sorted in ascending order, find the index of the last occurrence of T in A or return -1 if there is no such index.

Assumptions

There can be duplicate elements in the array.

Examples

A = {1, 2, 3}, T = 2, return 1
A = {1, 2, 3}, T = 4, return -1
A = {1, 2, 2, 2, 3}, T = 2, return 3
Corner Cases

What if A is null or A is array of zero length? We should return -1 in this case.
同样的道理 

- 先压缩左边if (array[mid] <= target) {
				mid = left;
			} 
- 然后先检查右边
	if (array[right] == target) {
			return right;
		} 
```java
public class Solution {
	public int lastOccur(int[] array, int target) {
		if (array.length == 0 || array == null) {
			return -1;
		}
		int left = 0;
		int right = array.length -1;
		while (left < right - 1) {
			int mid = left + (right - left) / 2;
			if (array[mid] <= target) {
				mid = left;
			} else {
				right = left;
			}
		}
		if (array[right] == target) {
			return right;
		} else if (array[left] == target]) {
			return left;
		}
		return -1;
	}
}
 
```
## 19. K Closest In Sorted Array
Given a target integer T, a non-negative integer K and an integer array A sorted in ascending order, find the K closest numbers to T in A. If there is a tie, the smaller elements are always preferred.

Assumptions

A is not null
K is guranteed to be >= 0 and K is guranteed to be <= A.length
Return

A size K integer array containing the K closest numbers(not indices) in A, sorted in ascending order by the difference between the number and T. 
Examples

A = {1, 2, 3}, T = 2, K = 3, return {2, 1, 3} or {2, 3, 1}
A = {1, 4, 6, 8}, T = 3, K = 3, return {4, 1, 6}
 - 题目要求查找k个最近的,可以先找离target最近的,找一个`<=`target的, 然后for loop中心开花
 - 需要返回的数组 int[] result = new int[k];  为空没找到的情况 return new int[0];
if(right >= array.length || left > 0 && target - **array[left]** <= array[right] - target) {
	//右边越界 || 左边不越界接近
}

```java
public class Solution {
	public int[] kClosest(int[] array, int target, int k) {
		if (array == null || array.length == 0) {
			return new int[0];
		}
		int left = largestSmallerEqual(array, target); //左边界<=
		int right = left + 1; //右边界
		int[] result = new int[k];
		for(int i = 0; i < k; i++) {
			if (right >= array.length || left >= 0 && target - array[left] <= array[right] - target) {
				result[i] = array[left--];
			} else {
				result[i] = array[right++];
			}
		}
		return result;
	}
	private int largestSmallerEqual(int[] array, int target) {
		int left = 0;
		int right = array.length - 1;
		while (left < right - 1) {
			int mid = left + (right - left) / 2;
			if (array[mid] <= target) {
				left = mid;
			} else {
				right = mid;
			}
		}
		if (array[right] <= target) {
			return right;
		}
		if (array[left] <= target) {
			return left;
		}
		return -1;
 	}
}
```
## 636. Smallest Element Larger than Target
Given a target integer T and an integer array A sorted in ascending order, find the index of the smallest element in A that is larger than T or return -1 if there is no such index.

Assumptions

There can be duplicate elements in the array.

Examples

A = {1, 2, 3}, T = 1, return 1

A = {1, 2, 3}, T = 3, return -1

A = {1, 2, 2, 2, 3}, T = 1, return 1

Corner Cases

What if A is null or A of zero length? We should return -1 in this case.

```java
public class Solution {
	public int smallestElementLargerThanTarget(int[] array, int target) {
		if (array.length == 0 || array == null) {
			return -1;
		}
		int left = 0;
		int right = array.length - 1;
		while (left < right - 1) {
			int mid = left + (right - left) / 2;
			if (array[mid] <= target) {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		if (array[left] > target) {
			return left;
		} else if (array[right] > target) {
			return right;
		}
		return -1;
	} 
}
```
## 20. Search In Unknown Sized Sorted Array
Given a integer dictionary A of unknown size, where the numbers in the dictionary are sorted in ascending order, determine if a given target integer T is in the dictionary. Return the index of T in A, return -1 if T is not in A.

Assumptions

dictionary A is not null
dictionary.get(i) will return null(Java)/INT_MIN(C++)/None(Python) if index i is out of bounds
Examples

A = {1, 2, 5, 9, ......}, T = 5, return 2
A = {1, 2, 5, 9, 12, ......}, T = 7, return -1

关键就是需要判断字典不要越界

```java
public class Solution {
  public int search(Dictionary dic, int target){
  	if (dic == null) {
  		return -1;
  	}
  	int left = 0;
  	int right = 1;
  	while (dic.get(right) != null && dic.get(right) < target) {
  		left = right;
  		right = 2 * right;
  	}
  	return binarySearch(dic, target, left, right);
  }
  private int binarySearch(Dictionary dict, int target, int left, int right) {
  	while(left <= right) {
  		int mid = left + (right - left) / 2;
  		if (dict.get(mid) == null || dict.get(mid) > target) {
  			right = mid - 1;
  		} else if (dict.get(mid) < target) {
  			left = mid + 1;
  		} else {
  			return mid;
  		}
  	}
  	return -1;
  }
}
```


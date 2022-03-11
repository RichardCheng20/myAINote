还没做！！！ 

#### [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)

![image-20220119210809762](10%20Bi%20Representation%20&%20Operation.assets/image-20220119210809762.png)

```java
class Solution {
    public int singleNumber(int[] nums) {
        int single = 0;
        for (int num : nums) {
            single ^= num;
        }
        return single;
    }
}
```



#### [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)

![image-20220124144711508](10%20Bi%20Representation%20&%20Operation.assets/image-20220124144711508.png)

#### [461. 汉明距离](https://leetcode-cn.com/problems/hamming-distance/)

![image-20220223201457353](10%20Bi%20Representation%20&%20Operation.assets/image-20220223201457353.png)

分享一下位运算的巧用：

1. 判断数偶： 奇数 x % 2 == 1 偶数x % 2 == 0
2. 两数取平均(除2): mid = (left+right)/2 等价于 mid = (left+right) >> 1
3. 清除最低位的1: x = x&(x-1)
4. 得到最低位的1: n = x & -x
5. 清零: x&~x

这道题就是异或之后的查看结果中1的个数

```java
class Solution {
    public int hammingDistance(int x, int y) {
        int z = x ^ y;
        int count = 0;
        while (z != 0) {
            z &= z - 1;
            count++;
        }
        return count;
    }
}
=======
  class Solution {
    public int hammingDistance(int x, int y) {
        int z = x ^ y;
        int count = 0;
        while (z != 0) {
           if ((z & 1) == 1) count++;
           z = z >> 1;
        }
        return count;
    }
}
```




1. 在mac上从git上clone复制下来需要的仓库: 

2. **找到clone地址**

   https://github.com/RichardCheng20/myAINote.git

![image-20210831105750114](../macwindows%E5%90%8C%E6%AD%A5.assets/image-20210831105750114.png)


![image-20210831105621661](../macwindows%E5%90%8C%E6%AD%A5.assets/image-20210831105621661.png)

==git clone==  会有仓库的基本配置

3. 如果出现私有访问错误需要使用**token**

![image-20210831105509895](../macwindows%E5%90%8C%E6%AD%A5.assets/image-20210831105509895.png)

Reference: https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Fix-GitHubs-support-for-password-authentication-was-removed-error

比如我的token: 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

注意密码使用token

![image-20210831093823121](/Users/chengzhifu/Library/Application Support/typora-user-images/image-20210831093823121.png)

4. 一定要到你clone下来的地址里查看git status 

![image-20210831110108213](../macwindows%E5%90%8C%E6%AD%A5.assets/image-20210831110108213.png)

5. Mac提交到github

`git add .` 将项目添加到暂存区

`git commit -m "comment"` 提交到本地仓库

`git push` 提交到远程仓库

`git pull` 拉取/同步远程仓库代码到本地 一定要记得pull 

![image-20210831110240874](../macwindows%E5%90%8C%E6%AD%A5.assets/image-20210831110240874.png)
G:\BaiduNetdiskDownload\1、Maven从基础到高级应用\视频-Maven

## Maven简介

![image-20220428172437871](day1.assets/image-20220428172437871.png)

![image-20220428172614661](day1.assets/image-20220428172614661.png)

- 1 下载地址

http://maven.apache.org/  

http://maven.apache.org/download.cgi  

- 2 环境变量配置路径安装



![image-20220428213110688](day1.assets/image-20220428213110688.png)



### 本地仓库配置

- repository位置

D:\maven\repository

D:\soft\apache-maven-3.6.3-bin\apache-maven-3.6.3\conf

![image-20220428214312013](day1.assets/image-20220428214312013.png)



### 远程仓库配置

![image-20220428215126406](day1.assets/image-20220428215126406.png)

### 手工制作Maven项目

![image-20220428220301951](day1.assets/image-20220428220301951.png)

<img src="day1.assets/image-20220428220229821.png" alt="image-20220428220229821" style="zoom:50%;" />

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project
xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>com.itheima</groupId>
<artifactId>project-java</artifactId>
<version>1.0</version>
<packaging>jar</packaging>
<dependencies>
<dependency>
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>4.12</version>
</dependency>
</dependencies>
</project>
```

maven命令

<img src="day1.assets/image-20220428220803123.png" alt="image-20220428220803123" style="zoom:33%;" />

```xml
mvn compile #
mvn clean #
mvn test #
mvn package #
mvn install #
```

或者使用插件： 

![image-20220428222851022](day1.assets/image-20220428222851022.png)

![image-20220428223515654](day1.assets/image-20220428223515654.png)

### Idea创建

D:\soft\apache-maven-3.6.1\conf记得修 改setting文件

1. 创建空project，一定要是3.6.1一下版本无冲突

2. ![image-20220428224445221](day1.assets/image-20220428224445221.png)
3. ![image-20220428224734193](day1.assets/image-20220428224734193.png)
4. ![image-20220428224848070](day1.assets/image-20220428224848070.png)
5. ![image-20220428225007921](day1.assets/image-20220428225007921.png)
6. ![image-20220428225317628](day1.assets/image-20220428225317628.png)
7. 在pom.xml中添加

```xml
<dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
        </dependency>
    </dependencies>
```

8. 然后写Demo.java和DemoTest.java

```java
package com.itheima;

public class Demo {
    public String say(String name) {
        System.out.println("hello " + name);
        return "hello " + name;

    }
}
```

![image-20220429081324797](day1.assets/image-20220429081324797.png)

![image-20220429081147342](day1.assets/image-20220429081147342.png)

### 使用原型创建

1. 新建module

![image-20220429081810901](day1.assets/image-20220429081810901.png)

![image-20220429082729743](day1.assets/image-20220429082729743.png)

### 创建web工程

![image-20220429085355373](day1.assets/image-20220429085355373.png)

![image-20220429090521329](day1.assets/image-20220429090521329.png)

![image-20220429090810413](day1.assets/image-20220429090810413.png)

在web.xml中只保留

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app version="2.4"
         xmlns="http://java.sun.com/xml/ns/j2ee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd">
</web-app>
```

然后pom.xml删除干净

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

  <modelVersion>4.0.0</modelVersion>
  <packaging>war</packaging>

  <name>web01</name>
  <groupId>com.itheima</groupId>
  <artifactId>web01</artifactId>
  <version>1.0-SNAPSHOT</version>
  
  <dependencies>
  </dependencies>

</project>
```

然后添加插件

```xml
 <build>
        <plugins>
            <plugin>

                <groupId>org.apache.tomcat.maven</groupId>
                <artifactId>tomcat7-maven-plugin</artifactId>
                <version>2.1</version>
                <configuration>
                    <port>80</port>
                    <path>/</path>
                </configuration>

            </plugin>
        </plugins>
    </build>
```

![image-20220429105511527](day1.assets/image-20220429105511527.png)

完整版pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <packaging>war</packaging>

    <groupId>com.itheima</groupId>
    <artifactId>web01</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.tomcat.maven</groupId>
                <artifactId>tomcat7-maven-plugin</artifactId>
                <version>2.1</version>
                <configuration>
                    <port>80</port>
                    <path>/</path>
                </configuration>

            </plugin>
        </plugins>
    </build>
</project>
```

### 依赖管理

![image-20220429110629788](day1.assets/image-20220429110629788.png)

导入方式：

03用了的jar包，02可以用！

![image-20220429110314107](day1.assets/image-20220429110314107.png)

![image-20220429110611969](day1.assets/image-20220429110611969.png)

可选依赖

![image-20220429110754838](day1.assets/image-20220429110754838.png)

排除依赖

![image-20220429111556120](day1.assets/image-20220429111556120.png)

### 依赖范围

![image-20220429140929035](day1.assets/image-20220429140929035.png)

![image-20220429163718776](day1.assets/image-20220429163718776.png)

### 生命周期与插件

 ![image-20220429165628765](day1.assets/image-20220429165628765.png)





![image-20220429170911372](day1.assets/image-20220429170911372.png)

运行到generate-test-resource这个阶段的时候就需要执行插件

执行什么由goal决定，jar对源码打包

![image-20220429171941029](day1.assets/image-20220429171941029.png)

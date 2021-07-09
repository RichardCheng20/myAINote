# 03 MyBatis入门

•	核心组件
`SqlSessionFactory`：用于创建SqlSession的工厂类。
`SqlSession`：MyBatis的核心组件，用于向数据库执行SQL。
`主配置文件`：XML配置文件，可以对MyBatis的底层行为做出详细的配置。
`Mapper接口`：就是DAO接口，在MyBatis中习惯性的称之为**Mapper**。
`Mapper映射器`：用于编写SQL，并将SQL和实体类映射的组件，**采用XML、注解**均可实现。
•	示例
使用MyBatis对用户表进行CRUD操作。
http://www.mybatis.org/mybatis-3 
http://www.mybatis.org/spring
https://mvnrepository.com/artifact/mysql/mysql-connector-java/8.0.25

# step1 先去配置mysql和mybatis 

```xml
#ServerProperties
server.port=8080
server.servlet.context-path=/community
#ThymeleafProperties
spring.thymeleaf.cache=false

# DataSourceProperties
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/community?characterEncoding=utf-8&useSSL=false&serverTimezone=Hongkong
spring.datasource.username=root
spring.datasource.password=root
spring.datasource.type=com.zaxxer.hikari.HikariDataSource
spring.datasource.hikari.maximum-pool-size=15
spring.datasource.hikari.minimum-idle=5
spring.datasource.hikari.idle-timeout=30000

# MybatisProperties entity用来封装表的数据
mybatis.mapper-locations=classpath:mapper/*.xml
mybatis.type-aliases-package=com.nowcoder.community.entity
#主键自增长
mybatis.configuration.useGeneratedKeys=true
mybatis.configuration.mapUnderscoreToCamelCase=true

```
# step 2 在entity中创建User.java

```java
public class User {
// id,username,password,salt,email,type,status,activation_code,header_url,create_time
    private int id;
    private String username;
    private String password;
    private String salt;
    private String email;
    private int type;
    private int status;
    private String activationCode;
    private String headerUrl;
    private Date createTime;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getSalt() {
        return salt;
    }

    public void setSalt(String salt) {
        this.salt = salt;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public String getActivationCode() {
        return activationCode;
    }

    public void setActivationCode(String activationCode) {
        this.activationCode = activationCode;
    }

    public String getHeaderUrl() {
        return headerUrl;
    }

    public void setHeaderUrl(String headerUrl) {
        this.headerUrl = headerUrl;
    }

    public Date getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Date createTime) {
        this.createTime = createTime;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                ", salt='" + salt + '\'' +
                ", email='" + email + '\'' +
                ", type=" + type +
                ", status=" + status +
                ", activationCode='" + activationCode + '\'' +
                ", headerUrl='" + headerUrl + '\'' +
                ", createTime=" + createTime +
                '}';
    }
}
```
# Step 3 然后访问数据库在DAO

在dao目录下创建UserMapper接口

```java
package com.nowcoder.community.dao;

import com.nowcoder.community.entity.User;
import org.apache.ibatis.annotations.Mapper;

//使用mybatis的注解来标识bean
@Mapper
public interface UserMapper {
    //写上增删改和sql配置文件

    //根据Id查询用户
    User selectById(int id);
    //用户名查询
    User selectByName(String username);
    // 邮箱
    User selectByEmail(String email);

    //增加
    int insertUser(User user);

    //修改状态
    int updateStatus(int id, int status);

    int updateHeader(int id, String headerUrl);

    int updatePassword(int id, String password);

}
```

 # step 4 在mapper目录下创建user-mapper.xml


```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!--1 修改namespace为接口位置-->
<mapper namespace="com.nowcoder.community.dao.UserMapper">
    <sql id="insertFields">
        username,password,salt,email,type,status,activation_code,header_url,create_time
    </sql>
    <sql id="selectFields">
        id,username,password,salt,email,type,status,activation_code,header_url,create_time
    </sql>
    <!--    User selectById(int id);id要写对应的方法名-->
    <select id="selectById" resultType="User">
        select
        <include refid="selectFields"></include>
        from user
        where id = #{id}
    </select>
    <!--    User selectByName(String username);-->
    <select id="selectByName" resultType="User">
        select
        <include refid="selectFields"></include>
        from user
        where username = #{username}
    </select>
    <!--    User selectByEmail(String email);-->
    <select id="selectByEmail" resultType="User">
        select
        <include refid="selectFields"></include>
        from user
        where email = #{email}
    </select>

    <!--    int insertUser(User user);如果参数是一个bean就需要声明-->
    <insert id="insertUser" parameterType="User" keyProperty="id">
        insert into user (<include refid="insertFields"></include>>)
        values(#{username},#{password},#{salt},#{email},#{type},#{status},#{activationCode},#{headerUrl},#{createTime})
    </insert>

    <!--    int updateStatus(int id, int status);-->
    <update id="updateStatus">
        update user set status = #{status} where id = #{id}
    </update>
    <!--    int updateHeader(int id, String headerUrl);-->
    <update id="updateHeader">
        update user set header_url = #{headerUrl} where id = #{id}
    </update>
    <!--    int updatePassword(int id, String password);-->
    <update id="updatePassword">
        update user set password = #{password} where id = #{id}
    </update>
</mapper>
```
# step 5 test目录下创建MapperTests 

降低打印日志的级别便于Debug 
logging.level.com.nowcoder.community=debug
#logging.file=d:/work/data/nowcoder/community.log

```java

@RunWith(SpringRunner.class)
@SpringBootTest
//测试代码以某一个为配置类
@ContextConfiguration(classes = CommunityApplication.class)
public class MapperTests {
    @Autowired
    private UserMapper userMapper;

    @Test
    public void testSelectUser() {
        User user = userMapper.selectById(101);
        System.out.println(user);

        user = userMapper.selectByName("liubei");
        System.out.println(user);

        user = userMapper.selectByEmail("nowcoder101@sina.com");
        System.out.println(user);
    }

    @Test
    public void testInsertUser() {
        User user = new User();
        user.setUsername("test");
        user.setPassword("123456");
        user.setSalt("abc");
        user.setEmail("test@qq.com");
        user.setHeaderUrl("http://www.nowcoder.com/101.png");
        user.setCreateTime(new Date());

        int rows = userMapper.insertUser(user);
        System.out.println(rows);
        System.out.println(user.getId());
    }

    @Test
    public void updateUser() {
        int rows = userMapper.updateStatus(150, 1);
        System.out.println(rows);

        rows = userMapper.updateHeader(150, "http://www.nowcoder.com/102.png");
        System.out.println(rows);

        rows = userMapper.updatePassword(150, "hello");
        System.out.println(rows);
    }
```
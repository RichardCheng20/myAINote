# 0 1 Spring 入门
SpringBoot简化spring而生

Spring, Spring MVC, MyBatis ssm



`注解`

## config包
```java
//配置类注解
@Configuration
public class AlphaConfig {

    //调用第三方的bean,bean的名字以方法命名
    @Bean
    public SimpleDateFormat simpleDateFormat() {
        return new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    }
}
```
## controller 
```java
@Controller
@RequestMapping("/alpha")
public class AlphaController {

    //注入service
    @Autowired
    private AlphaService alphaService;

    //浏览器路径
    @RequestMapping("/hello")
    @ResponseBody
    public String sayHello() {
        return "Hello Spring Boot.";
    }

    //处理查询请求

    @RequestMapping("/data")
    @ResponseBody
    public String getData() {
        return alphaService.find();
    }
}
```
## dao
### 接口AlphaDao
```java
public interface AlphaDao {
    String select();
}
```
### 接口的实现Hibernate 
```java
package com.nowcoder.community.dao;

import org.springframework.stereotype.Repository;

//访问数据库的注解,括号里面是定义名字
@Repository("alphaDaoHibernate")
public class AlphaDaoHibernateImpl implements AlphaDao{
    @Override
    public String select() {
        return "Hibernate";
    }
}
```

### 接口的实现Mybatis 
```java
@Repository
//防止两bean冲突
@Primary
public class AlphaDaoMyBatisImpl implements AlphaDao{
    @Override
    public String select() {
        return "MyBatis";
    }
}
```




## service 
```java
//业务组件的注解
@Service
public class AlphaService {

    public AlphaService() {
        System.out.println("实例化AlphaService");
    }

    //注解容器自动调用这个方法,这方法会在构造器之后调用
    @PostConstruct
    public void init() {
        System.out.println("初始化AlphaService");
    }

    //在销毁对象之前调用
    @PreDestroy
    public void destroy() {
        System.out.println("销毁AlphaService");
    }
}
```
程序启动实例化，bean只被实例化一次， 只有一个实例，因为web只被实例化一次。 
以上都是使用spring容器管理自己写的类，假如需要使用别人jar包中的类，不能直接在类上加上注解， 需要自己写一个配置类，在配置类中通过bean注解声明，放到config包

**什么叫依赖注入？** 
例如当前的bean要使用alpha dao,没有必要通过容器去getBean获取，只用给声明注入alpha dao就可以了，
![在这里插入图片描述](https://gitee.com/RichardCheng_5ecf/cloudimage/raw/master/img/20210521010223886.png)


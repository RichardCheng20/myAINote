03 tcp状态和多路IO1tcp状态转换图![img](D:/Program Files/Typora/03 tcp状态和多路IO_files/Image.png)
2 半关闭主动方发生在FIN_WAIT_2状态,这个状态时,主动方不可以在应用层发送数据了,但是应用层还可以接收数据,这个状态称为半关闭#include <sys/socket.h>int shutdown(int sockfd, int how);sockfd: 需要关闭的socket的描述符how:  允许为shutdown操作选择以下几种方式:  SHUT_RD(0)：  关闭sockfd上的读功能，此选项将不允许sockfd进行读操作。          该套接字**不再接收数据**，任何当前在套接字接受缓冲区的数据将被无声的丢弃掉。  SHUT_WR(1):   关闭sockfd的写功能，此选项将不允许sockfd进行写操作。进程不能在对此套接字发出写操作。  SHUT_RDWR(2):  关闭sockfd的读写功能。相当于调用shutdown两次：首先是以SHUT_RD,然后以SHUT_WR。

3 心跳包如果对方异常断开,本机检测不到,一直等待,浪费资源需要设置tcp的保持连接,作用就是每隔一定的时间间隔发送探测分节,如果连续发送多个探测分节对方还未回,就将次连接断开int keepAlive = 1;setsockopt(listenfd, SOL_SOCKET, SO_KEEPALIVE, (void*)&keepAlive, sizeof(keepAlive));
心跳包: 最小粒度乒乓包: 携带比较多的数据的心跳包
4 设置端口复用int opt = 1;  setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));注意: 程序中设置某个端口重新使用,在这之前的其他网络程序将不能使用这个端口

5 高并发服务器阻塞等待 消耗资源非阻塞忙轮询 消耗cpu多路IO多路IO转接(多路IO复用): 内核监听多个文件描述符的属性(读写缓冲区)变化如果某个文件描述符的读缓冲区变化了,这个时候就是可以读了,将这个事件告知应用层![img](D:/Program Files/Typora/03 tcp状态和多路IO_files/Image [1].png)6 select epoll pollwindwos  使用select  select跨平台poll 少用epoll  linux 
7 select函数的API#include <sys/select.h> /* According to earlier standards */    #include <sys/time.h>    #include <sys/types.h>    #include <unistd.h>
    int select(int nfds, fd_set *readfds, fd_set *writefds,         fd_set *exceptfds, struct timeval *timeout);功能: 监听多个文件描述符的属性变化(读,写,异常)    void FD_CLR(int fd, fd_set *set);    int FD_ISSET(int fd, fd_set *set);    void FD_SET(int fd, fd_set *set);    void FD_ZERO(fd_set *set);
参数:   nfds : 最大文件描述符+1   readfds : 需要监听的读的文件描述符存放集合   writefds :需要监听的写的文件描述符存放集合  NULL   exceptfds : 需要监听的异常的文件描述符存放集合 NULL   timeout: 多长时间监听一次  固定的时间,限时等待  NULL 永久监听   struct timeval {        long  tv_sec;     /* seconds */ 秒        long  tv_usec;    /* microseconds */微妙      };
 返回值: 返回的是变化的文件描述符的个数注意: 变化的文件描述符会存在监听的集合中,未变化的文件描述符会从集合中删除   8 select实现的原理![img](D:/Program Files/Typora/03 tcp状态和多路IO_files/Image [2].png)
9 select 的优缺点优点: 跨平台缺点:文件描述符1024的限制  由于 FD_SETSIZE的限制只是返回变化的文件描述符的个数,具体哪个那个变化需要遍历每次都需要将需要监听的文件描述集合由应用层符拷贝到内核大量并发,少了活跃,select效率低
假设现在 4-1023个文件描述符需要监听,但是5-1000这些文件描述符关闭了?假设现在 4-1023个文件描述符需要监听,但是只有 5,1002 发来消息- 无解
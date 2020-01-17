### 多路复用IO(IO multiplexing)（重点）
有些地方也称这种IO方式为事件驱动`IO(event driven IO)`。`select/epoll`的好处就在于单个`process`就可以同时处理多个网络连接的IO。它的基本原理就是`select/epoll`这个function会不断的轮询所负责的所有`socket`，当某个`socket`有数据到达了，就通知用户进程。
![多路复用模型](images/model.PNG)

当用户进程调用了`select`，那么整个进程会被`block`，而同时，kernel会“监视”所有`select`负责的`socket`，当任何一个`socket`中的数据准备好了，`select`就会返回。这个时候用户进程再调用`read`操作，将数据从`kernel`拷贝到用户进程。

这个图和`blocking IO`的图其实并没有太大的不同，事实上还更差一些。因为它不仅阻塞了还多需要使用两个系统调用`(select和recvfrom)`，而`blocking IO`只调用了一个系统调用`(recvfrom)`，当只有一个连接请求的时候，这个模型还不如阻塞IO效率高。但是，用`select`的优势在于它可以同时处理多个`connection`，而阻塞`IO`那里不能，我不管阻塞不阻塞，你所有的连接包括`recv`等操作，我都帮你监听着,其中任何一个有变动（有连接，有数据），我就告诉你用户，那么你就可以去调用这个数据了，这就是他的NB之处。这个IO多路复用模型机制是操作系统帮我们提供的，在windows上有这么个机制叫做`select`，那么如果我们想通过自己写代码来控制这个机制或者自己写这么个机制，我们可以使用python中的`select`模块来完成上面这一系列代理的行为。在一切皆文件的unix下，这些可以接收数据的对象或者连接，都叫做文件描述符`fd`。

强调：

. 如果处理的连接数不是很高的话，使用`select/epoll`的web server不一定比使用`multi-threading + blocking IO`的web server性能更好，可能延迟还更大。`select/epoll`的优势并不是对于单个连接能处理得更快，而是在于能**处理更多的连接**。

. 在多路复用模型中，对于每一个`socket`，一般都设置成为`non-blocking`，但是，如上图所示，整个用户的`process`其实是一直被`block`的。只不过`process`是被`select`这个函数`block`，而不是被`socket IO`给`block`。

### python中的select模块：
``` py
import select

fd_r_list, fd_w_list, fd_e_list = select.select(rlist, wlist, xlist, [timeout])
```
参数： 可接受四个参数（前三个必须） 
`rlist: wait until ready for reading`:等待读的对象，你需要监听的需要获取数据的对象列表 
`wlist: wait until ready for writing`:等待写的对象，你需要写一些内容的时候，input等等，也就是说我会循环他看看是否有需要发送的消息，如果有我取出这个对象的消息并发送出去，一般用不到，这里我们也给一个[]。 
`xlist: wait for an “exceptional condition”`:等待异常的对象，一些额外的情况，一般用不到，但是必须传，那么我们就给他一个[]。
`timeout`: 超时时间 
当`超时时间 ＝ n(正整数)`时，那么如果监听的句柄均无任何变化，则`select`会阻塞n秒，之后返回三个空列表，如果监听的句柄有变化，则直接执行。 
返回值：三个列表与上面的三个参数列表是对应的 
`select`方法用来监视文件描述符(当文件描述符条件不满足时，`select`会阻塞)，当某个文件描述符状态改变后，会返回三个列表: 
. 当`参数1`序列中的`fd`满足“可读”条件时，则获取发生变化的fd并添加到`fd_r_list`中 
. 当`参数2`序列中含有`fd`时，则将该序列中所有的`fd`添加到 `fd_w_list`中 
. 当`参数3`序列中的`fd`发生错误时，则将该发生错误的`fd`添加到 `fd_e_list`中 
. 当超时时间为空，则`select`会一直阻塞，直到监听的句柄发生变化 

### 结论: select的优势在于可以处理多个连接，不适用于单个连接。

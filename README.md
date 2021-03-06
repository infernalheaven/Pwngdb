# Pwngdb

GDB for pwn.

## Install

### install
	cd ~/
	git clone https://github.com/scwuaptx/Pwngdb.git 
	cp ~/Pwngdb/.gdbinit ~/

If you dont want to use gdb-peda , you can modify the gdbinit to remove it.

### Heapinfo 

If you want to use the feature of heapinfo and tracemalloc , you need to install libc debug file (libc6-dbg & libc6-dbg:i386 for debian package) 

## Features

+ `libc` : Print the base address of libc
+ `ld` : Print the base address of ld
+ `codebase` : Print the base of code segment
+ `heap` : Print the base of heap
+ `got` : Print the Global Offset Table infomation
+ `dyn` : Print the Dynamic section infomation
+ `findcall` : Find some function call 
+ `bcall` : Set the breakpoint at some function call
+ `tls` : Print the thread local storage address
+ `at` : Attach by process name
+ `findsyscall` : Find the syscall
+ `fmtarg` : Calculate the index of format string
	+ You need to stop on printf which has vulnerability.
+ `force` : Calculate the nb in the house of force.
+ `heapinfo` : Print some infomation of heap
+ `chunkinfo`: Print the infomation of chunk
    + chunkinfo (Address of victim)
+ `chunkptr` : Print the infomation of chunk 
	+ chunkptr (Address of user ptr)
+ `mergeinfo` : Print the infomation of merge
	+ mergeinfo (Address of victim)
+ `printfastbin` : Print some infomation of fastbin
+ `tracemalloc on` : Trace the malloc and free and detect some error .
	+ You need to run the process first than `tracemalloc on`, it will record all of the malloc and free.
	+ You can set the `DEBUG` in pwngdb.py , than it will print all of the malloc and free infomation such as the screeshot.
+ `parseheap` : Parse heap layout

## Screenshot

+ Chunkinfo

![chunkinfo](http://i.imgur.com/gtQuIsL.png)
+ Mergeinfo

![chunkinfo](http://i.imgur.com/TjWkzGc.png)
+ Heapinfo

![heapinfo](http://i.imgur.com/xhTc8Gv.png)

+ parseheap

![parseheap](http://i.imgur.com/R7goaLF.png)

+ tracemalloc

![trace](http://i.imgur.com/7UHqiwX.png)

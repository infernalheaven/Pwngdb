import gdb
import angelheap

from utils import *

angelheap_cmd = None

class AngelHeapCmd(object):
    commands = []
    def __init__(self):
        # list all commands
        self.commands = [cmd for cmd in dir(self) if callable(getattr(self, cmd)) ]  

    def tracemalloc(self,*arg):
        """ Trace the malloc and free and detect some error """
        (option,) = normalize_argv(arg,1)
        if option == "on":
            try :
                angelheap.trace_malloc()
            except :
                print("Can't create Breakpoint")
        else :
            angelheap.dis_trace_malloc()

    def heapinfo(self):
        """ Print some information of heap """
        angelheap.putheapinfo()

    def chunkinfo(self,*arg):
        """ Print chunk information of victim"""
        (victim,) = normalize_argv(arg,1)
        angelheap.chunkinfo(victim)

    def chunkptr(self,*arg):
        """ Print chunk information of user ptr"""
        (ptr,) = normalize_argv(arg,1)
        angelheap.chunkptr(ptr)

    def mergeinfo(self,*arg):
        """ Print merge information of victim"""
        (victim,) = normalize_argv(arg,1)
        angelheap.mergeinfo(victim)

    def force(self,*arg):
        """ Calculate the nb in the house of force """
        (target,) = normalize_argv(arg,1)
        angelheap.force(target)
    
    def printfastbin(self):
        """ Print the fastbin """
        angelheap.putfastbin()

    def inused(self):
        """ Print the inuse chunk """
        angelheap.putinused()

    def parseheap(self):
        """ Parse heap """
        heapbase = int(gdb.execute("heap",to_string=True).split("\x1b[37m")[1].strip(),16)
        if heapbase :
            angelheap.parse_heap(heapbase)
        else :
            print("heap not found")

    def fakefast(self,*arg):
        (addr,size) = normalize_argv(arg,2)
        angelheap.get_fake_fast(addr,size)

class AngelHeapCmdWrapper(gdb.Command):
    """ angelheap command wrapper """
    def __init__(self):
        super(AngelHeapCmdWrapper,self).__init__("angelheap",gdb.COMMAND_USER)

    def invoke(self,args,from_tty):
        global angelheap_cmd
        self.dont_repeat()
        arg = args.split()
        if len(arg) > 0 :
            cmd = arg[0]

            if cmd in angelheap_cmd.commands :
                func = getattr(angelheap_cmd,cmd)
                func(*arg[1:])
            else :
                print("Unknown command")
        else :
            print("Unknow command")

        return 

class Alias(gdb.Command):
    """ angelheap Alias """

    def __init__(self,alias,command):
        self.command = command
        super(Alias, self).__init__(alias,gdb.COMMAND_NONE)

    def invoke(self,args,from_tty):
        self.dont_repeat()
        gdb.execute("%s %s" % (self.command,args))


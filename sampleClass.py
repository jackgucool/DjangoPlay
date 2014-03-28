__author__ = 'yiminggu'

class Bird:


    def __init__(self,kind,call):
        self.call = call
        self.kind = kind
    #
    # def __init__(self):
    #     self.kind = 'init_kind'
    #     self.call = 'init_call'







    def do_call(self):
        print "a %s goes %s" % (self.kind, self.call)






class Parrot(Bird):  # inherit from Bird
    def __init__(self):
        Bird.__init__(self, "Parrot", "Kah!")


class Cuckoo(Bird):  # inherit from Bird
    def __init__(self):
        Bird.__init__(self, "Cuckoo", "Cuckoo!")


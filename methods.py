# Methods

# class MethodExamples:
#
#     this_can_be_accessed_easily = "Hi, I am easily found!"
#
#     def __init__(self):
#         self.this_can_be_accessed_easily = "Hi, I am easily found!"
#
#
# x = MethodExamples()
#
#
#
# print(x.this_can_be_accessed_easily) #Hi, I am easily found!
# x.this_can_be_accessed_easily = "I have been changed"
# print(x.this_can_be_accessed_easily) #I have been changed



# in most languages public and private must be specified but in python , __init__ can still be accessed
class MethodExamples:
    #this_can_be_accessed_easily = "Hi, I am easily found!"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, I am easily found!"

    def get_this_can_be_accessed_easily(self):
        return self.this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value_to_be_set):
        self.this_can_be_accessed_easily = value_to_be_set

x = MethodExamples()
print(x._this_can_be_accessed_easily) #Hi, I am easily found!
x.set_this_can_be_accessed_easily = "I have been changed"
print(x._this_can_be_accessed_easily) #I have been changed



class queue:
    FRONTPOINTER = 0 #static constant
    def __init__(self,this_list,length = -1):
        if length == -1 or length < len(this_list): #length defaults to the length of the current list
            self.__length = len(this_list)
        else:
            self.__length = length #custom length if given
        self.__this_queue = this_list
        self.rear_pointer = len(this_list)-1 #sets rear pointer to the current last element
    
    def enqueue(self,e) -> bool:
        '''
        Adds an element to that back of the queue. Returns true if the element is added, false if the queue is full.
        '''
        if len(self.__this_queue) < self.__length: #adds an element and returns true if possible
            self.__this_queue.append(e)
            return True
        else:
            return False #returns false if queue is full
    
    def dequeue(self) -> any:
        '''
        Removes and returns the element at the front pointer.
        '''
        if len(self.__this_queue) > 0:
            return self.__this_queue.pop(self.FRONTPOINTER) # removes the element at the head of the queue
        else:
            return None #returns None if the queue is empty
        
    def peek(self) -> any:
        '''
        Returns the front element of the queue. Returns false if the queue is empty.
        '''
        if len(self.__this_queue) > 0:
            return self.__this_queue[self.FRONTPOINTER]
        else:
            return False #returns false if the queue is empty
        
    def get_length(self) -> int:
        '''
        Returns the maximum length of the queue
        '''
        return self.__length
    
    def get_count(self) -> int:
        '''
        Returns the current number of items in the queue
        '''
        return len(self.__this_queue)
    
    def return_queue(self) -> list:
        return(self.__this_queue)





    

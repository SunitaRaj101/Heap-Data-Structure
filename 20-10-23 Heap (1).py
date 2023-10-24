#!/usr/bin/env python
# coding: utf-8

# ## Max Heap

# In[53]:


#Max Heap

class Max_Heap:
    def __init__(self,arr):
        self.arr=arr
        self.size=len(arr)
    #maxheap
    def heapify(self):
        arr=self.arr
        def heapify_algo(arr,i):
            largest=i
            li=2*i+1
            ri=2*i+2
            
            if li<len(arr) and arr[li]>arr[largest]:
                largest=li
            if ri<len(arr) and arr[ri]>arr[largest]:
                largest=ri
            if largest!=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                heapify_algo(arr,largest)
                
        
        for i in reversed(range(len(arr))):
            heapify_algo(arr,i)
        return arr
            
    def insert(self,val):
        self.size+=1
        self.arr.append(val)
        index=self.size-1
        while index>=1:
            parent=index//2
            if self.arr[index]>self.arr[parent]:
                self.arr[index],self.arr[parent]=self.arr[parent],self.arr[index]
                index=parent
            else:
                return
    def deletenode(self,index):
        if self.size==0:
            return 
        
        self.arr[index]=self.arr[len(self.arr)-1]
        self.arr.pop()
        i=0
        while i<len(self.arr):
            li=2*i+1
            ri=2*i+2
            if li<len(self.arr) and self.arr[li]>self.arr[i]:
                self.arr[i],self.arr[li]=self.arr[li],self.arr[i]
                i=li
            elif ri<len(self.arr) and self.arr[ri]>self.arr[i]:
                self.arr[i],self.arr[ri]=self.arr[ri],self.arr[i]
                i=ri
            else:
                return

    def printt(self):
        print(self.arr)
h=Max_Heap([34,56,3,26,768,343])
h.heapify()
h.insert(300)
h.printt()
h.deletenode(5)
h.printt()


# ## Min Heap

# In[54]:


#Min Heap
class Min_Heap:
    def __init__(self,arr):
        self.arr=arr
        self.size=len(arr)
    #maxheap
    def heapify(self):
        arr=self.arr
        def heapify_algo(arr,i):
            smallest=i
            li=2*i+1
            ri=2*i+2
            
            if li<len(arr) and arr[li]<arr[smallest]:
                smallest=li
            if ri<len(arr) and arr[ri]<arr[smallest]:
                smallest=ri
            if smallest!=i:
                arr[i],arr[smallest]=arr[smallest],arr[i]
                heapify_algo(arr,smallest)
                
        
        for i in reversed(range(len(arr))):
            heapify_algo(arr,i)
        return arr
            
    def insert(self,val):
        self.size+=1
        self.arr.append(val)
        index=self.size-1
        while index>=1:
            parent=index//2-1
            if self.arr[index]<self.arr[parent]:
                self.arr[index],self.arr[parent]=self.arr[parent],self.arr[index]
                index=parent
            else:
                return
    def deletenode(self,index):
        if self.size==0:
            return 
        
        self.arr[index]=self.arr[len(self.arr)-1]
        self.arr.pop()
        i=0
        while i<len(self.arr):
            li=2*i+1
            ri=2*i+2
            if li<len(self.arr) and self.arr[li]<self.arr[i]:
                self.arr[i],self.arr[li]=self.arr[li],self.arr[i]
                i=li
            elif ri<len(self.arr) and self.arr[ri]<self.arr[i]:
                self.arr[i],self.arr[ri]=self.arr[ri],self.arr[i]
                i=ri
            else:
                return

    def printt(self):
        print(self.arr)
h=Min_Heap([34,56,3,26,768,343])
h.heapify()
h.insert(300)
h.printt()
h.deletenode(5)
h.printt()


# ## Heap Sort
# 

# In[22]:


def heapify(arr,n,i):
    largest=i
    li=2*i+1
    ri=2*i+2
    
    if li<n and arr[largest]<arr[li]:
        largest=li
    if ri<n and arr[largest]<arr[ri]:
        largest=ri
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
    
def heapsort(arr):
#     n=len(arr)
#build max heap
    for i in reversed(range(n//2)):
        heapify(arr,n,i)
    print(arr)
    
    for i in reversed(range(1,n)):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr = [1, 12, 9, 5, 6, 10]
heapsort(arr)


n = len(arr)
arr


# In[ ]:





'''
Created on 5 May, 2014

@author: xiao8
'''

def sum2(a, b):
    return a + b

def min1(a):
    min1 = a[0]
    for i in a:
        if i < min1:
            min1 = i
    return min1
        
print('test2 not from __nam_')

if __name__ == '__main__':
    print('test 2')
    print(min1([10,2,3,4,5,6]))
    

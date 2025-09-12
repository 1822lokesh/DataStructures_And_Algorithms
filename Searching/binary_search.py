list=[10,20,30,40,50]
low=0
high=len(list)-1
key=int(input("enter a key: "))
found=False
while low <=high :
        mid=(low+high)//2
        if key==list[mid]:
            print("key found")
            found=True
            break
        elif key < list[mid]:
             high=mid-1
        else:
             low=mid+1
if not found:
    print("Element not found")


        

    






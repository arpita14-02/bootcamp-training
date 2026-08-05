numbers = [2,7,11,15], target = 9
low=0
high=len(numbers)-1
while(low<high):
            if (numbers[low]+numbers[high])==target:
                print(low+1,high+1)
            elif (numbers[low]+numbers[high])>target:
                high-=1
            elif(numbers[low]+numbers[high])<target:
                low+=1
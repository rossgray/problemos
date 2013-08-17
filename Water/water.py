# Python 3

def findWaterInCup(cup, total_water, cup_capacity):
    ''' There is a pyramid with 1 cup at level 1, 2 cups at level 2, 3 at level 3 and so on...
        It looks something like this 
               1 
              2 3 
             4 5 6 
        Every cup has capacity C. You pour amount L of water from the top of the pyramid. 
        When cup 1 gets filled it overflows to cup 2 & 3 equally, and when they get filled,
        Cup 4 and 6 get water only from 2 and 3 respectively but 5 gets water from both the cups and so on. 
        Given C and M, find the amount of water in the ith cup.'''

    if cup == 1:
        return min(cup_capacity, total_water)

    # l = level number, i = first cup on level l    
    l=1
    i=1
    water_amt = total_water
    while True:
        i+=l
        l+=1
        # caculate total amount of water on this level
        new_water_amt = water_amt-(l-1)*cup_capacity
        water_amt = max(new_water_amt, 0)

        #check if desired cup is on this level
        if cup < i+l:
            # cup is on this level
            # now check if the cup is on the outside or the inside of the row
            if (cup == i) or (cup == i+l-1):
                # outside cup
                return min(water_amt/(2*(l-1)), cup_capacity)
            else:
                #inside cup
                return min(water_amt/(l-1), cup_capacity)

        
print(findWaterInCup(3, 10, 5))
print(findWaterInCup(5, 20, 3))
print(findWaterInCup(6, 20, 5))

                   

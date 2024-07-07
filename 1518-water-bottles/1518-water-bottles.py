class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        total_drinkable_bottles = num_bottles
           
        while num_bottles >= num_exchange:
            num_bottles = num_bottles - num_exchange + 1
            total_drinkable_bottles += 1
        return total_drinkable_bottles
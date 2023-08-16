#!/usr/bin/python3
def weight_average(my_list=[]):
   if not my_list:
        return 0
   total_sum = 0
   no_of_items = 0

   for pair in my_list:
        total_sum += pair[0] * pair[1]
        no_of_items += pair[1]

   return (total_sum / no_of_items)

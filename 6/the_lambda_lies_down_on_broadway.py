square_of_sum_of_first_n_ints = lambda x: int(((x * (x + 1))/2)**2) # Make Gauss proud :)
sum_of_first_n_squares = lambda x: sum([i**2 for i in range(1, x+1)])

print(square_of_sum_of_first_n_ints(100) - sum_of_first_n_squares(100))

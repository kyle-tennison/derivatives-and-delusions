import despair as d


x, y, z = d.symbols("x, y, z")

all_of_my_homework_problems_that_i_hate = [
    2*x + 4*y + z, # == 0
    2*x - 2,
    y+4,
]


x, y, z = d.solve_eoe(all_of_my_homework_problems_that_i_hate, (x, y, z))

d.splendid() #   yeah pretty splendid
def calculate_daily_house_points(spells_cast, points_made, quidditch_wins):
    return(spells_cast*10 + points_made*20 + quidditch_wins*150)

print(calculate_daily_house_points(5,3,2))
print(calculate_daily_house_points(15,5,1))

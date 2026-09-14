game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

#we can print new enemy even though if it is embedded inside if function
# if game_level < 5 :
#     new_enemy = enemies[0]
#
# print(new_enemy)

#we cant print new enemy cause we enclosed it in a def function
def create_enemy():
    new_enemy = ""
    if game_level < 5 :
        new_enemy = enemies[0]

    print(new_enemy)
create_enemy()
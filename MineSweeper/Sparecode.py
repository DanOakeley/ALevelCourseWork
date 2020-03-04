#create bombs on the screen (each tile is 20 x 20 so alter cords)
TotalBombs = 0
bombLocations = []
for y in range(50):
    for x in range(50):
        while TotalBombs <=2:
            #cordinates of bomb
#            bombX = random.randrange(10,40,30)
#            bombY = random.randrange(10,40,30)
            #if statement to check if bombs already exist on that locaton
            my_bomb = tile(WHITE, 30, 30, random.randrange(10,40,30), random.randrange(10,40,30))
            bomb_list.add(my_bomb)
            all_sprites_list.add(my_bomb)
            TotalBombs = TotalBombs + 1

from host import GO

print("hey")

game = GO(5)
print(game)

game.init_board(5)

game.visualize_board()
game.play()
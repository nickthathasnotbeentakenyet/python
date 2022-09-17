from draw2d import \
    start_drawing, draw_line, draw_oval, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

# COMMENT: FUNCTIONS' CALLS START HERE 
    # draw_grid(canvas, scene_width, scene_height, 50)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas, 0, 480, 80)
    draw_cloud(canvas, 150, 350, 80)
    draw_cloud(canvas, 550, 430, 60)
    draw_cloud(canvas, 750, 400, 80)
    draw_tractor(canvas, 500, 150)
    draw_tree(canvas, 100, 100, 10)
    draw_tree(canvas, 300, 150, 5)
    draw_birds(canvas, 170, 440, 7)
    draw_birds(canvas, 250, 400, 8)
    draw_birds(canvas, 280, 470, 5)
    draw_fruits(canvas, 75, 230, 10, "red")
    draw_fruits(canvas, 80, 270, 12, "gold")
    draw_fruits(canvas, 125, 220, 15, "yellow")
    draw_fruits(canvas, 90, 210, 12, "goldenrod")
    draw_fruits(canvas, 110, 260, 15, "orange")
    draw_fruits(canvas, 280, 220, 10, "goldenrod")
    draw_fruits(canvas, 310, 210, 12, "crimson")
    draw_fruits(canvas, 290, 190, 12, "firebrick1")
    draw_grass(canvas, 200, 50, 12)
    draw_grass(canvas, 90, 100, 9)
    draw_grass(canvas, 250, 150, 7)
    draw_grass(canvas, 270, 125, 6)
    draw_grass(canvas, 650, 0, 13)
    draw_grass(canvas, 470, 0, 13)
    draw_grass(canvas, 490, 0, 17)
    draw_rocks(canvas, 460, -10, 20)
    draw_rocks(canvas, 100, -30, 40)
    draw_rocks(canvas, 700, -30, 70)
    draw_butterfly(canvas, 130, 180, 15, "mediumPurple1")
    draw_butterfly(canvas, 150, 20, 16, "skyblue1")
    draw_butterfly(canvas, 350, 270, 10, "maroon4")
    draw_butterfly(canvas, 660, 20, 8, "greenYellow")
    draw_butterfly(canvas, 710, 30, 12, "mediumPurple1")
    
# COMMENT: CALLS TO MY FUNCTIONS END HERE

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# COMMENT: FUNCTIONS' DECLARATION START HERE

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky"""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground"""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="forestGreen")

def draw_cloud(canvas, x, y, diameter):
    """Draw white cloud at a given position and size"""
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill="white", outline="white")
    draw_oval(canvas, x+30, y-10, x+30 + diameter*.7, y-10 + diameter*.7, fill="white", outline="white")
    draw_oval(canvas, x+40, y+10, x+30 + diameter, y-10 + diameter, fill="white", outline="white")
    draw_oval(canvas, x-15, y-15, x + diameter*.7, y + diameter*.7, fill="white", outline="white")
    draw_oval(canvas, x-30, y, x-30 + diameter*.8, y + diameter*.8, fill="white", outline="white")

def draw_grass(canvas, x, y, size):
    """Draw grass bushes. Sizes and placements on the ground vary"""
    draw_polygon(canvas, x, y, x-size*.8, y+size*3, x+size*2, y, outline="paleTurquoise4", fill="green")
    draw_polygon(canvas, x, y, x+size, y+size*5, x+size*2, y, outline="paleTurquoise4", fill="green")
    draw_polygon(canvas, x+size, y, x+size*3, y+size*4, x+size*2, y, outline="paleTurquoise4", fill="green")

def draw_rocks(canvas, x, y, size):
    """Draw rock on the ground"""
    draw_oval(canvas, x+size*.5, y, x+size*2, y+size*1.5, outline="#333", fill="#333")
    draw_oval(canvas, x, y, x+size, y+size, outline="paleTurquoise4", fill="#333")

def draw_butterfly(canvas, x, y, size, color):
    """Draw butterfly of a different color, size and position on the matrix"""
    draw_oval(canvas, x, y, x+size, y+size, outline="#333", fill=color)
    draw_oval(canvas, x+size, y, x+size*2, y+size, outline="#333", fill=color)
    draw_oval(canvas, x+size*.5, y, x+size, y-size*.5, outline="#333", fill=color)
    draw_oval(canvas, x+size, y, x+size*1.5, y-size*.5, outline="#333", fill=color)
    draw_line(canvas, x+size, y+size*.5, x+size*.5, y+size*1.5, width=2, fill="#333")
    draw_line(canvas, x+size, y+size*.5, x+size*1.5, y+size*1.5, width=2, fill="#333")
    draw_oval(canvas, x+size*.5, y+size*1.5, x+size*.5-7, y+size*1.5+7, outline="#333", fill="#333")
    draw_oval(canvas, x+size*1.5, y+size*1.5, x+size*1.5+7, y+size*1.5+7, outline="#333", fill="#333")
    draw_line(canvas, x+size, y+size, x+size, y-size*.5, width=5, fill="#333")


def draw_birds(canvas, x, y, size):
    """Draw simple bird in the sky"""
    draw_line(canvas, x, y, x+size, y+size, width=3.5, fill="gray30")
    draw_line(canvas, x+1, y-1, x-size, y+size, width=3.5, fill="gray30")

def draw_tree(canvas, x, y, size):
    """Draw a lonely placed tree. The size is to bring trees closer and further for the observer"""
    draw_rectangle(canvas, x, y, x+size*1.7, y+size*10, width=0, outline="saddlebrown", fill="saddleBrown")
    draw_oval(canvas, x-size*5, y+size*10-10, x+size*5+size, y+size*20, outline="forestgreen", fill="forestgreen" )
    draw_oval(canvas, x, y-size*.6, x+size*15, y+size*.2, outline="darkgreen", fill="darkgreen")

def draw_fruits(canvas, x, y, size, color):
    """Draws fruits of different size and color with a little stick that holds them to the tree"""
    draw_oval(canvas, x, y, x+size, y+size, outline=color, fill=color)
    draw_line(canvas, x+size/2, y+size, x+size/2, y+size*1.5, fill="#333" )

def draw_tractor(canvas, x, y):
    """Draw a moving tractor"""
    draw_rectangle(canvas, x, y, x+100, y+40, width=1, outline="skyBlue4", fill="cadetBlue4") # engine
    draw_rectangle(canvas, x+100, y, x+200, y+100, width=1, outline="skyBlue4", fill="slateGray4") # driver's seat
    draw_rectangle(canvas, x+125, y+50, x+175, y+80, width=1, outline="skyBlue4", fill="sky Blue") # window
    draw_rectangle(canvas, x+20, y+40, x+10, y+70, width=1, outline="skyBlue4", fill="cadetBlue4") # chimney
    draw_line(canvas, x+45, y-20, x+300, y-20, width=20, fill="lightsalmon4") # dirt
    draw_line(canvas, x+70, y-15, x+120, y-15, width=3, fill="#333") # dirt2
    draw_line(canvas, x+90, y-25, x+140, y-25, width=3, fill="#333") # dirt3
    draw_line(canvas, x+210, y-15, x+240, y-15, width=3, fill="#333") # dirt4
    draw_line(canvas, x+250, y-15, x+290, y-15, width=3, fill="#333") # dirt5
    draw_line(canvas, x+220, y-25, x+280, y-25, width=3, fill="#333") # dirt6
    draw_line(canvas, x+190, y+25, x+230, y+120, width=5, fill="slateGray4") # tool
    draw_line(canvas, x+230, y+120, x+260, y+40, width=5, fill="slateGray4") # tool2
    draw_polygon(canvas, x+260, y+40, x+250, y+65, x+235, y+25, width=0, outline="slateGray4", fill="slateGray4")
    draw_oval(canvas, x+20, y-30, x+65, y+15, fill="#333", outline="#333") # front tire
    draw_oval(canvas, x+30, y-20, x+55, y+5, fill="saddlebrown", outline="saddlebrown") # front wheel
    draw_text(canvas, x+43, y-7, "x", fill="#333")
    draw_oval(canvas, x+130, y-30, x+210, y+55, fill="#333", outline="#333") # back tire
    draw_oval(canvas, x+140, y-20, x+200, y+45, fill="saddlebrown", outline="saddlebrown") # back wheel
    draw_text(canvas, x+170, y+13, "X", fill="#333")
    draw_oval(canvas, x+10, y+80, x+20, y+90, fill="gray30", outline="gray30") # puff1
    draw_oval(canvas, x+40, y+120, x+60, y+140, fill="gray30", outline="gray30") # puff2
    draw_oval(canvas, x+50, y+130, x+70, y+150, fill="gray30", outline="gray30") # puff2+
    draw_oval(canvas, x+50, y+120, x+70, y+140, fill="gray30", outline="gray30") # puff2+
    draw_oval(canvas, x+60, y+125, x+80, y+145, fill="gray30", outline="gray30") # puff2+
    draw_oval(canvas, x+110, y+170, x+150, y+210, fill="gray30", outline="gray30") # puff3
    draw_oval(canvas, x+100, y+160, x+140, y+200, fill="gray30", outline="gray30") # puff3+
    draw_oval(canvas, x+135, y+170, x+175, y+210, fill="gray30", outline="gray30") # puff3+
    draw_oval(canvas, x+122, y+150, x+162, y+190, fill="gray30", outline="gray30") # puff3+
    draw_oval(canvas, x+150, y+160, x+190, y+200, fill="gray30", outline="gray30") # puff3+
    draw_text(canvas, x+50, y+30, "General Motors", fill="gold") # text on the engine section

# NOTE: the grid function is left for future needs. Call to this function is disabled.
def draw_grid(canvas, width, height, interval, color="#333"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)
# NOTE: END of note
# COMMENT: FUNCTIONS' DECLARATIONS END HERE

# Call the main function so that
# this program will start executing.
main()


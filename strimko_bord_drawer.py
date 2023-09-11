from  PIL import Image ,ImageDraw, ImageFont



# I can take the input matrixes in format like this :
# strimko_bord = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 4, 0], [0, 3, 0, 1]]
# chains = [['00', '11', '22', '32'], ['01', '10', '20', '31'], ['02', '12', '21', '30'], ['03', '13', '23', '33']]

def draw_strimko_bord(strimko_bord, chains):
    bs=128 # Bluck size
    size=len(strimko_bord)
    total_size=size*bs

    # Contrasting
    main_output=Image.new('RGBA',(total_size,total_size), "white") # You can change the color syle
    draw = ImageDraw.Draw(main_output)

    fnt = ImageFont.truetype("arial.ttf", 40) # You can use other fonts as will
    line_color = (0, 0, 0)  # Black in RGB
    line_width = 7 # You can use other widths as will
    
    # drawing chain
    for chain in range (size):
        for state in range(size-1): # Evry state in a chain
            start_X=(int(chains[chain][state][1]))*bs+(bs/2)
            start_Y=(int(chains[chain][state][0]))*bs+(bs/2)

            line_end_X=(int(chains[chain][state+1][1]))*bs+(bs/2)
            line_end_Y=(int(chains[chain][state+1][0]))*bs+(bs/2)
            
            line_start=(start_X,start_Y)
            line_end=(line_end_X,line_end_Y)
            
            draw.line((line_start,line_end),fill=line_color,width=line_width)

    # drawing circles and values
    radius=32
    for x in range (size):
        for y in range (size):
            centerX =(y * bs )+ (bs / 2)
            centerY =(x * bs )+(bs / 2 )
            draw.ellipse((centerX-radius,centerY-radius,centerX+radius,centerY+radius),fill=(230,230,230),outline='black',width=3)
            center_loc=(centerX, centerY)
            this_vlue=str(strimko_bord[x][y])
            #draw.text(center_loc, this_vlue, font=fnt)
            draw.text(center_loc, this_vlue, font=fnt, fill=(0, 0, 0), anchor='mm')
    main_output.show()

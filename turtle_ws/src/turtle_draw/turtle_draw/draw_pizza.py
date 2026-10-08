# converting pizza pic into
image= [ '16w',
        '4w4b8w',
        '4w1b3br2b6w',
        '4w3b3br1b5w',
        '3w1b3y2b2br1b4w',
        '3w3b3y1b2br1b3w',
        '3w1b2r1b4y1b2br1b2w',
        '2w1b1y2b3y2b1y1b1br1b2w',
        '2w1b5y1b2r1b1y1b1br1b',
        '2w1b6y2b1y1b1br1b1w',
        '1w1b2y2b7y2b1w',
        '1w1b1y1b2r1b1y5b3w',
        '1w1b1y1b1r4b7w',
        '1w4b11w'
    ]

# [[(16,'w')],
#  [(4,'w'),(4,'b'),(8,'w')]
#  ,...]

#maping RGB colours used in image with letters using in array
colors = {
    'w': (255, 255, 255),
    'b': (0, 0, 0),
    'y': (255, 215, 0),
    'r': (255, 0, 0),
    'br': (165, 42, 42)
}

image_pairs= []

for row in image:
    #pix=[x for x in row]
    i=0
    #d=0
    rows=[]

    while(i <len(row)):
        
        d=0
        curr_color=''
        curr_count=''
        while (i + d  < len(row)) and row[i + d].isdigit():
            
            curr_count=curr_count+ row[i+d]
            d+=1
        #curr_count=int(curr_count)

        while (i + d < len(row)) and row[i + d].isalpha():
            
            curr_color=curr_color+row[i+d]
            d+=1

        row_tup=(int(curr_count),curr_color)
        i=i+d
            
        rows.append(row_tup)

    image_pairs.append(rows)
print(image_pairs)
    


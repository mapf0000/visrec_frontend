import json

def convert_coordinates():
    with open("region_attributes.json", "r") as read_file:
        data = json.load(read_file)

    for metadata_id in data['_via_img_metadata']:
        for region in data['_via_img_metadata'][metadata_id]['regions']:
            x_coord = list(region['shape_attributes']['all_points_x'])
            y_coord = list(region['shape_attributes']['all_points_y'])
            print('Coordinates:')
            coord_fmt = ''
            for x,y in zip(x_coord, y_coord):
                if coord_fmt == '':
                    coord_fmt = str(x) + ',' + str(y)
                else:
                    coord_fmt += ',' +  str(x) + ',' + str(y)
                    
            print(coord_fmt)

convert_coordinates()
import xml.etree.ElementTree

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def bounding_box_of_points(
    point_arr # # [{"x": integer, "y": integer}, ...]
    ):
    min_x = None
    min_y = None
    max_x = None
    max_y = None

    for pt in point_arr:
        if min_x is None or pt.x < min_x:
            min_x = pt.x
        if max_x is None or pt.x > max_x:
            max_x = pt.x
        
        if min_y is None or pt.y < min_y:
            min_y = pt.y
        if max_y is None or pt.y > max_y:
            max_y = pt.y
        
    return min_x, min_y, max_x, max_y

def convert_xml_labels_to_csv_lines(xml_text):
    annotation_el = xml.etree.ElementTree.fromstring(xml_text)
    filename_string = annotation_el.find("filename").text

    csv_lines = []
    for object_el in annotation_el.findall("object"):
        obj_name_string = object_el.find("name").text

        point_coords = [] # [{"x": integer, "y": integer}, ...]
        
        for point_el in object_el.find("polygon").findall("pt"):
            x = int(point_el.find("x").text)
            y = int(point_el.find("y").text)
            point_coords.append(Point(x, y))
        
        min_x, min_y, max_x, max_y = bounding_box_of_points(point_coords)

        csv_line = (
            filename_string + "," +
            str(min_x) + "," +
            str(min_y) + "," +
            str(max_x) + "," +
            str(max_y) + "," +
            obj_name_string
        )
        csv_lines.append(csv_line)
    
    return csv_lines
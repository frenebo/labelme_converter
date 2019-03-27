import xml.etree.ElementTree

def bounding_box_of_points(
    point_arr # # [{"x": integer, "y": integer}, ...]
    ):
    min_x = None
    min_y = None
    max_x = None
    max_y = None

    for point_info in point_arr:
        if min_x is None or point_info["x"] < min_x:
            min_x = point_info["x"]
        if max_x is None or point_info["x"] > max_x:
            max_x = point_info["x"]
        
        if min_y is None or point_info["y"] < min_y:
            min_y = point_info["y"]
        if max_y is None or point_info["y"] > max_y:
            max_y = point_info["y"]
        
    return min_x, min_y, max_x, max_y


def convert_xml_labels_to_csv_lines(xml_text):
    annotation_el = xml.etree.ElementTree.fromstring(xml_text)
    filename_string = annotation_el.find("filename").text

    csv_lines = []
    for object_el in annotation_el.findall("object"):
        obj_name_string = object_el.find("name").text

        point_coords = [] # [{"x": integer, "y": integer}, ...]
        
        for point_el in object_el.find("polygon").findall("pt"):
            point_coords.append({
                "x": int(point_el.find("x").text),
                "y": int(point_el.find("y").text),
            })
        
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
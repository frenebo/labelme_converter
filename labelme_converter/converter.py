import xml.etree.ElementTree
import csv
import io

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def bounding_box_of_points(
    points # list of Point classes
    ):
    min_x = None
    min_y = None
    max_x = None
    max_y = None

    for pt in points:
        if min_x is None or pt.x < min_x:
            min_x = pt.x
        if max_x is None or pt.x > max_x:
            max_x = pt.x
        
        if min_y is None or pt.y < min_y:
            min_y = pt.y
        if max_y is None or pt.y > max_y:
            max_y = pt.y
        
    return min_x, min_y, max_x, max_y

def create_csv_line(*element_strings):
    csv_output = io.StringIO()
    
    # Line terminator is "" because only one line is going to be returned, without a newline
    csv_writer = csv.writer(csv_output, lineterminator="")
    csv_writer.writerow(element_strings)
    
    return csv_output.getvalue()

def convert_xml_labels_to_csv_lines(xml_text):
    annotation_el = xml.etree.ElementTree.fromstring(xml_text)
    filename_string = annotation_el.find("filename").text
    folder_string = annotation_el.find("folder").text
    # file_path = folder_string + "/" + filename_string
    file_path = filename_string # don't include folder path for now

    csv_lines = []
    for object_el in annotation_el.findall("object"):
        obj_name_string = object_el.find("name").text

        points = []
        
        for point_el in object_el.find("polygon").findall("pt"):
            x = int(point_el.find("x").text)
            y = int(point_el.find("y").text)
            
            points.append(Point(x, y))
        
        min_x, min_y, max_x, max_y = bounding_box_of_points(points)

        csv_line = create_csv_line(
            file_path,
            str(min_x),
            str(min_y),
            str(max_x),
            str(max_y),
            obj_name_string
        )
        csv_lines.append(csv_line)
    
    # One placeholder line for images with no annotations. ex: "some_folder/image.jpg,,,,,"
    if len(csv_lines) == 0:
        return [
            create_csv_line(
                file_path,
                "",
                "",
                "",
                "",
                "",
            )
        ]
    else:
        return csv_lines

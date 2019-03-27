
if __name__ == "__main__":
    from labelme_converter import convert_xml_labels_to_csv_lines

    with open("example_annotations.xml", "r") as example_file:
        converted_lines = convert_xml_labels_to_csv_lines(example_file.read())
    
    
    print(converted_lines)

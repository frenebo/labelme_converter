
if __name__ == "__main__":
    from labelme_converter import convert_xml_labels_to_csv_lines

    example_files = ["example_annotations.xml", "example_no_annotations.xml"]
    for file_name in example_files:
        with open(file_name, "r") as example_file:
            converted_lines = convert_xml_labels_to_csv_lines(example_file.read())
            print(file_name + ":")
            for line in converted_lines:
                print("    " + line)
            # print(converted_lines)

from labelme_converter import convert_xml_labels_to_csv_lines
import sys
import os

if __name__ == "__main__":
    source_dir_name = sys.argv[1]
    target_csv_filename = sys.argv[2]
    print(source_dir_name)
    print(target_csv_filename)

    with open(target_csv_filename, "w+") as csv_file:
        for xml_filename in os.listdir(source_dir_name):
            xml_filepath = os.path.join(source_dir_name, xml_filename)
            with open(xml_filepath) as xml_file:
                csv_lines = convert_xml_labels_to_csv_lines(xml_file.read())
                for line in csv_lines:
                    csv_file.write(line + "\n")

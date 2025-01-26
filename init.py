import os
import json
import re
import shutil

def load_metadata(meta_file):
    with open(meta_file, 'r') as file:
        return json.load(file)

def replace_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()
    
    for old, new in replacements.items():
        content = re.sub(re.escape(old), new, content)

    with open(file_path, 'w') as file:
        file.write(content)
    
    print(f"Updated file: {file_path}")

def rename_package_path(base_path, old_package, new_package):
    old_path = os.path.join(base_path, *old_package.split('.'))
    new_path = os.path.join(base_path, *new_package.split('.'))

    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"Renamed package path from {old_path} to {new_path}.")
    else:
        print(f"Warning: Old package path '{old_path}' does not exist!")

def update_gradle_file(gradle_file, metadata):
    replacements = {
        "$(name)": metadata["name"],
        "$(details)": metadata["details"],
        "$(version_name)": metadata["version_name"],
        "$(version_code)": metadata["version_code"],
        "$(application_id)": metadata["new_package"]
    }
    replace_in_file(gradle_file, replacements)

def update_strings_xml(strings_xml_path, metadata):
    if not os.path.exists(strings_xml_path):
        print(f"Warning: strings.xml not found at {strings_xml_path}")
        return

    with open(strings_xml_path, 'r') as file:
        content = file.read()

    updated_content = re.sub(r'(<string\s+name="app_name">)(.*?)(</string>)', rf'\1{metadata["name"]}\3', content)
    updated_content = re.sub(r'(<string\s+name="app_details">)(.*?)(</string>)', rf'\1{metadata["details"]}\3', updated_content)

    with open(strings_xml_path, 'w') as file:
        file.write(updated_content)

    print(f"Updated app_name to '{metadata['name']}' and app_details to '{metadata['details']}' in strings.xml.")

def update_source_files(source_dir, old_package, new_package):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".java") or file.endswith(".kt"):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, {f"package {old_package}": f"package {new_package}"})
                print(f"Updated package name in {file_path}")

def process_android_project(meta_file_path):
    if not os.path.exists(meta_file_path):
        print(f"Error: Metadata file not found at {meta_file_path}")
        return

    metadata = load_metadata(meta_file_path)

    required_keys = ["old_package", "new_package", "name", "details", "version_name", "version_code"]
    for key in required_keys:
        if key not in metadata:
            print(f"Error: Missing key '{key}' in metadata file.")
            return

    app_src_main_java = os.path.abspath("app/src/main/java/")
    gradle_file = os.path.abspath("app/build.gradle")
    strings_xml_path = os.path.abspath("app/src/main/res/values/strings.xml")

    update_source_files(app_src_main_java, metadata["old_package"], metadata["new_package"])
    rename_package_path(app_src_main_java, metadata["old_package"], metadata["new_package"])
    update_gradle_file(gradle_file, metadata)
    update_strings_xml(strings_xml_path, metadata)

    print("Project renaming and updates complete!")

if __name__ == "__main__":
    meta_file_path = os.path.abspath("./_meta.json")
    process_android_project(meta_file_path)

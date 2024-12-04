import os
import json
import re
import shutil

def load_metadata(meta_file):
    """Load metadata from the JSON file."""
    with open(meta_file, 'r') as file:
        return json.load(file)
def replace_in_file(file_path, replacements):
    """Replace text in a file based on a dictionary of replacements."""
    with open(file_path, 'r') as file:
        content = file.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(file_path, 'w') as file:
        file.write(content)
def rename_package_path(base_path, old_package, new_package):
    """Rename the package directory path."""
    old_path = os.path.join(base_path, *old_package.split('.'))
    new_path = os.path.join(base_path, *new_package.split('.'))
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"Renamed package path from {old_path} to {new_path}.")
    else:
        print(f"Old package path {old_path} does not exist!")
def update_gradle_file(gradle_file, app_name, version_name, version_code, new_package):
    """Update the app's Gradle build file."""
    replacements = {
        "$(name)": app_name,
        "$(version_name)": version_name,
        "$(version_code)": version_code,
        "$(application_id)": new_package
    }
    replace_in_file(gradle_file, replacements)
    print(f"Updated Gradle file: {gradle_file}.")
def update_app_name(strings_xml_path, app_name):
    """Update the app_name in the strings.xml file."""
    if not os.path.exists(strings_xml_path):
        print(f"strings.xml not found at: {strings_xml_path}")
        return
    with open(strings_xml_path, 'r') as file:
        content = file.read()
    updated_content = re.sub(
        r'(<string name="app_name">)(.*?)(</string>)',
        rf'\1{app_name}\3',
        content
    )
    with open(strings_xml_path, 'w') as file:
        file.write(updated_content)
    print(f"Updated app_name to '{app_name}' in strings.xml.")
def process_android_project(meta_file_path):
    """Process the Android project to update package name, app name, and Gradle configuration."""
    metadata = load_metadata(meta_file_path)
    old_package = metadata["old_package"]
    new_package = metadata["new_package"]
    app_name = metadata["name"]
    version_name = metadata["version_name"]
    version_code = metadata["version_code"]
    app_src_main_java = "app/src/main/java/"
    gradle_file = "app/build.gradle"
    strings_xml_path = "app/src/main/res/values/strings.xml"
    for root, _, files in os.walk(app_src_main_java):
        for file in files:
            if file.endswith(".java") or file.endswith(".kt"):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, {f"package {old_package}": f"package {new_package}"})
    rename_package_path(app_src_main_java, old_package, new_package)
    update_gradle_file(gradle_file, app_name, version_name, version_code, new_package)
    update_app_name(strings_xml_path, app_name)
    print("Project renaming complete!")

if __name__ == "__main__":
    meta_file_path = "./_meta.json"
    if not os.path.exists(meta_file_path):
        print(f"Metadata file not found: {meta_file_path}")
    else:
        process_android_project(meta_file_path)

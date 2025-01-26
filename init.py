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
    print(f"Updated file: {file_path}")

def rename_package_path(base_path, old_package, new_package):
    """Rename the package directory path."""
    old_path = os.path.join(base_path, *old_package.split('.'))
    new_path = os.path.join(base_path, *new_package.split('.'))
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"Renamed package path from {old_path} to {new_path}.")
    else:
        print(f"Old package path {old_path} does not exist!")

def update_gradle_file(gradle_file, app_name, details, version_name, version_code, new_package):
    """Update the app's Gradle build file."""
    replacements = {
        "$(name)": app_name,
        "$(details)": details,
        "$(version_name)": version_name,
        "$(version_code)": version_code,
        "$(application_id)": new_package
    }
    replace_in_file(gradle_file, replacements)

def update_strings_xml(strings_xml_path, app_name, details):
    """Update the app_name and app_details in the strings.xml file."""
    if not os.path.exists(strings_xml_path):
        print(f"strings.xml not found at: {strings_xml_path}")
        return

    with open(strings_xml_path, 'r') as file:
        content = file.read()

    # Replace placeholders dynamically
    updated_content = re.sub(r'(<string\s+name="app_name">)(.*?)(</string>)', rf'\1{app_name}\3', content)
    updated_content = re.sub(r'(<string\s+name="app_details">)(.*?)(</string>)', rf'\1{details}\3', updated_content)

    with open(strings_xml_path, 'w') as file:
        file.write(updated_content)
    print(f"Updated app_name to '{app_name}' and app_details to '{details}' in strings.xml.")

def process_android_project(meta_file_path):
    """Process the Android project to update package name, app name, and Gradle configuration."""
    metadata = load_metadata(meta_file_path)

    # Ensure required keys exist in the metadata
    required_keys = ["old_package", "new_package", "name", "details", "version_name", "version_code"]
    for key in required_keys:
        if key not in metadata:
            print(f"Error: Missing key '{key}' in metadata file.")
            return

    old_package = metadata["old_package"]
    new_package = metadata["new_package"]
    app_name = metadata["name"]
    details = metadata["details"]
    version_name = metadata["version_name"]
    version_code = metadata["version_code"]

    app_src_main_java = "app/src/main/java/"
    gradle_file = "app/build.gradle"
    strings_xml_path = "app/src/main/res/values/strings.xml"

    # Update package name in Java/Kotlin files
    for root, _, files in os.walk(app_src_main_java):
        for file in files:
            if file.endswith(".java") or file.endswith(".kt"):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, {f"package {old_package}": f"package {new_package}"})

    # Rename package directories
    rename_package_path(app_src_main_java, old_package, new_package)

    # Update Gradle build file
    update_gradle_file(gradle_file, app_name, details, version_name, version_code, new_package)

    # Update strings.xml
    update_strings_xml(strings_xml_path, app_name, details)

    print("Project renaming complete!")

if __name__ == "__main__":
    meta_file_path = "./_meta.json"
    if not os.path.exists(meta_file_path):
        print(f"Metadata file not found: {meta_file_path}")
    else:
        process_android_project(meta_file_path)

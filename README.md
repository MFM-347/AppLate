# AppLate

Android **App Template** with GitHub Workflow Build

This template automates building Android APK and AAB files using GitHub Actions, supporting debug builds and uploading build artifacts for distribution. The workflow being used is manually triggered.

## Features

1. **Automated CI/CD with GitHub Actions** for building Android APKs and AABs.
2. **Customizable Project Setup** using an initialization script.
3. **Environment Variables for Secure Signing** of builds.
4. **Manual Trigger Workflow** for controlled release management.
5. **Easy Artifact Download** directly from GitHub Actions.

## Usage

### Initialize Your Project

1. Run the `init.py` script to set up your Android project metadata:

   - Updates package name, app name, and version details in the source code.
   - Configures secrets for GitHub workflows.

   ```bash
   python init.py
   ```

````
The script reads metadata from a `_meta.json` file. Example structure:

```json
{
  "old_package": "dev.mfm.app",
  "new_package": "com.package.new",
  "name": "NewAppName",
  "version_name": "1.0.0",
  "version_code": "1"
}
```

2. Verify your Android project files are updated correctly:
   - `strings.xml`: Contains the updated app name.
   - `build.gradle`: Updated with the new app name, version name, and version code.
   - Package directory structure updated for the new package name.

### Add Environment Variables

2. **Keystore Information**:
   - Add secrets to sign your builds:
     - `KEYSTORE_BASE_64`, `DEBUG_KEYSTORE_PASSWORD`, `DEBUG_KEYSTORE_ALIAS`, `DEBUG_KEY_PASSWORD`.

### Run GitHub Actions Workflows

1. Trigger workflows from the **Actions** tab:

   - Select **Build release-app** for production builds.
   - Select **Build debug-app** for testing builds.

2. Download artifacts (`release-build.zip` or `debug-build.zip`) from the workflow run.

## Credits

This workflow was inspired by **Lloyd Dcosta**'s guide on [Medium](https://medium.com/@dcostalloyd90/automating-android-builds-with-github-actions-a-step-by-step-guide-2a02a54f59cd) and enhanced by [@MFM-347](https://github.com/MFM-347).

## License

The code in this repository is licensed under the **Apache 2.0 License**.

[![License](https://img.shields.io/badge/License-Apache_2.0-0298c3.svg)](https://opensource.org/licenses/Apache-2.0)
````

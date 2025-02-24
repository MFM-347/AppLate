# AppLate - Android CI/CD Template

![API](https://img.shields.io/badge/Api%2021+-f4f5f6?logo=android&logoColor=black&style=for-the-badge)
![Java](https://img.shields.io/badge/Java-red?logo=Java&logoColor=white&style=for-the-badge)
![Material You](https://custom-icon-badges.demolab.com/badge/material%20you-lightblue?style=for-the-badge&logoColor=333&logo=material-you)
![GitHub code size](https://img.shields.io/github/languages/code-size/MFM-347/AppLate?style=for-the-badge&color=505B92)
![Github Repo Size](https://img.shields.io/github/repo-size/MFM-347/AppLate?style=for-the-badge&color=505B92)
![Stars](https://img.shields.io/github/stars/MFM-347/AppLate?color=blue&style=for-the-badge)
![Latest Release](https://img.shields.io/github/v/release/MFM-347/AppLate?color=B9C3FF&include_prereleases&style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/MFM-347/AppLate?color=F05032&style=for-the-badge)

**Automate Android APK & AAB Builds with GitHub Actions**

AppLate is a streamlined **Android Continuous Integration/Continuous Deployment (CI/CD) template** that simplifies the building of Android applications. Using GitHub Actions, this template automates the creation of APK and AAB files, enabling efficient distribution. The workflow supports both **debug** and **release builds** with manual triggering for controlled release management.

## 🚀 Features

✅ **Automated CI/CD** with GitHub Actions for APK & AAB builds.  
✅ **Customizable Project Setup** using an initialization script.  
✅ **Secure Signing** via environment variables.  
✅ **Manual Workflow Triggers** for release management.  
✅ **Easy Artifact Downloads** directly from GitHub Actions.

## 📌 Getting Started

### 1️⃣ Update Workflow Permissions

Ensure that your GitHub Actions workflow has the necessary **read and write** permissions:

1. Navigate to your **GitHub repository**.
2. Click on **Settings**.
3. Select **Actions** from the left sidebar.
4. Scroll down to **Workflow permissions**.
5. Choose **Read and write permissions**.
6. Click **Save**.

### 2️⃣ Initialize Your Project

1. Update metadata in `devAssets/_meta.json` under `objects > new` with the latest project details.
2. Run the **Initialize** workflow from the `Actions` section to replace old metadata across all **Android project-related files**.
3. Validate changes by checking:
   - `AndroidManifest.xml`
   - `build.gradle`
   - Package names in source code
4. Ensure no outdated references remain before proceeding.

### 3️⃣ Add Environment Variables

To sign builds securely, add the following **GitHub Secrets** in your repository:

| Secret Name               | Description                     |
| ------------------------- | ------------------------------- |
| `KEYSTORE_BASE_64`        | Base64-encoded keystore file    |
| `DEBUG_KEYSTORE_PASSWORD` | Password for the debug keystore |
| `DEBUG_KEYSTORE_ALIAS`    | Alias for the debug keystore    |
| `DEBUG_KEY_PASSWORD`      | Password for the key            |

## 🎯 Running GitHub Actions Workflows

To trigger a build, follow these steps:

1. Go to **GitHub Actions**.
2. Select the workflow:
   - **Build Release App** → Generates production-ready builds.
   - **Build Debug App** → Generates test/debug builds.
3. Download build artifacts (`release-build.zip` or `debug-build.zip`) after the workflow completes.

## 📖 Credits

- XML formatting is done using [Android XML Formatter](https://github.com/ByteHamster/android-xml-formatter).
- This workflow is inspired of **Lloyd Dcosta**’s workflow example on [Medium](https://medium.com/@dcostalloyd90/automating-android-builds-with-github-actions-a-step-by-step-guide-2a02a54f59cd) and further enhanced by **[@MFM-347](https://github.com/MFM-347)**.

## 📜 License

This project is licensed under the **Apache 2.0 License**.

[![License](https://img.shields.io/badge/License-Apache_2.0-0298c3.svg?style=for-the-badge)](https://github.com/MFM-347/AppLate/blob/main/LICENSE)

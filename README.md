# UI Tests with Allure Report

This project contains automated UI tests written in Python with Selenium and Pytest, running inside Docker containers.  
The Allure report is automatically generated and published to GitHub Pages.

---

## 🚀 How to Run Tests on GitHub

The project uses **GitHub Actions** to run tests and generate reports.

### 🔁 Manual Trigger

To start the tests manually:

1. Go to the **Actions** tab in your GitHub repository.  
2. Choose the **UI Tests** workflow.  
3. Click **Run workflow**.

> The workflow will:
> - Run tests via Docker Compose  
> - Generate Allure Report  
> - Publish the report to GitHub Pages (`gh-pages` branch)

---

## 🔐 Environment Variables

To run the tests and deploy the Allure report via GitHub Actions,  
you must configure the following secrets in **Settings → Secrets and variables → Actions** of your GitHub repository:

| Secret Name           | Description                                 |
|-----------------------|---------------------------------------------|
| `CI_TOKEN`            | GitHub token for deploying to Pages         |

> ⚠️ These secrets are **required** for the workflow to run properly and for Allure report deployment.

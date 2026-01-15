# 🚀 Deployment Guide

## ✅ Pre-Deployment Checklist
Check that you have done the following before moving to the CircleCI deployment part:
1. ✅ Dockerfile
2. ✅ Kubernetes Deployment file
3. ✅ Code Versioning using GitHub

## ✅ Enable Required GCP APIs

Go to your GCP account and enable all the following APIs:

Navigation:
In the left pane → APIs & Services → Library

Enable the following:
- Kubernetes Engine API
- Container Registry API
- Compute Engine API
- Cloud Build API
- Cloud Storage API
- IAM API

## ✅ Create GKE Cluster and Artifact Registry
1. Create GKE Cluster:
    - Go to your GCP Console and search for GKE.
    - Create a new cluster with a name of your choice.
    - In the Networking tab, provide the necessary access/configurations.

2. Create Artifact Registry:
    - In the GCP Console, search for Artifact Registry.
    - Create a new Artifact Registry with a name of your choice

## ✅ Create a Service Account and Configure Access
1. Create a Service Account in your GCP Console.
2. Assign the following roles:
    - Storage Object Admin
    - Storage Object Viewer
    - Owner
    - Artifact Registry Admin
    - Artifact Registry Writer
3. Download the key as a `.json` file.
4. Place the key file (e.g., `gcp-key.json`) in the root directory of your project.
5. Important: Add `gcp-key.json` to your `.gitignore` to prevent it from being pushed to GitHub.


# 🔐 Convert gcp-key.json to Base64
In your terminal (e.g., Git Bash or VS Code), run:
```bash
cat gcp-key.json | base64 -w 0
```
Copy the output and use it as needed in environment variables or CircleCI secrets.

## ✅ Set Up CircleCI Configuration
1. Create the CircleCI config file:
In your project root directory, create the following file:
```bash
.circleci/config.yml
```
2. Get the code for the config file from the specified GitHub repository.
3. Set up a CircleCI account:
    - You can sign up using your Google account.
    - After creating the account, connect it to GitHub to access your repositories.

## ✅ Connect Project to CircleCI and Set Environment Variables
1. Open CircleCI and go to the Projects section.
2. Connect CircleCI to your GitHub account:
    - Authorize CircleCI to access your GitHub repositories.
3. Select your project repository:
    - CircleCI will automatically detect the .circleci/config.yml file.
4. Configure project settings:
    - Set up triggers and pipelines.
5. Add Environment Variables under Project Settings → Environment Variables:
    - `GCLOUD_SERVICE_KEY` — your Base64-encoded GCP key
    - `GOOGLE_PROJECT_ID` — your GCP project ID
    - `GKE_CLUSTER` — your GKE cluster name
    - `GOOGLE_COMPUTE_REGION` — your compute region

## ✅ Set Up LLMOps Secrets in GKE using kubectl
1. Access your GKE cluster:
    - Open your GKE Console.
    - Go to Workloads → Click on your workload.
    - Open the kubectl terminal.
2. Configure your local terminal to connect with your cluster:
    - Run the following command, adjusting for your project details:
    ```bash
    gcloud container clusters get-credentials llmops \
    --region us-central1 \
    --project project-4f25978b-aed8-4441-b5d
    ```
3. Create a Kubernetes secret to store your LLM API key:
    ```bash
    kubectl create secret generic llmops-secrets \
    --from-literal=GROQ_API_KEY="your_actual_groq_api_key"
    ```

## ✅ Trigger CircleCI Pipeline
- After completing all configurations, trigger your pipeline in CircleCI manually for the first time to ensure everything is working.
- From now on, the pipeline will be automatically triggered on each git push to the repository.
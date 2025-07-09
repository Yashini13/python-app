# 💰 BudgetBuddy – A Simple Python Finance Tracker (AWS DevOps Project)

BudgetBuddy is a minimal Flask-based finance management app that allows users to track expenses and calculate total spending. This project demonstrates a full DevOps pipeline using AWS services like CodeCommit, CodeBuild, CodePipeline, ECR, EKS, and CloudWatch.

---

## 🛠 Tech Stack

- **Backend**: Python (Flask)
- **Containerization**: Docker
- **CI/CD Tools**: AWS CodeCommit, CodeBuild, CodePipeline
- **Deployment**: AWS EKS (Kubernetes)
- **Monitoring**: AWS CloudWatch Logs
- **Registry**: Amazon ECR

---

## 🚀 Features

- Add expenses with name and amount
- Calculate and display total expenditure
- Web UI using Flask templates
- CI/CD with automated Docker builds and Kubernetes deployment
- Monitored using AWS CloudWatch Logs

---

## 🔧 Prerequisites

- AWS CLI configured
- Docker installed
- kubectl & eksctl configured
- AWS IAM permissions for CodeCommit, CodeBuild, ECR, EKS

---

## 🧑‍💻 Getting Started

### 1. Clone or Fork this Repository

```bash
git clone https://git-codecommit.REGION.amazonaws.com/v1/repos/budgetbuddy
cd buddybudget
aws ecr create-repository --repository-name budgetbuddy
git remote add aws-codecommit https://git-codecommit.REGION.amazonaws.com/v1/repos/budgetbuddy
git push aws-codecommit main

4. Configure CodeBuild
Link to your CodeCommit repo

Use buildspec.yml to:

Build Docker image

Push to ECR

5. Configure CodePipeline
Source: CodeCommit

Build: CodeBuild

Deploy: (Optional) Add Lambda to run kubectl apply

☸️ Kubernetes Deployment
Set up EKS cluster:

bash
Copy
Edit
eksctl create cluster --name budget-cluster --region ap-south-1
Deploy app:

bash
Copy
Edit
kubectl apply -f deployment/
Get app URL:

bash
Copy
Edit
kubectl get svc budgetbuddy-service
📈 Monitoring
View logs:

bash
Copy
Edit
kubectl logs -l app=budgetbuddy
```



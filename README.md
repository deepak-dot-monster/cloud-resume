\# Cloud Resume Challenge ☁️



A serverless, full-stack resume website built on AWS — combining a static frontend, a serverless visitor-counter backend, custom domain HTTPS, automated CI/CD, and production-style monitoring.



\*\*Live site:\*\* \[deepak.monster](https://deepak.monster)



\---



\## Overview



This project implements the \[Cloud Resume Challenge](https://cloudresumechallenge.dev/), a widely recognized AWS portfolio benchmark, using \*\*AWS CloudFormation\*\* for infrastructure-as-code.



It's not just a static page — every request to the site pulls a live visitor count from a serverless backend, the entire infrastructure is version-controlled and reproducible, and the frontend auto-deploys on every push via CI/CD.



\## Architecture



─────────────────┐



Visitor ───────────▶ │ CloudFront │

│ (HTTPS, CDN) │

└────────┬─────────┘

│

▼

┌─────────────────┐

│ S3 Bucket │

│ (static site, │

│ private + OAC) │

└─────────────────┘



Browser JS ────────▶ API Gateway ────▶ Lambda ────▶ DynamoDB

(fetch call) (REST API) (Python) (visitor count)



Route 53 (DNS) + ACM (SSL) ──▶ deepak.monster

CloudWatch + SNS ──▶ Lambda error \& billing alerts

GitHub Actions ──▶ auto-deploy frontend on push





\## Tech Stack



| Layer | Service |

|---|---|

| Frontend hosting | Amazon S3 + CloudFront (Origin Access Control) |

| DNS \& SSL | Route 53 + AWS Certificate Manager |

| Backend API | API Gateway (REST) |

| Compute | AWS Lambda (Python 3.12) |

| Database | DynamoDB (on-demand, atomic counter) |

| IaC | AWS CloudFormation |

| CI/CD | GitHub Actions |

| Monitoring | CloudWatch Alarms + SNS |



\## Repository Structure



cloud-resume/

├── frontend/ # Static site (HTML/CSS/JS)

│ ├── index.html

│ ├── styles.css

│ └── script.js

├── backend/

│ └── src/

│ ├── app.py # Lambda function (visitor counter)

│ └── requirements.txt

├── infrastructure/ # CloudFormation templates

│ ├── backend-template.yaml # Lambda + API Gateway + DynamoDB

│ ├── frontend-template.yaml # S3 + CloudFront + ACM

│ └── monitoring-template.yaml # CloudWatch alarms + SNS

├── .github/

│ └── workflows/

│ └── deploy-frontend.yml # Auto-deploy frontend on push

├── LICENSE

└── README.md





\## Features



\- \*\*Serverless visitor counter\*\* — atomic DynamoDB `ADD` operation avoids race conditions under concurrent traffic

\- \*\*Locked-down S3 bucket\*\* — no public access; only CloudFront can read via Origin Access Control

\- \*\*Custom domain + free SSL\*\* — Route 53 + ACM, auto-renewing certificate

\- \*\*CI/CD\*\* — GitHub Actions syncs `frontend/` to S3 and invalidates the CloudFront cache on every push to `main`

\- \*\*Monitoring \& alerting\*\* — CloudWatch alarms on Lambda errors and estimated monthly billing, notifying via SNS email



\## Deploying This Yourself



```bash

\# Backend (Lambda + API Gateway + DynamoDB)

aws cloudformation deploy \\

&#x20; --template-file infrastructure/backend-template.yaml \\

&#x20; --stack-name cloud-resume-backend \\

&#x20; --capabilities CAPABILITY\_IAM \\

&#x20; --region ap-south-1



\# Frontend (S3 + CloudFront + ACM)

aws cloudformation deploy \\

&#x20; --template-file infrastructure/frontend-template.yaml \\

&#x20; --stack-name cloud-resume-frontend \\

&#x20; --region ap-south-1



\# Monitoring (CloudWatch + SNS)

aws cloudformation deploy \\

&#x20; --template-file infrastructure/monitoring-template.yaml \\

&#x20; --stack-name cloud-resume-monitoring \\

&#x20; --region us-east-1 \\

&#x20; --parameter-overrides AlertEmail=your-email@example.com

```



\## What I Learned



Building this surfaced several real-world debugging scenarios:

\- Diagnosing a misconfigured Lambda resource policy causing API Gateway 500s despite the function working correctly in isolation

\- DNS propagation and nameserver delegation troubleshooting across registrar and Route 53

\- CI/CD credential scoping via GitHub Actions Secrets

\- Structuring infrastructure-as-code for readability and reuse across environments



\## Author



**Deepak **— \[GitHub](https://github.com/deepak-dot-monster) · \[deepak.monster](https://deepak.monster)


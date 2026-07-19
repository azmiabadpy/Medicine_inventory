# 💊 Medicine Inventory Management System

## 📌 Project Overview

The **Medicine Inventory Management System** is a cloud-integrated application built using **Python Flask** that helps manage medicine stock, sales, and inventory operations.

The project demonstrates integration with multiple AWS services including **Amazon RDS for database storage, Amazon S3 for log storage, Amazon SNS for email notifications, and Amazon CloudWatch for application monitoring**.

The application is containerized using Docker and designed following DevOps practices with focus on scalability, monitoring, and automation.

---

# 🏗️ Architecture

```
                         Users
                           |
                           |
                           v

                    Flask Application
                    (Docker Container)

                           |
        ------------------------------------------------
        |                     |                        |
        v                     v                        v

    Amazon RDS              Amazon S3              Amazon SNS
     MySQL              Application Logs       Email Notifications
   Database                 Storage              Stock Alerts


                           |
                           v

                    Amazon CloudWatch
                Logs + Metrics Monitoring

```

---

# 🚀 Features

## Medicine Management

- Add new medicines
- Update medicine details
- Edit existing inventory
- Sell medicines
- Track available stock
- Dashboard view for inventory status


## Inventory Monitoring

- Real-time stock tracking
- Low-stock detection
- Automated medicine shortage alerts


## Cloud Integration

- Store application data in Amazon RDS
- Upload application logs to Amazon S3
- Send stock alerts using Amazon SNS
- Monitor application health using CloudWatch


---

# 🛠️ Technologies Used

## Application

- Python
- Flask
- HTML
- Jinja Templates
- PyMySQL


## Database

- Amazon RDS
- MySQL


## Cloud Services

- Amazon EC2
- Amazon RDS
- Amazon S3
- Amazon SNS
- Amazon CloudWatch
- IAM


## DevOps Tools

- Docker
- Linux
- Git & GitHub


---

# 📂 Project Structure

```
medicine-inventory/

│
├── routes/
│   ├── __init__.py
│   └── medicine.py
│
├── services/
│   ├── __init__.py
│   ├── inventory_service.py
│   ├── s3_service.py
│   └── sns_service.py
│
├── templates/
│   ├── add_medicine.html
│   ├── base.html
│   ├── dashboard.html
│   ├── edit_medicine.html
│   ├── index.html
│   └── sell_medicine.html
│
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
│
├── cloudwatch_configuration_file
└── README.md

```

---

# ⚙️ Application Workflow

## 1. User Interaction

Users can:

- Add medicines
- Update inventory
- Sell medicines
- View dashboard


---

## 2. Database Storage

Medicine information is stored in:

```
Flask Application
        |
        |
    database.py
        |
        |
 Amazon RDS MySQL
```

Stored information:

- Medicine name
- Quantity
- Price
- Expiry details
- Sales information


---

## 3. Inventory Service

The inventory service manages business logic:

```
inventory_service.py

        |
        |
 Checks medicine quantity

        |
        |
Low stock detected

        |
        |
Triggers SNS notification

```

---

# 📧 SNS Email Notification

When medicine stock goes below the defined threshold:

```
Medicine Quantity < Minimum Limit

             |
             v

        SNS Service

             |
             v

       Email Notification

```

Example:

```
Subject:
Medicine Stock Alert


Message:
Paracetamol stock is running low.
Please update inventory.
```

---

# 📦 S3 Log Storage

Application logs are uploaded to Amazon S3.

Flow:

```
Flask Application

        |

   s3_service.py

        |

     Amazon S3

        |

 Stored Application Logs

```

Benefits:

- Centralized log storage
- Backup capability
- Long-term log retention


---

# 📊 CloudWatch Monitoring

CloudWatch Agent is configured for monitoring:

Collected metrics:

- CPU utilization
- Memory usage
- Disk utilization
- Application logs


Architecture:

```
EC2 Instance

      |

CloudWatch Agent

      |

CloudWatch Logs

      |

Monitoring Dashboard

```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t medicine-inventory .
```

---

## Run Container

```bash
docker run -d \
-p 5000:5000 \
--name medicine-app \
medicine-inventory
```

---

## Check Running Container

```bash
docker ps
```

---

## View Application Logs

```bash
docker logs medicine-app
```

---

# 🔐 Environment Configuration

Create environment variables:

```
DB_HOST=<rds-endpoint>
DB_USER=<username>
DB_PASSWORD=<password>
DB_NAME=<database-name>

AWS_REGION=<region>

S3_BUCKET=<bucket-name>

SNS_TOPIC_ARN=<sns-topic-arn>
```

---

# 📋 Installation & Setup

## Clone Repository

```bash
git clone https://github.com/<username>/medicine-inventory.git

cd medicine-inventory
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application will start:

```
http://localhost:5000
```

---

# 🧪 Testing

Test application:

```bash
curl http://localhost:5000
```

Verify:

- Medicine creation
- Inventory updates
- Database connection
- SNS alerts
- S3 log uploads


---

# 🔒 Security Practices

Implemented:

- IAM roles for AWS access
- Environment variables for secrets
- Restricted database access
- Separate application and database layers


---

# 📚 Learning Outcomes

Through this project, I learned:

- Building Flask applications
- Connecting applications with AWS services
- Designing cloud-based architectures
- Managing databases using Amazon RDS
- Implementing centralized logging
- Creating automated notification systems
- Monitoring applications using CloudWatch
- Containerizing applications with Docker


---

# 🔮 Future Improvements

Future enhancements:

- Deploy using Kubernetes (EKS)
- Add Jenkins CI/CD pipeline
- Use Terraform for AWS infrastructure provisioning
- Add Application Load Balancer
- Implement Auto Scaling
- Use AWS Secrets Manager
- Add Prometheus and Grafana monitoring


---

# 👨‍💻 Author

**Abadur Rahaman Azmi**

DevOps Engineer

### Skills

AWS | Docker | Kubernetes | Jenkins | Terraform | Linux | Python | CI/CD

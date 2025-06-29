# 🔐 Anonymized Analysis Powered by Ethical Machine Learning

**Hackathon:** Hack to Future 2.0  
**Team Name:** Nobodies (HFA06)  
**Project Type:** Ethical Machine Learning for Customer Analytics

---

## 🧠 Project Summary

This project focuses on enabling insightful customer trend analysis through ethical use of machine learning — **without compromising user privacy**. By anonymizing and encrypting sensitive data before training, our system upholds data rights while still delivering actionable intelligence for organizations.

---

## 🎯 Objectives

1. **Develop a machine learning framework** to analyze customer behavior and trends from anonymized datasets.
2. **Ensure ethical data usage** using multi-layered encryption techniques like AES-GCM and RSA.
3. **Completely anonymize personally identifiable information (PII)** in the data used for training.

---

## 🔧 Tech Stack

- **Language:** Python
- **Libraries:** 
  - `pandas` for data manipulation  
  - `scikit-learn` for ML modeling  
  - `matplotlib` for visualization
- **Security:** 
  - RSA Encryption (Public Key Only)
  - AES-GCM Encryption
  - SHA-based Hashing
- **Data Input:** CSV-based dataset (static for demo, scalable to dynamic DB)

---

## 🔐 Key Features

### 🔄 Data Anonymization & Encryption
- All sensitive user data fields are **encrypted using RSA public keys**.
- The **private decryption keys are discarded** to enforce irreversible anonymization.
- Additional **hashing** ensures tamper-proof security.

### 🧮 Machine Learning Model
- Trained on **3000 anonymized datasets**.
- Predicts customer behavior parameters with high accuracy.
- Validated using real-time graphical outputs.

### 📊 Visualization
- Uses `matplotlib` to generate graphical output for:
  - Model accuracy
  - Behavioral trend distributions

### 🔎 User Transparency
- A clear **user agreement** on the front-end defines:
  - Data usage purposes
  - Anonymization guarantees
  - Consent policies

---

## 🧪 Testing & Output

- Used a **CSV dataset** as input.
- Successfully encrypted PII and trained model on anonymized data.
- Final output includes accuracy plots and prediction graphs.
- Front-end includes user agreement consent page.

---

## 💡 Problem-Solution Mapping

| Problem                                  | Our Solution                                                                 |
|------------------------------------------|------------------------------------------------------------------------------|
| Analyzing customer trends in large DBs   | ML model trained on anonymized data (3000+ rows)                            |
| Securing sensitive user data             | AES-GCM + RSA double-layer encryption with no retained private key          |
| User mistrust due to data misuse         | Clear consent-based front-end with transparent data usage explanation       |

---

## 📽️ Final Demo

- Frontend user agreement page
- Backend encryption → ML → Visualization flow
- Secure, privacy-first design

---

## 🙌 Thank You

Built with responsibility, ethics, and innovation for Hack to Future 2.0 🚀

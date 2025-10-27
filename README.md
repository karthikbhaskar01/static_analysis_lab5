# Lab 5 – Static Analysis

## 📘 Overview
This lab demonstrates static code analysis using **Pylint**, **Flake8**, and **Bandit** on the `inventory_system.py` program.

## 🧰 Tools Used
- Pylint (Code quality and style)
- Flake8 (PEP8 style checker)
- Bandit (Security analysis)

## 🛠 Fix Summary
Fixed four issues:
1. Replaced `except:` with `except Exception as e:`
2. Removed unused imports
3. Replaced `eval()` with safer parsing
4. Fixed long lines and spacing (PEP8 compliance)

## 📁 Files Included
- `inventory_system.py` – Cleaned and updated code  
- `pylint_report.txt`, `flake8_report.txt`, `bandit_report.txt` – Analysis reports  
- `issues_table.txt` – Documentation of issues and fixes  
- `reflection.txt` – Reflection on static analysis  
- `inventory.json` – Sample input data  

## ✅ Result
All high and medium severity issues resolved. Code rated 9+/10 by Pylint.

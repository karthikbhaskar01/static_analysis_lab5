# 🧰 Issues Fixed Table

| Issue Type / Tool | Line(s) | Description | Fix Approach |
|-------------------|----------|--------------|---------------|
| Mutable default argument (Pylint) | 10 | Default list used as mutable argument (`logs=[]`) | Changed to `logs=None` and initialized inside function |
| Bare except (Pylint) | 24 | `except:` used without specifying exception | Replaced with `except KeyError` and `except Exception as e` |
| Use of eval (Bandit) | 64 | Insecure use of `eval()` allows code execution | Removed unsafe `eval()` call |
| Missing input validation (Pylint/Bandit) | 15–20 | Invalid data types could cause crashes | Added type checks for `item` and `qty` |
| Improper file handling (Flake8) | 34–41 | Files opened without context manager | Used `with open()` for automatic closing |
| Missing logging configuration | — | Errors not logged properly | Added `logging.basicConfig()` setup |

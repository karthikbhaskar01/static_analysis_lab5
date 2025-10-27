# Lab 5 Reflection

1. **Easiest/Hardest?**  
   - Easiest: Adding docstrings and renaming to snake_case.  
   - Hardest: Removing `eval()` — had to rethink demo flow.

2. **False positives?**  
   - None. All warnings were valid.

3. **Workflow integration?**  
   - **Local**: `pre-commit` hook with `pylint`, `flake8`, `bandit`.  
   - **CI**: GitHub Actions to run on every push.

4. **Improvements?**  
   - **Score**: 4.8 → 8.08 / 10  
   - **Security**: No `eval`, safe file handling  
   - **Readability**: Docstrings, logging, PEP-8  
   - **Robustness**: Specific exceptions, encoding
# Lab 6 submission steps

The handout asks for two reports, two test files, screenshots taken only after each required threshold is reached, and at least two commits. Keep the line coverage and branch coverage stages separate so each commit shows that stage's test file and screenshot.

## 1. Install and enter the Lab 6 folder

```powershell
py -m pip install -r requirements.txt
cd "lab6"
```

Run the starter tests once to see the baseline:

```powershell
coverage run -m pytest test_pizza_order.py
coverage report -m pizza_order.py
```

This initial report is for analysis. Do not submit a screenshot of it.

## 2. Line/code coverage stage

Run the line-coverage test file without branch measurement:

```powershell
coverage erase
coverage run --source=pizza_order -m pytest CodeCoverageTest_PES1UG24CS329_pizza_order.py
coverage report -m pizza_order.py
```

Confirm `pizza_order.py` is at least 90% covered. Capture a terminal screenshot showing the passing pytest summary and the `coverage report -m` table. Save it as `CodeCoverage_PES1UG24CS329.png` in this folder. This test set is designed to execute every statement; it omits some alternate outcomes so the report can show why line coverage alone does not prove branch completeness.

Commit this stage from the repository root (the folder containing `Lab 6`):

```powershell
git add "lab6/CodeCoverageTest_PES1UG24CS329_pizza_order.py" "lab6/CodeCoverage_PES1UG24CS329.png"
git commit -m "Add Lab 6 code coverage tests and report"
```

## 3. Branch coverage stage

Run the branch-coverage test file with branch measurement enabled:

```powershell
coverage erase
coverage run --branch --source=pizza_order -m pytest BranchCoverageTest_PES1UG24CS329_pizza_order.py
coverage report -m pizza_order.py
```

Confirm the reported coverage is at least 90%. Capture a terminal screenshot showing the passing pytest summary and the coverage table. Save it as `BranchCoverage_PES1UG24CS329.png` in this folder. The branch test set checks both sides of the decisions, including size/topping errors, topping count boundaries, cheese burst, discount day/student cases, and delivery distance/time boundaries.

Commit this stage separately:

```powershell
git add "lab6/BranchCoverageTest_PES1UG24CS329_pizza_order.py" "lab6/BranchCoverage_PES1UG24CS329.png"
git commit -m "Add Lab 6 branch coverage tests and report"
```

## 4. Before submitting

- Keep both screenshots in the `Lab 6` folder and ensure the terminal text is readable.
- Check `git log -2 --oneline` to confirm there are at least two separate commits.
- Check `git status` to ensure the screenshots and both test files are committed.
- Push only to your own SE lab submissions repository, not the course starter repository.

The `PES1UG24CS329` portion of the two required filenames is based on the current local account name. Replace it consistently in the filenames, commands, and screenshot names if your instructor expects a different identifier.

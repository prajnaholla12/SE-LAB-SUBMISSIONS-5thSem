# Lab 6 Coverage Analysis

**Student:** PES1UG24CS329 | Prajna Holla 
**Application:** `pizza_order.py`

## Purpose

This lab compares statement (line) coverage with branch coverage. Statement coverage records whether executable statements ran at least once. Branch coverage also checks whether both outcomes of each decision were taken. A high statement percentage alone can miss an untested decision outcome.

## Code coverage result

Command used:

```powershell
py -m coverage run --source=pizza_order -m pytest CodeCoverageTest_PES1UG24CS329_pizza_order.py
py -m coverage report -m pizza_order.py
```

**Result:** 12 tests passed. `pizza_order.py` had 34 statements, 0 missed, and **100% statement coverage**. The terminal evidence is `CodeCoverage_PES1UG24CS329.png`.

The tests execute all statements, including invalid-size and negative-topping errors, both topping-price calculations, cheese-burst pricing and rejection, each discount calculation path, and each delivery result. Some decisions can still skip an outcome without skipping a statement. For example, the line-coverage set does not exercise the false outcome of the cheese-burst check or the non-student outcome of the student-discount check. This is why statement coverage alone does not establish branch coverage.

## Branch coverage result

Command used:

```powershell
py -m coverage run --branch --source=pizza_order -m pytest BranchCoverageTest_PES1UG24CS329_pizza_order.py
py -m coverage report -m pizza_order.py
```

**Result:** 15 tests passed. The report showed 34 statements, 0 missed, **24 branches, 0 partial branches, and 100% coverage**. The terminal evidence is `BranchCoverage_PES1UG24CS329.png`.

The branch tests check both outcomes for the size and topping validations, topping counts on either side of three, cheese-burst availability, minimum order total, Tuesday/weekend/regular-day discounts, student eligibility, delivery distance, and delivery-time boundaries at 30 and 45 minutes.

## Conclusion

The line-coverage test set executes every measured statement. The expanded branch-coverage test set also exercises every measured decision outcome. Coverage reports show which code ran; they support test completeness analysis but do not prove the application is defect-free.


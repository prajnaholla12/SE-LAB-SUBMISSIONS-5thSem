# Static Code Analysis — Issue Table

**Program:** `school_transport.py`

The line numbers below refer to the original, unmodified version of `school_transport.py`. Some findings overlap across tools; the table describes distinct issues or closely related findings.

| Issue | Type / Tool | Original line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| SQL query built with an f-string | Security — Bandit B608 | 8 | Values were interpolated into SQL, creating a SQL-injection risk. | Used parameterized SQL placeholders and passed values as a tuple. |
| Subprocess command uses `shell=True` | Security — Bandit B602 | 21 | A command containing a route value was executed through the shell. | Removed the subprocess call and printed a dispatch message for this demonstration. |
| Unnecessary subprocess import | Security review — Bandit B404 | 1 | The `subprocess` module was only needed for the shell-based dispatch command. | Removed the import after removing the subprocess call. |
| Runtime validation uses `assert` | Reliability — Bandit B101 | 33 | An `assert` was used for a runtime fee check; assertions may be disabled in optimized runs. | Replaced it with an explicit condition that raises `ValueError` if the fee total is unexpected. |
| Missing module and function docstrings | Code quality — Pylint C0114/C0116 | 1, 7, 11, 14, 20, 23, 29 | The module and functions did not explain their purpose. | Added a module docstring and concise function docstrings. |
| Function names not in `snake_case` | Naming — Pylint C0103 | 7, 11, 14, 20, 23 | Names such as `enrollRider` and `feeCollected` did not follow Python naming conventions. | Renamed functions to `enroll_rider`, `route_roster`, `export_roster`, `dispatch_alert`, and `fee_collected`. |
| Unused `driver` parameter | Code quality — Pylint W0613 | 11 | `routeRoster` accepted a `driver` parameter but never used it. | Removed the unused parameter and updated the call site. |
| File opened without encoding and manually closed | Reliability — Pylint W1514/R1732 | 15–18 | The file was opened without an explicit encoding and manually closed, so an exception could prevent closure. | Used a `with` statement and specified `encoding="utf-8"`. |
| Bare `except` clause | Reliability/style — Pylint W0702; Flake8 E722 | 26 | A bare `except` caught all exceptions, including unexpected ones unrelated to SQLite. | Caught `sqlite3.Error` specifically and handled an empty `SUM` result separately. |
| Long lines, spacing, and blank-line violations | Style — Pylint C0301; Flake8 E501/E231/E302 | 5, 8, 12, 21 and surrounding definitions | Statements exceeded line-length limits or had inconsistent spacing and function separation. | Wrapped long statements, corrected spacing, and used consistent blank lines. |

## Verification after fixes

- **Pylint:** 10.00/10.
- **Bandit:** No issues identified.
- **Flake8:** No output, indicating no reported violations.
- The program ran successfully and printed the dispatch message and the R2 roster containing `Zoya`.

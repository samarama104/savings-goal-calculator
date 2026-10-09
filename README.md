# Savings Goal Calculator

A Python command-line tool that calculates how many monthly
contributions are needed to reach a savings goal.

## Features

- Calculates the amount remaining to save.
- Rounds the required number of months up to a whole number.
- Recognizes when the goal has already been reached.
- Rejects negative amounts and a zero contribution when more savings are needed.

## Requirements

Python 3. No additional packages required.

## How to run

Open a terminal in the project folder and run:

```bash
python3 savings_calculator.py
```

Enter your savings goal, current savings, and monthly contribution
as numbers without dollar signs or commas.

## Example

```text
Savings goal ($): 1000
Current savings ($): 250
Monthly contribution ($): 200
Remaining to save: $750.00
Months needed: 4
```

Three contributions of $200 would leave $150 still to save,
so the calculator rounds up to four months.

## Example checks

| Goal | Current savings | Monthly contribution | Expected result |
|---|---|---|---|
| 1000 | 250 | 200 | $750 remaining; 4 months |
| 1000 | 1000 | 0 | Goal already reached |
| 1000 | 250 | 0 | Contribution error message |
| 1000 | -50 | 200 | Negative amount error message |

## What I practiced

- Collecting input and converting text to numbers.
- Using arithmetic and math.ceil() to round up.
- Formatting amounts to two decimal places.
- Using if, elif, and else to validate inputs.

## Limitations

- Assumes a fixed monthly contribution.
- Does not account for interest or withdrawals.
- Expects numeric input; text or blank input causes an error.
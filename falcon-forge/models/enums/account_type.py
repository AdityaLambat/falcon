from enum import Enum


class AccountType(Enum):

    SAVINGS = "Savings"
    CURRENT = "Current"
    SALARY = "Salary"
    FIXED_DEPOSIT = "Fixed Deposit"
    RECURRING_DEPOSIT = "Recurring Deposit"
    LOAN = "Loan"
    NRE = "NRE"
    NRO = "NRO"
    FCNR = "FCNR"
    OVERDRAFT = "Overdraft"
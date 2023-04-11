import mintapi
import os
from datetime import date, timedelta, datetime


def main():
    mint = mintapi.Mint(
        os.environ.get('EMAIL'),
        os.environ.get('PASSWORD'),
        mfa_method='soft-token',
        mfa_token=os.environ.get("MFA_TOKEN"),
        headless=True,
        wait_for_sync=True,
        wait_for_sync_timeout=300,
        fail_if_stale=True,
    )

    print(get_previous_month_leftover(mint.get_budget_data()))


def get_previous_month_leftover(data):
    first_day_of_current_month = date.today().replace(day=1)
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)

    last_month = last_day_of_previous_month.month
    if last_month < 10:
        last_month_str = '0' + str(last_month)
    else:
        last_month_str = str(last_month)

    current_year = last_day_of_previous_month.year

    amount_to_invest = 0

    for item in data:
        if str(current_year) + '-' + last_month_str not in item['budgetDate']:
            continue
        if item['subsumed'] is True:
            continue
        if 'rollover' not in item:
            continue
        if item['rollover'] is True and item['budgetAmount'] > item['amount']:
            continue

        amount_to_invest += item['budgetAmount'] - item['amount']

    return round(amount_to_invest, 2)


if __name__ == '__main__':
    main()

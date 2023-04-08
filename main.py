import mintapi
import os


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

    print(mint.get_account_data())


if __name__ == '__main__':
    main()

import os

from facebookads.api import FacebookAdsApi
from facebookads import objects


def main():
    print_header()
    facebook_api = facebook_session_init()

    file = get_text_file_from_user()
    if not file:
        print('Please check file path and try again.')
        return

    # TODO: Refactor generator to yeild X number of emails, in array, at a time
    emails = read_emails_from_file(file)
    for email in emails:
        facebook_ads_api_call(email)


def print_header():
    print('------------------------------------------')
    print('           DEMO FACEBOOK ADS!             ')
    print('------------------------------------------')
    print()


def get_text_file_from_user():
    file = input('What text file would you like to upload? ')
    if not file or not file.strip():
        return None
    if not os.path.isfile(file):
        return None

    return os.path.abspath(file)


def read_emails_from_file(file):
    """
    Generator to yield one line instead of storing all lines in memory.
    """
    with open(file, 'rb') as file_in:
        for line in file_in:
            yield line


def facebook_session_init():
    # Place import keys in an ENVIRONMENT VARIABLES and out of source control.
    try:
        my_app_id = os.environ['APP_ID']
    except KeyError:
        print('Please set envrionment variable APP_ID')

    try:
        my_app_secret = os.environ['APP_SECRET']
    except KeyError:
        print('Please set envrionment variable APP_SECRET')

    try:
        my_access_token_1 = os.environ['ACCESS_TOKEN']
    except KeyError:
        print('Please set envrionment variable ACCESS_TOKEN')

    try:
        proxies = {
            'http': os.environ['HTTP_PROXY'],
            'https': os.environ['HTTPS_PROXY']
        }
    except KeyError:
        print('Please set envrionment variable HTTP_PROXY and HTTPS_PROXY')

    session = FacebookSession(
        my_app_id,
        my_app_secret,
        my_access_token,
        proxies
    )

    return FacebookAdsApi(session)


def facebook_ads_api_call():
    """ Facebook API functionality goes here.
    """
    pass


if __name__ == '__main__':
    main()

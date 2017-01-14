import os

from itertools import islice
# from facebookads.api import FacebookAdsApi
# from facebookads import objects


def main():
    print_header()
    # facebook_api = facebook_session_init()

    file = get_text_file_from_user()
    if not file:
        print('Please check file path and try again.')
        return

    emails = read_emails_from_file(file)
    for email in emails:
        print(len(email))
        # facebook_ads_api_call(email)


def print_header():
    print('------------------------------------------')
    print('           DEMO FACEBOOK ADS!             ')
    print('------------------------------------------')
    print()


def get_text_file_from_user():
    """This function gets the file from the user and checks if it is valid

    Returns:
        str: Absolute path to file.
    """
    file = input('What text file would you like to upload? ')
    if not file or not file.strip():
        return None
    if not os.path.isfile(file):
        return None

    return os.path.abspath(file)


def read_emails_from_file(file, n=10000):
    """Generator to yield an arry of n lines from a file.

    Args:
        file (str): Path to file.
        n (int): Number of lines to yield.
    Returns:
        Generator object
    """
    with open(file, 'rb') as file_in:
        while True:
            next_n_lines = list(islice(file_in, n))
            if not next_n_lines:
                break
            yield next_n_lines


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

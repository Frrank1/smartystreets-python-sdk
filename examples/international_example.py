import os

from smartystreets_python_sdk import StaticCredentials, ClientBuilder
from smartystreets_python_sdk.international_street import Lookup


def run():
    auth_id = os.environ['SMARTY_AUTH_ID']  # We recommend storing your keys in environment variables
    auth_token = os.environ['SMARTY_AUTH_TOKEN']
    credentials = StaticCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).build_international_street_api_client()

    lookup = Lookup("Rua Padre Antonio D'Angelo 121 Casa Verde, Sao Paulo", 'Brazil')
    lookup.geocode = True  # Must be expressly set to get latitude and longitude.

    candidates = client.send(lookup)  # The candidates are also stored in the lookup's 'result' field.

    first_candidate = candidates[0]
    print("Address is {}".format(first_candidate.analysis.verification_status))
    print("Address precision: {}\n".format(first_candidate.analysis.address_precision))

    print("First Line: {}".format(first_candidate.address1))
    print("Second Line: {}".format(first_candidate.address2))
    print("Third Line: {}".format(first_candidate.address3))
    print("Fourth Line: {}".format(first_candidate.address4))
    print("Latitude: {}".format(first_candidate.metadata.latitude))
    print("Longitude: {}".format(first_candidate.metadata.longitude))


if __name__ == "__main__":
    run()

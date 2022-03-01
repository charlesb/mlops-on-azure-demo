import argparse

from azureml.core import Datastore

import aml_utils


def main(datastore_name, account_name, filesystem):

    ws = aml_utils.retrieve_workspace()

    adlsgen2_datastore = Datastore.register_azure_data_lake_gen2(
        workspace=ws,
        datastore_name=datastore_name,
        account_name=account_name,
        filesystem=filesystem
    ) 

    print(f'Datastore {adlsgen2_datastore} created with storage account {account_name}/{filesystem}')


def parse_args(args_list=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--datastore-name', type=str, required=True)
    parser.add_argument('--account-name', type=str, required=True)
    parser.add_argument('--filesystem', type=str, required=True)
    args_parsed = parser.parse_args(args_list)
    return args_parsed


if __name__ == "__main__":
    args = parse_args()

    main(
        datastore=args.datastore,
        data_path=args.path
    )

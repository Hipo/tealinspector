from base64 import b64decode
from algosdk.v2client.algod import AlgodClient
from algosdk.source_map import SourceMap


def get_algod_client(*, network):
    if network == "mainnet":
        algod_address = "https://mainnet-api.algonode.cloud"
    elif network == "testnet":
        algod_address = "https://testnet-api.algonode.cloud"
    elif network == "betanet":
        algod_address = "https://betanet-api.algonode.cloud"
    else:
        raise ValueError("Network is not valid.")

    algod_client = AlgodClient(
        algod_address=algod_address,
        algod_token=""
    )

    return algod_client


def get_teal(*, algod_client, application_id):
    approval_program = algod_client.application_info(application_id)['params']['approval-program']
    bytecode = b64decode(approval_program)
    teal = algod_client.algod_request("POST", '/teal/disassemble', data=bytecode)['result']
    return teal


def get_sourcemap(*, algod_client, teal):
    result = algod_client.compile(teal, source_map=True)
    sourcemap = SourceMap(result['sourcemap'])
    return sourcemap


def print_teal(*, teal, line_number, line_count=25):
    print(f"Line: {line_number}")

    teal_lines = teal.split('\n')
    for l in range(line_number - line_count, line_number + 1):
        print(l, teal_lines[l], '<---------- ' if l == line_number else '')


def inspect(*, network, application_id, program_counter, line_count):
    algod_client = get_algod_client(network=network)
    teal = get_teal(algod_client=algod_client, application_id=application_id)
    sourcemap = get_sourcemap(algod_client=algod_client, teal=teal)
    line_number = sourcemap.get_line_for_pc(program_counter)
    print_teal(teal=teal, line_number=line_number, line_count=line_count)

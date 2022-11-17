import argparse
from tealinspector.main import inspect


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--network", type=str, help="mainnet, testnet or betanet. default is to mainnet.",
        const="mainnet", default="mainnet", nargs="?",
    )
    parser.add_argument("--application_id", type=int)
    parser.add_argument("--program_counter", type=int)
    parser.add_argument("--line_count", type=int, help="default is to 25.", const=25, default=25, nargs="?")

    arguments = parser.parse_args()

    inspect(
        network=arguments.network,
        application_id=arguments.application_id,
        program_counter=arguments.program_counter,
        line_count=arguments.line_count,
    )

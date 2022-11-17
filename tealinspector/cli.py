import json
from pathlib import Path
import sys
from tealinspector import inspect


def run():
    network = Path(sys.argv[1])
    application_id = Path(sys.argv[2])
    program_counter = Path(sys.argv[3])

    inspect(
        network=network,
        application_id=application_id,
        program_counter=program_counter,
    )

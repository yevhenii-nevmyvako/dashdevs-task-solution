from typing import Optional

import click

from equilibrium_index_finder.core.base import save_result_to_json, find_index
from equilibrium_index_finder.validations.validation_input_array import validate_file_extension


@click.command()
@click.argument('numbers', type=str)
@click.option(
    '--dst_filepath', '-f', type=click.Path(exists=False), default=None,
    help='Destination file save the result in JSON format.'
)
def find_equilibrium_index_cli(numbers: str, dst_filepath: Optional[str] = None) -> click:
    """CLI to find the equilibrium index in a list of integers. And save result to json if you need.

    \b
    Example usage:
        python script.py '1,7,3,6,5,6' -f path/to/result.json

    """
    arr = list(map(int, numbers.replace(',', ' ').split()))
    result = find_index(arr)
    if dst_filepath:
        validate_file_extension(dst_filepath)
        save_result_to_json(result, dst_filepath)
        click.echo(f"The result has been saved to {dst_filepath}.")
    else:
        click.echo(f"The equilibrium index is {result}.")


if __name__ == "__main__":
    find_equilibrium_index_cli()

"""
agipy enables you to destroy cloud infrastructure in a hurry.
Copyright (C) 2019  Nils Müller<shimst3r@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os

import click.testing

from . import azure


def test_azure_without_prefix():
    expected = (
        "Usage: azure [OPTIONS]\n"
        'Try "azure --help" for help.\n'
        "\n"
        'Error: Missing option "--prefix".\n'
    )

    runner = click.testing.CliRunner()
    actual = runner.invoke(azure.azure, args=[]).output

    assert actual == expected


def test_azure_without_environment_variables():
    expected = "azure provider is missing the 'AZURE_CLIENT_ID'.\n"

    runner = click.testing.CliRunner()
    actual = runner.invoke(azure.azure, args=["--prefix=test"]).output

    assert actual == expected


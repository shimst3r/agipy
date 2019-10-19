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


def test_azure_with_permutations_of_missing_environment_variables(subtests):
    """
    This test case verifies that the azure provider will not run when at least
    one of the necessary environment variables is not set if called without
    additional command line arguments.
    """
    setup_funs = {
        (_set_client_id, "AZURE_CLIENT_ID"),
        (_set_client_secret, "AZURE_CLIENT_SECRET"),
        (_set_subscription_id, "AZURE_SUBSCRIPTION_ID"),
        (_set_tenant_id, "AZURE_TENANT_ID"),
    }

    for fun, env in setup_funs:
        with subtests.test(msg=f"Testing without {env} being set"):
            for setup_fun, _ in setup_funs - {fun}:
                setup_fun()

            del os.environ[env]

            expected = f"azure provider is missing the '{env}'.\n"

            runner = click.testing.CliRunner()
            actual = runner.invoke(azure.azure, args=["--prefix=test"]).output

            assert actual == expected


def _set_client_id():
    os.environ["AZURE_CLIENT_ID"] = "Azure_Client_Id"


def _set_client_secret():
    os.environ["AZURE_CLIENT_SECRET"] = "Azure_Client_Secret"


def _set_subscription_id():
    os.environ["AZURE_SUBSCRIPTION_ID"] = "Azure_Subscription_Id"


def _set_tenant_id():
    os.environ["AZURE_TENANT_ID"] = "Azure_Tenant_Id"


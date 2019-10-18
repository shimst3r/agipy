# agipy

[![Build Status](https://travis-ci.org/shimst3r/agipy.svg?branch=master)](https://travis-ci.org/shimst3r/agipy)

> /əˈdʒɪˈpaɪ/, portmanteau of AgI (chemical formula of silver iodide) and Python

`agipy` enables you to destroy cloud infrastructure in a hurry. Whether you want to destroy a demo
environment you no longer need or want to purge artifacts a colleague left behind, `agipy` is here
to help you dissolving your cloud problems.

## About the name

`agipy` is a portmanteau of the chemical formula AgI for silver iodide and the word Python. Silver
iodide is a chemical used for [cloud seeding](https://en.wikipedia.org/wiki/Cloud_seeding#Methodology)
and [Python](https://www.python.org/) is the language `agipy` is implemented in.

## How to use `agipy`

To find out how the CLI works, use the built-in help function:

```sh
agipy --help
```

`agipy` is based on the concept of _providers_: For each public cloud provider, a `agipy`-specific
provider module has to be implemented. At the moment, the following provider modules exist:

* [Microsoft Azure](https://azure.microsoft.com/en-us/)

Because each provider has its own semantics, please refer to the respective subsection.

### How to use the `azure` provider

As of yet, the `azure` provider is capable of deleting all resource groups with a specific prefix.
For using the provider, you have to set the following environment variables:

* `AZURE_CLIENT_ID`, the service principal ID
* `AZURE_CLIENT_SECRET`, the service principal secret
* `AZURE_SUBSCRIPTION_ID`
* `AZURE_TENANT_ID`

Then you can call the provider via:

```sh
agipy azure --prefix=${RG_PREFIX}
```

## How to Test

The test suite is based on the great [`pytest`][1] library. Once installed, the automatic test
discovery can be used via

```sh
pytest agipy
```

## How to Contribute

This project is released under the GPL license because I opt for a wide acceptance rate. This also
means that I am happy for contributions! This can be done on many ways:

* Open PRs with improvements,
* add issues if you find bugs,
* add issues for new features,
* use `agipy` and spread the word.

PRs have to comply with:

* [`black`](https://black.readthedocs.io/en/stable/),
* [`mypy`](http://mypy-lang.org),
* and [`pylint`](https://www.pylint.org).

New features must be covered by proper tests (idealy unit tests and functional tests) using the [`pytest`][1] library.

## Contributors

* [shimst3r](https://twitter.com/shimst3r)

## License

> agipy enables you to destroy cloud infrastructure in a hurry.
> Copyright (C) 2019  Nils Müller<shimst3r@gmail.com>
>
> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
>
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
>
> You should have received a copy of the GNU General Public License
> along with this program.  If not, see <https://www.gnu.org/licenses/>

[1]: https://docs.pytest.org/en/latest/
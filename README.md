![Python checks](https://github.com/leakquicked/netdata-parser/actions/workflows/python-checks.yml/badge.svg)

# Netdata Parser

Summarize local newline-delimited JSON telemetry exports.

## Requirements
Python 3.10+, standard library only.

## Usage
`python netdata_parser.py --help`

Supply a local text export or copied response headers. This tool is passive: it does not contact websites or alter configuration. Findings are advisory and require review in context.

## Tests
`python -m unittest discover -s tests -v`

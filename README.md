# mission-payout-generator

Given a CSV of data in the following format:

`<mission type>,<mission size>,<participant 1 name>,...,<participant n name>`

Where:

* `mission type` can be:
  * Combat
  * Gathering
  * Trading
  * Fishing

* `mission size` can be:
  * S
  * M
  * L
  * XL

## Usage

1. Place your `input.csv` in the same folder as `main.exe`.
2. Run`main.exe`.

**From terminal:**

* **Python 3.5+ installed**: Run `python main.py <optional_input_file> <optional_output_file>`
  * It will default to `input.csv` and `output.csv` if the input and output filenames aren't specified.

OR

* **Python not installed**: Run `main.exe <optional_input_file> <optional_output_file>`
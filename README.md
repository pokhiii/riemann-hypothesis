# Riemann Hypothesis

This project provides a Python script that approximates the non-trivial zeros of the Riemann zeta function along the critical line, offering insights into the Riemann Hypothesis. It includes a main script to verify the initial zeros and an extended test script for further exploration.

## Getting Started

### Prerequisites
- Python 3.12 or later
- `mpmath` library for high-precision calculations

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/pokhiii/riemann-hypothesis.git
   cd riemann-hypothesis
   ```

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the main script and see the first 20 zeros of the zeta function on the critical line:
```bash
python main.py
```

To conduct an extended test, which evaluates additional points along the critical line, you can run:
```bash
python test.py
```

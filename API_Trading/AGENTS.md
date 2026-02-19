# AGENTS.md

- This file provides guidance to agents when working with code in this repository.
- API documentation for Groww API is available at local documentation on "Groww/Documentation" folder.

## Project Overview
Python trading API project for Groww and Zerodha platforms. No formal build system, tests, or linting configured.

## Dependencies
- `growwapi` - Primary API client (install via: `pip install growwapi`)
- `pandas` - Data manipulation
- `requests` - HTTP client
- `numpy` - Numerical computing
- API documentation available at https://growwapi.readthedocs.io or check growwapi package source

## Running Scripts
```bash
# Run any Python script directly
python Groww/<script_name>.py
```

## Non-Obvious Conventions

### API Credentials
- Credentials are hardcoded in each script file (not in environment variables)
- `API_AUTH_TOKEN` variable holds the JWT token
- Tokens expire frequently - regenerate via Groww dashboard if API calls fail

### Data Patterns
- `get_positions_for_user()` returns dict with `'positions'` key containing list
- `get_holdings_for_user()` returns dict with `'holdings'` key containing list
- LTP queries require exchange prefix: `NSE_{symbol}` or `BSE_{symbol}`
- Segment always uses `groww.SEGMENT_CASH`


### Symbol Formatting
- NSE stocks: `NSE_RELIANCE`
- BSE stocks: `BSE_IDEABO` (note: BSE uses different suffix)
- Check `tradable_exchanges` field in holdings to determine exchange

## Critical Gotchas
- `time.sleep(1)` required between API calls to avoid rate limiting
- Token in `Test.py` differs from `Get_Get_LTP.py` - each file has its own token
- `groww.PRODUCT_MIS` used for intraday, `groww.PRODUCT_CNC` for delivery
- Exception handling uses bare `except Exception as e` pattern
- CSV exports via `dataframe.to_csv('filename.csv')` - uncomment to enable

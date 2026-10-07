# Winch Law Firm website
Replacement main-site source for Netlify hosting. Live main domain remains on Wix until acceptance checks pass. Read [migration status](MIGRATION_STATUS.md).

## Build and check
Python 3.11+:
```
pip install -r requirements.txt
python build.py
python tests/check_site.py
node --check src-assets/site.js
```
Netlify uses netlify.toml: build command installs dependencies and runs build.py; publish directory public; production branch main. Set GA_MEASUREMENT_ID only after verifying the intended GA4 stream. Enable Netlify form detection and configure/test firm email notifications before launch.

Source: build.py page templates, migration/ preserved sanitized Wix content, src-assets/ CSS and JS, brand/ approved imagery. public/ is generated deploy output. Never store credentials, inquiry submissions, or private client files in this public repository.

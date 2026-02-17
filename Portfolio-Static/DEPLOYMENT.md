# GitHub Actions Deployment

This project deploys `Portfolio-Static` to Netlify using GitHub Actions.

## Workflow

The workflow file is:

- `.github/workflows/deploy-portfolio-static.yml`

It runs when:

- code under `Portfolio-Static/` changes on `master`
- the workflow file changes
- you trigger it manually from **Actions** (`workflow_dispatch`)

## Required GitHub Secrets

Add these repository secrets in **GitHub -> Settings -> Secrets and variables -> Actions**:

- `NETLIFY_AUTH_TOKEN`
- `NETLIFY_SITE_ID`

## How to get values

### `NETLIFY_AUTH_TOKEN`

1. Log into Netlify.
2. Go to **User settings -> Applications -> Personal access tokens**.
3. Generate a new token.
4. Save it as `NETLIFY_AUTH_TOKEN` in GitHub secrets.

### `NETLIFY_SITE_ID`

1. Open your site in Netlify.
2. Go to **Site configuration -> General**.
3. Copy the **Site ID**.
4. Save it as `NETLIFY_SITE_ID` in GitHub secrets.

## Notes

- The workflow deploys production directly (`--prod`).
- Serverless functions are deployed from `Portfolio-Static/netlify/functions`.
- If your functions use environment variables (example: `NEWS_API_KEY`), set them in Netlify site environment variables.

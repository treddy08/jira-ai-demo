# Jira AI Integration Demo

This is a demo repository showing how to use the RHPDS reusable Jira AI workflow.

## How it works

1. The `.jira` file contains the Jira ticket number: `RHCLOUD-1234`
2. When you push commits, GitHub Actions automatically:
   - Gets the commit diff
   - Analyzes it with Claude AI
   - Posts a summary to the Jira ticket

## Testing the workflow

1. Make a code change:
   ```bash
   # Edit app.py
   git add app.py
   git commit -m "Improve password validation"
   git push
   ```

2. Check the Actions tab to see the workflow run

3. Check Jira ticket RHCLOUD-1234 for the AI-generated comment

## Switching Jira tickets

To work on a different ticket:
```bash
echo "RHCLOUD-5678" > .jira
git add .jira
git commit -m "Switch to new Jira ticket"
git push
```

## Workflow file

See `.github/workflows/jira-update.yml` for the simple caller that references the reusable workflow.

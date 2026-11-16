# GitHub Actions Account Creator - PUBLIC REPO

**PUBLIC REPO = UNLIMITED FREE MINUTES!**

## Target: 500,000 accounts

## Math:

Per workflow run:
- 20 parallel jobs (20 different GitHub runner IPs)
- ~5 accounts per job before rate limit
- = **~100 accounts per run**

With public repo (no limits):
- Run every 10 minutes = 144 runs/day
- 144 runs × 100 accounts = **~14,400 accounts/day**
- **500k accounts in ~35 days**

## Speed up options:
- Run more frequently (every 5 min) = ~30 days
- Increase parallel jobs (up to 256) = ~3 days
- Use multiple repos = ~1-2 days

## Deploy to Public Repo:

### Step 1: Sign out of current GitHub account
Go to GitHub.com → Sign out

### Step 2: Create new GitHub account (or use existing alt account)
- Use different email
- Verify email

### Step 3: Create PUBLIC repository
- Name it anything (e.g., "test-runner")
- Make it PUBLIC
- Don't initialize with README

### Step 4: Push this folder
```bash
cd C:\Users\Administrator\fafo\github_actions
git init
git add .
git commit -m "Init"
git remote add origin https://github.com/YOUR_NEW_USERNAME/test-runner.git
git branch -M main
git push -u origin main
```

### Step 5: Enable Actions
- Go to repo → Actions tab
- Click "I understand my workflows, go ahead and enable them"

### Step 6: Watch it run
- Workflow runs automatically every 10 minutes
- Or click "Run workflow" to start immediately

## Get Results:
- Go to Actions → Click on a run → Download artifacts
- Each artifact = accounts from that job

## Timeline (500k):
- Week 1: ~100k accounts
- Week 2: ~200k accounts
- Week 3: ~300k accounts
- Week 4: ~400k accounts
- Week 5: **500k accounts**

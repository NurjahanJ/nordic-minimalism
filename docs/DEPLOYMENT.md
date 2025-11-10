# GitHub Pages Deployment Guide

## Overview

This Nordic Minimalism website is configured for automatic deployment to GitHub Pages using GitHub Actions. Every push to the `main` branch triggers an automated deployment.

## Setup Instructions

### 1. Repository Configuration

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Add GitHub Pages deployment configuration"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Navigate to **Settings** → **Pages**
   - Under **Source**, select **GitHub Actions**
   - The workflow will automatically deploy your site

### 2. Deployment Workflow

The deployment is handled by `.github/workflows/deploy.yml` which:

- **Triggers on:** Push to `main` branch or manual dispatch
- **Permissions:** Read contents, write to Pages, use ID token
- **Process:**
  1. Checks out the repository
  2. Sets up GitHub Pages configuration
  3. Uploads the entire project as a Pages artifact
  4. Deploys to GitHub Pages

### 3. File Structure for Deployment

```
nordic-minimalism/
├── .github/
│   └── workflows/
│       └── deploy.yml          # Deployment workflow
├── .nojekyll                   # Prevents Jekyll processing
├── index.html                  # Main page (required for Pages)
├── about.html                  # About page
├── designers.html              # Designers page
├── timeline.html               # Timeline page
├── styles.css                  # Nordic design system
├── README.md                   # Project documentation
├── DEPLOYMENT.md               # This file
├── docs/                       # Project documentation
└── research/                   # Design research files
```

### 4. Accessing Your Site

Once deployed, your site will be available at:
```
https://[your-username].github.io/nordic-minimalism
```

Replace `[your-username]` with your actual GitHub username.

### 5. Deployment Status

- **Build Status:** Check the Actions tab in your repository
- **Deployment URL:** Available in the Pages settings after first deployment
- **Custom Domain:** Can be configured in Pages settings if desired

## Workflow Features

### Automatic Deployment
- **On Push:** Every commit to `main` triggers deployment
- **Manual Trigger:** Can be manually triggered from Actions tab
- **Concurrency Control:** Prevents multiple deployments running simultaneously

### Optimizations
- **No Jekyll Processing:** `.nojekyll` file ensures direct file serving
- **Artifact Upload:** Entire project uploaded for complete site deployment
- **Permissions:** Minimal required permissions for security

## Troubleshooting

### Common Issues

1. **404 Error:** Ensure `index.html` is in the root directory
2. **CSS Not Loading:** Check file paths are relative (no leading `/`)
3. **Deployment Failed:** Check Actions tab for error details
4. **Pages Not Enabled:** Verify Pages is enabled in repository settings

### Checking Deployment

1. Go to **Actions** tab in your repository
2. Click on the latest workflow run
3. Check each step for success/failure status
4. View deployment URL in the workflow summary

## Nordic Design Considerations

This deployment preserves all Nordic minimalism principles:

- **Fast Loading:** Static HTML/CSS with optimized fonts
- **Accessibility:** Semantic structure maintained in deployment
- **Clean URLs:** GitHub Pages provides clean, Nordic-appropriate URLs
- **Responsive Design:** Mobile-first approach works perfectly with Pages

## Maintenance

### Updating the Site
1. Make changes to your local files
2. Commit and push to `main` branch
3. Deployment happens automatically
4. Check Actions tab to monitor progress

### Branch Strategy
- **Main Branch:** Production-ready code, auto-deploys
- **Feature Branches:** Development work, no auto-deployment
- **Pull Requests:** Review changes before merging to main

---

*This deployment configuration embodies Nordic principles of simplicity and functionality—elegant, minimal setup with maximum effectiveness.*

---
title: Your First Contribution
weight: 2
---

Follow these steps to open your first pull request against a MATE repository.

## 1. Fork the repository

Go to the GitHub page of the MATE package you want to work on and click the **Fork** button. This creates your own copy of the repository under your GitHub account.

## 2. Clone your fork

```bash
git clone https://github.com/<your-username>/<package-name>
```

## 3. Create a branch

Always work on a dedicated branch, not directly on `master`:

```bash
git checkout -b my-fix
```

## 4. Make and test your changes

Edit the source files, then [build and install](../building) the package to verify your changes work.

## 5. Commit

```bash
git add modified-file.c
git commit -m "Short description of the change"
```

Write a commit message that explains *what* changed and *why*.

## 6. Push and open a pull request

```bash
git push origin my-fix
```

Then go to your fork on GitHub. You will see a **Compare & pull request** banner — click it and submit the PR. A maintainer will review it and may ask for changes.

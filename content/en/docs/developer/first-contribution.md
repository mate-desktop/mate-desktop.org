---
title: Your First Contribution
weight: 6
---

Follow these steps to open your first pull request against a MATE repository. Make sure you can [build the package](../building) before starting.

{{% steps %}}

### Fork the repository

Go to the GitHub page of the MATE package you want to work on and click the **Fork** button. This creates your own copy of the repository under your GitHub account.

### Clone your fork

```bash
git clone https://github.com/<your-username>/<package-name>
```

### Create a branch

Always work on a dedicated branch, not directly on `master`:

```bash
git checkout -b my-fix
```

### Make and test your changes

Edit the source files, then [build and install](../building) the package to verify your changes work. Use the [debugging tools](../debugging) if something does not behave as expected.

### Commit

```bash
git add modified-file.c
git commit -m "Short description of the change"
```

Write a commit message that explains *what* changed and *why*.

### Push and open a pull request

```bash
git push origin my-fix
```

Go to your fork on GitHub. You will see a **Compare & pull request** banner — click it and submit the PR. A maintainer will review it and may ask for changes.

{{% /steps %}}
## Tips

- Keep pull requests focused — one bug fix or feature per PR.
- If you are fixing a reported issue, reference it in the PR description: `Fixes #123`.
- It is fine to open a draft PR early to get feedback on your approach.

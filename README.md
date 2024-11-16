# sitcen-template

A standardised template for sitcen analyst repositories.
Below is a checklist which must be completed when using this template to make a new repo.

## Setup Checklist

### Create the repo

- [ ] Click 'use as template' and follow the prompts or [follow these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

### Add Collaborators

This will allow people to access the repo using best practice and following CO policy.

Click 'settings' -> 'Collaborators and teams' -> 'add teams' and add the following:

- [ ] 'SitCen Analysts Admins' and give it 'Admin' privileges
- [ ] 'SitCen Team' and give it 'Write' privileges

You must then remove yourself as admin, if you are not in the 'SitCen Analysts Admins' request to be added via the analyst group chat. It is CO policy that only teams should be added to repos not individuals.

- [ ] Removed myself as admin

### Protect main

This will prevent anyone pushing code without approval and from deleting code from main.

Click

1. Settings
2. Rules
3. Rulesets
4. New Branch Ruleset
5. New ruleset

Change the following settings

#### General

- [ ] Name -> 'Protect main'
- [ ] Enforcement status -> Active

#### Bypass list

Very important that no one is added to this

#### Targets

Click

1. Add Target
2. Include default branch

- [ ] Added default branch

#### Rules

- [ ] Restrict creations -> False
- [ ] Restrict updates -> False
- [ ] Restrict deletions -> True
- [ ] Require linear history -> False
- [ ] Require merge queue -> False
- [ ] Require deployments to succeed -> False
- [ ] Require signed commits -> False
- [ ] Require a pull request before merging -> True
  - [ ] Required approvals -> 1
  - [ ] Dismiss stale pull request approvals when new commits are pushed -> True
  - [ ] Require review from Code Owners -> False
  - [ ] Require approval of the most recent reviewable push -> True
  - [ ] Require conversation resolution before merging -> True
  - [ ] Request pull request review from Copilot -> False
- [ ] Require status checks to pass -> True
  - [ ] Require branches to be up to date before merging -> True
  - [ ] Do not require status checks on creation -> True
  - [ ] Add the following status checks
    - [ ] ruff_format
    - [ ] ruff_lint
    - [ ] trufflehog
    - [ ] bandit
    - [ ] gitlint
    - [ ] merge_conflict_markers
- [ ] Block forced pushes -> True
- [ ] Require code scanning results -> False

#### Restrictions

- [ ] Restrict commit metadata -> False
- [ ] Restrict branch names -> False

### Change General Settings

Click

1. Settings
2. General

Then change the following settings

- [ ] Ensure repo name begins with 'sitcen-'
- [ ] Template repository -> False
- [ ] Require contributors to sign off on web-based commits -> False
- [ ] Default branch -> main
- [ ] Wikis -> False
- [ ] Issues -> True
- [ ] Allow Forking -> True
- [ ] Sponsorships -> False
- [ ] Discussions -> False
- [ ] Projects -> True
- [ ] Allow merge commits -> False
- [ ] Allow squash merging -> True
- [ ] Default commit message -> Pull request title and commit details
- [ ] Allow rebase merging Loading -> False
- [ ] Always suggest updating pull request branches Loading -> True
- [ ] Allow auto-merge  -> True
- [ ] Automatically delete head branches -> True
- [ ] Limit how many branches and tags can be updated in a single push -> True -> 2

### Update README.md

Remove this checklist and update the README.md so it is relevant to the purpose of the Repo.

- [ ] The following instructions must be included:

  ## Local Installation

    ```sh
    git clone git+ssh://git@github.com/cabinetoffice/<repo-name-here>.git
    ```

- [ ] If this repo will be used as a package the following must also be included.

  ## Using this Package

    To install this package in terminal run.

    ```sh
    pip install git+ssh://git@github.com/cabinetoffice/<repo-name-here>
    ```

    Further documentation on this project can be found in the [SitCen Docs](https://github.com/cabinetoffice/sitcen-docs).

- [ ] Add commit format guide
  ## Commit Format
  
  This project follows the [Conventional Commit Format](https://www.conventionalcommits.org/en/v1.0.0/). To ensure adherence to this standard, [gitlint](https://jorisroovers.com/gitlint/latest/) is used to enforce the format on commit messages as a pre-commit hook. Additionally, gitlint is applied to the pull request title as part of a continuous integration (CI) check conducted by GitHub Actions.
  
  To ensure your commit messages follow the Conventional Commits specification, use the following structure:
  
  `<type>: <description>`
  
  ### Key Elements
  
  - **type:** Must be one of the following:
  
    - `build`: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
    - `ci` Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
    - `docs` Documentation only changes
    - `feat` A new feature
    - `fix` A bug fix
    - `perf` A code change that improves performance
    - `refactor` A code change that neither fixes a bug nor adds a feature
    - `style` Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
    - `test` Adding missing tests or correcting existing tests
    - `revert` If the commit reverts a previous commit, it should begin with `revert: `, followed by the header of the reverted commit. In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.
  
  - **Description:** A brief summary of the changes made in the commit.
  
  ### Examples
  
  `feat: adds a rolling average line to the gas production chart`

  `fix: prevent racing of requests`
___
___
**This README content should have now been deleted.**

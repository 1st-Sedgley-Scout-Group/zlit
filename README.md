# zlit

A streamlit application to show zettle data.

## Local Installation

  ```sh
  git clone git+ssh://git@github.com/1st-Sedgley-Scout-Group/zlit.git
  ```

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

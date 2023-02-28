## Contributing

[fork]: /fork
[pr]: /compare
[code-of-conduct]: CODE_OF_CONDUCT.md

Hi there! We're thrilled that you'd like to contribute to this project. Your help is essential for keeping it great.

Please note that this project is released with a [Contributor Code of Conduct][code-of-conduct]. By participating in this project you agree to abide by its terms.

## Issues and PRs

If you have suggestions for how this project could be improved, or want to report a bug, open an issue! We'd love all and any contributions. If you have questions, too, we'd love to hear them.

We'd also love PRs. If you're thinking of a large PR, we advise opening up an issue first to talk about it, though! Look at the links below if you're not sure how to open a PR.

## Submitting a pull request

1. Create a folder at your desire location (usually at your desktop).

2. Open Git Bash Here


3. [Fork](https://github.com/SANTHOSH17-DOT/attack-vectors-suite) the project. Click on the <a href="https://github.com/SANTHOSH17-DOT/attack-vectors-suite/fork"><img src="https://i.imgur.com/G4z1kEe.png" height="15" width="15"></a> icon in the top right to get started.

4. Clone your forked repository of project.

```bash
git clone https://github.com/SANTHOSH17-DOT/attack-vectors-suite.git
```

5. Navigate to the project directory.

```bash
cd attack-vectors-suite
```

6. Add a reference(remote) to the original repository.

```bash
git remote add upstream https://github.com/SANTHOSH17-DOT/attack-vectors-suite.git
```

7. Check the remotes for this repository.

```bash
git remote -v
```

8. Always take a pull from the upstream repository to your main branch to keep it updated as per the main project repository.

```bash
git pull upstream main
```

9. Create a new branch(prefer a branch name that relates to your assigned issue).

```bash
git checkout -b <YOUR_BRANCH_NAME>
```

10. Perform your desired changes to the code base.

11. Check your changes.

```bash
git status
```

```bash
git  diff
```

12. Stage your changes.

```bash
git add . <\files_that_you_made_changes>
```

13. Commit your changes.

```bash
git commit -m "Commit Message"
```

14. Push the committed changes in your feature branch to your remote repository.

```bash
git push -u origin <your_branch_name>
```

15. To create a pull request, click on `compare and pull requests`.

16. Add an appropriate title and description to your PR explaining your changes.

17. Click on `Create pull request`.

Congratulations🎉, you have made a PR to the attack-vectors-suite.
Wait for your submission to be accepted and your PR to be merged by a maintainer.

- Please adhere to this project's CODE_OF_CONDUCT.md and CONTRIBUTING.md guidelines.

Here are a few things you can do that will increase the likelihood of your pull request being accepted:

- Keep your changes as focused as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as separate pull requests.
- Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

Work in Progress pull requests are also welcome to get feedback early on, or if there is something blocked you.

## Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)


QUESTION_BANK_GIT_INTERMEDIATE2 = [
    {
        "skill": "Git & GitHub",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_text": "What is the purpose of the git merge-base command?",
                "options": ["Find the best common ancestor of two commits", "Create a merge commit automatically", "Delete a branch's history", "List all remote URLs"],
                "correct_answer": 0,
                "explanation": "git merge-base finds the best common ancestor shared by two commits."
            },
            {
                "question_text": "Which command displays the common ancestor of main and feature branches?",
                "options": ["git merge-base main feature", "git branch-base main feature", "git diff-base main feature", "git log-base main feature"],
                "correct_answer": 0,
                "explanation": "git merge-base returns the best common ancestor of the supplied commits."
            },
            {
                "question_text": "What is the purpose of git log --graph?",
                "options": ["Display commit history as an ASCII graph", "Create a graphical user interface", "Generate a repository image", "Display only file permissions"],
                "correct_answer": 0,
                "explanation": "The --graph option draws an ASCII representation of branch and merge history."
            },
            {
                "question_text": "Which command shows commits present in feature but not in main?",
                "options": ["git log main..feature", "git log feature..main", "git status main feature", "git diff --branches"],
                "correct_answer": 0,
                "explanation": "The range main..feature selects commits reachable from feature but not from main."
            },
            {
                "question_text": "What does git log --all display?",
                "options": ["Commit history reachable from all references", "Only commits on the current branch", "Only untracked files", "All GitHub pull requests"],
                "correct_answer": 0,
                "explanation": "The --all option considers all references when displaying commit history."
            },
            {
                "question_text": "What is the purpose of git log --author?",
                "options": ["Filter commits by author information", "Change the author of every commit", "Create an author account on GitHub", "Display only merge conflicts"],
                "correct_answer": 0,
                "explanation": "The --author option filters commits whose author matches the supplied pattern."
            },
            {
                "question_text": "Which command displays commits that changed a particular file?",
                "options": ["git log -- path/to/file", "git branch -- path/to/file", "git remote -- path/to/file", "git clean -- path/to/file"],
                "correct_answer": 0,
                "explanation": "The path-limited git log displays commits affecting the specified file."
            },
            {
                "question_text": "What does git diff --check help detect?",
                "options": ["Whitespace errors such as trailing whitespace", "Missing remote repositories", "Expired GitHub accounts", "Deleted branch names"],
                "correct_answer": 0,
                "explanation": "git diff --check reports whitespace errors in changes, including trailing whitespace."
            },
            {
                "question_text": "What does git diff --stat display?",
                "options": ["A summary of changed files and the number of changed lines", "Only the current branch name", "The repository's remote URL", "All commit messages in full"],
                "correct_answer": 0,
                "explanation": "The --stat option summarizes changed files and line counts."
            },
            {
                "question_text": "Which command displays only the names of staged files?",
                "options": ["git diff --cached --name-only", "git log --name-only", "git branch --cached", "git remote --cached"],
                "correct_answer": 0,
                "explanation": "git diff --cached --name-only lists paths changed in the index compared with HEAD."
            },
            {
                "question_text": "What does git status --short provide?",
                "options": ["A compact status representation", "A short commit history", "A list of remote users", "A shortened repository URL"],
                "correct_answer": 0,
                "explanation": "The --short option displays a compact two-column status for changed paths."
            },
            {
                "question_text": "What does the first status column in git status --short generally represent?",
                "options": ["The state of the index or staging area", "The remote repository name", "The file's creation date", "The current Git version"],
                "correct_answer": 0,
                "explanation": "In short status output, the first column represents the index state."
            },
            {
                "question_text": "What does the second status column in git status --short generally represent?",
                "options": ["The working-tree state", "The latest remote commit message", "The current user's email", "The file's storage size"],
                "correct_answer": 0,
                "explanation": "In short status output, the second column represents working-tree changes."
            },
            {
                "question_text": "What does git add -p allow a developer to do?",
                "options": ["Interactively stage selected parts of changes", "Push selected commits automatically", "Delete selected remote branches", "Rename every modified file"],
                "correct_answer": 0,
                "explanation": "Interactive patch mode lets developers choose individual change hunks to stage."
            },
            {
                "question_text": "What is a hunk in Git diff output?",
                "options": ["A section of changes shown together in a diff", "A type of remote repository", "A GitHub user role", "A commit signature"],
                "correct_answer": 0,
                "explanation": "A hunk is a contiguous section of changed lines represented in a diff."
            },
            {
                "question_text": "Which command interactively stages portions of a file?",
                "options": ["git add -p filename", "git commit -p filename", "git push -p filename", "git branch -p filename"],
                "correct_answer": 0,
                "explanation": "git add -p opens interactive patch mode for the specified file."
            },
            {
                "question_text": "What does git restore --source=HEAD~1 filename do?",
                "options": ["Restores the file from the commit before HEAD", "Deletes the previous commit", "Creates a new branch from HEAD~1", "Pushes the previous file to origin"],
                "correct_answer": 0,
                "explanation": "The --source option selects the tree from which the file is restored."
            },
            {
                "question_text": "What is the purpose of git checkout -- filename in older Git workflows?",
                "options": ["Discard unstaged changes to the file by restoring it from the index", "Commit the file", "Create a remote branch", "Display the file's commit history"],
                "correct_answer": 0,
                "explanation": "This older checkout form restores the working-tree file from the index."
            },
            {
                "question_text": "What does git rm --cached filename do?",
                "options": ["Remove the file from Git's index while keeping it in the working directory", "Delete the file from disk and history", "Rename the file", "Add the file to a remote branch"],
                "correct_answer": 0,
                "explanation": "The --cached option removes the file from tracking in the index without deleting the working copy."
            },
            {
                "question_text": "What is the purpose of git update-index?",
                "options": ["Directly modify information stored in Git's index", "Update a GitHub account profile", "Create a new remote repository", "Change the current commit message"],
                "correct_answer": 0,
                "explanation": "git update-index is a lower-level command for manipulating the index."
            },
            {
                "question_text": "What does git assume-unchanged do?",
                "options": ["Hints to Git to avoid checking a tracked file for changes in normal status operations", "Permanently ignores the file in every clone", "Deletes the file from the repository", "Prevents all developers from editing the file"],
                "correct_answer": 0,
                "explanation": "The assume-unchanged bit is a performance-related hint and is not a reliable replacement for .gitignore."
            },
            {
                "question_text": "What is the purpose of git skip-worktree?",
                "options": ["Mark an index entry so Git avoids updating that path in the working tree in certain operations", "Remove a file from every commit", "Skip all commits during rebase", "Ignore every file in a directory permanently"],
                "correct_answer": 0,
                "explanation": "skip-worktree is an index bit used by Git for special working-tree handling; it is not a general-purpose ignore rule."
            },
            {
                "question_text": "What is the purpose of git check-ignore?",
                "options": ["Determine which ignore rule matches a path", "Check whether a commit is signed", "Verify a remote URL", "Find merge conflicts in a branch"],
                "correct_answer": 0,
                "explanation": "git check-ignore reports whether paths are ignored and can show the matching rule."
            },
            {
                "question_text": "Which command displays the ignore rule responsible for excluding a file?",
                "options": ["git check-ignore -v filename", "git status -v filename", "git log --ignore filename", "git branch -v filename"],
                "correct_answer": 0,
                "explanation": "The -v option shows the source file, line number, and pattern responsible for ignoring a path."
            },
            {
                "question_text": "Where can Git ignore rules be configured for an individual repository?",
                "options": ["In the repository's .gitignore file", "Only in README.md", "Only in the remote URL", "Inside every commit message"],
                "correct_answer": 0,
                "explanation": "A repository-level .gitignore file stores patterns that apply to paths within that repository."
            },
            {
                "question_text": "What is the purpose of .git/info/exclude?",
                "options": ["Define repository-local ignore patterns that are not committed", "Store remote authentication tokens", "Record every merge commit", "Configure GitHub pull request templates"],
                "correct_answer": 0,
                "explanation": ".git/info/exclude provides local ignore rules that are not shared through commits."
            },
            {
                "question_text": "What is a global Git ignore file used for?",
                "options": ["Ignore common files across multiple repositories for one user", "Ignore files for every user on GitHub", "Delete files from remote repositories", "Replace repository-level branches"],
                "correct_answer": 0,
                "explanation": "A global excludes file applies user-specific ignore patterns across repositories."
            },
            {
                "question_text": "What does git config --list display?",
                "options": ["Git configuration settings visible to the current command", "Every commit in the repository", "All GitHub organization members", "All files in the staging area"],
                "correct_answer": 0,
                "explanation": "git config --list displays effective configuration values from applicable configuration sources."
            },
            {
                "question_text": "Which command sets the default initial branch name to main for new repositories?",
                "options": ["git config --global init.defaultBranch main", "git branch --global main", "git init --default main", "git remote set-default main"],
                "correct_answer": 0,
                "explanation": "init.defaultBranch controls the initial branch name created by git init."
            },
            {
                "question_text": "What does git config --local change?",
                "options": ["Configuration for the current repository", "System-wide configuration for every user", "GitHub account settings", "Remote server operating-system settings"],
                "correct_answer": 0,
                "explanation": "The --local scope writes configuration to the current repository's configuration file."
            },
            {
                "question_text": "What is the purpose of git config --show-origin?",
                "options": ["Show where configuration values were defined", "Display the original repository creator", "Show the first commit in history", "Display the original file name"],
                "correct_answer": 0,
                "explanation": "The --show-origin option identifies the configuration file or source for each value."
            },
            {
                "question_text": "What does git credential helper manage?",
                "options": ["Storage and retrieval of authentication credentials", "Commit message formatting", "Branch merge strategies", "File compression settings"],
                "correct_answer": 0,
                "explanation": "Credential helpers integrate Git with mechanisms for storing or retrieving credentials."
            },
            {
                "question_text": "Why is a personal access token commonly used for HTTPS Git operations on GitHub?",
                "options": ["It provides token-based authentication instead of account-password authentication", "It replaces the Git repository", "It automatically approves pull requests", "It changes the branch protection rules"],
                "correct_answer": 0,
                "explanation": "GitHub supports personal access tokens for HTTPS Git authentication, subject to token permissions."
            },
            {
                "question_text": "What is SSH authentication commonly used for with GitHub?",
                "options": ["Authenticate Git operations using a configured SSH key pair", "Encrypt every source-code variable automatically", "Create a new Git commit", "Replace all repository permissions"],
                "correct_answer": 0,
                "explanation": "An SSH public key registered with GitHub can authenticate Git operations from a matching private key."
            },
            {
                "question_text": "Which command tests SSH authentication with GitHub?",
                "options": ["ssh -T git@github.com", "git test github --ssh", "git remote verify-ssh", "ssh git status github"],
                "correct_answer": 0,
                "explanation": "ssh -T git@github.com tests whether SSH authentication with GitHub succeeds."
            },
            {
                "question_text": "What is the main difference between HTTPS and SSH Git remote URLs?",
                "options": ["They use different transport and authentication methods", "HTTPS cannot push commits", "SSH cannot clone repositories", "They always point to different repository contents"],
                "correct_answer": 0,
                "explanation": "HTTPS and SSH are different transport methods and use different authentication setups."
            },
            {
                "question_text": "What does git remote set-url origin URL do?",
                "options": ["Change the URL associated with the origin remote", "Create a new local branch", "Delete all remote commits", "Change the GitHub repository owner"],
                "correct_answer": 0,
                "explanation": "git remote set-url updates the URL configured for an existing remote."
            },
            {
                "question_text": "What is the purpose of git push --force-with-lease?",
                "options": ["Force-update a remote reference only if it still matches the expected state", "Push every local branch without checking", "Delete all remote tags", "Convert a merge into a rebase"],
                "correct_answer": 0,
                "explanation": "The lease check helps avoid overwriting remote work that appeared after the last fetch."
            },
            {
                "question_text": "Why is git push --force generally risky on a shared branch?",
                "options": ["It can overwrite commits pushed by other collaborators", "It always deletes local files", "It converts all commits into tags", "It disables Git authentication"],
                "correct_answer": 0,
                "explanation": "A force push can rewrite the remote branch and make other collaborators' commits unreachable from that branch."
            },
            {
                "question_text": "What is the purpose of a protected branch on GitHub?",
                "options": ["Apply rules that restrict changes or require checks before updates", "Hide the branch from its repository owner", "Automatically delete old commits", "Prevent all pull requests from being created"],
                "correct_answer": 0,
                "explanation": "Branch protection rules can require reviews, status checks, or restrict direct updates."
            },
            {
                "question_text": "What is a required status check in a GitHub pull request?",
                "options": ["An automated check that must pass before merging under the applicable rules", "A manual Git installation step", "A required commit message length", "A list of repository stars"],
                "correct_answer": 0,
                "explanation": "Required status checks enforce successful CI or other configured checks before a protected branch can be updated."
            },
            {
                "question_text": "What is the purpose of GitHub CODEOWNERS?",
                "options": ["Specify people or teams responsible for reviewing changes to certain paths", "List every Git commit author", "Store repository passwords", "Configure local Git aliases"],
                "correct_answer": 0,
                "explanation": "CODEOWNERS defines ownership patterns that can request reviews from designated users or teams."
            },
            {
                "question_text": "Where can a CODEOWNERS file be placed for GitHub to recognize it?",
                "options": ["In the repository root, .github/, or docs/ directory", "Only inside node_modules/", "Only in the user's home directory", "Only in the Git object database"],
                "correct_answer": 0,
                "explanation": "GitHub recognizes CODEOWNERS in the repository root, .github/, or docs/ directory, using the applicable search precedence."
            },
            {
                "question_text": "What is the purpose of a GitHub pull request draft?",
                "options": ["Indicate that a proposed change is not yet ready for review or merging", "Delete the source branch automatically", "Create a release tag", "Make the repository private"],
                "correct_answer": 0,
                "explanation": "Draft pull requests communicate that work is still in progress and is not yet ready for normal review."
            },
            {
                "question_text": "What does marking a GitHub pull request as ready for review do?",
                "options": ["Convert a draft pull request into a review-ready pull request", "Merge it automatically", "Delete all review comments", "Close the target branch"],
                "correct_answer": 0,
                "explanation": "The ready-for-review action changes a draft pull request to an open review-ready state."
            },
            {
                "question_text": "What is the purpose of a GitHub review request?",
                "options": ["Ask selected users or teams to review proposed changes", "Request a new Git installation", "Ask Git to delete a commit", "Change the repository's clone URL"],
                "correct_answer": 0,
                "explanation": "Review requests notify selected reviewers that their feedback is needed."
            },
            {
                "question_text": "What does resolving a review conversation in a pull request indicate?",
                "options": ["The discussion thread has been addressed or no longer needs to remain open", "The entire pull request is merged automatically", "The branch is deleted immediately", "All CI checks are skipped"],
                "correct_answer": 0,
                "explanation": "Resolving a conversation marks that review thread as addressed; it does not itself merge the pull request."
            },
            {
                "question_text": "What is the purpose of GitHub Actions?",
                "options": ["Automate workflows such as building, testing, and deploying software", "Replace the Git commit database", "Edit files without a repository", "Manage a computer's hardware drivers"],
                "correct_answer": 0,
                "explanation": "GitHub Actions automates repository workflows through event-triggered jobs."
            },
            {
                "question_text": "What is a workflow file for GitHub Actions commonly stored as?",
                "options": [".yml or .yaml file under .github/workflows/", "A .sql file under src/", "A .git file in the repository root", "A .exe file under node_modules/"],
                "correct_answer": 0,
                "explanation": "GitHub Actions workflow definitions are YAML files stored in .github/workflows/."
            },
            {
                "question_text": "What is the purpose of a GitHub Actions runner?",
                "options": ["Execute jobs defined in a workflow", "Store Git commit messages permanently", "Approve repository invitations", "Replace the remote repository"],
                "correct_answer": 0,
                "explanation": "A runner is the environment that executes the steps in a GitHub Actions job."
            }
        ]
    }
]

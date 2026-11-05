
QUESTION_BANK_GIT_BEGINNER2 = [
    {
        "skill": "Git & GitHub",
        "difficulty": "beginner",
        "questions": [
            {
                "question_text": "Which command displays the version of Git installed on a computer?",
                "options": ["git --version", "git version-check", "git status", "git info"],
                "correct_answer": 0,
                "explanation": "git --version prints the installed Git version."
            },
            {
                "question_text": "Which command displays help information about Git commands?",
                "options": ["git help", "git explain-all", "git manual", "git guide"],
                "correct_answer": 0,
                "explanation": "git help displays help information for Git commands."
            },
            {
                "question_text": "What does the command git status help a developer identify?",
                "options": ["Modified, staged, and untracked files", "The computer's IP address", "The GitHub account password", "The number of installed applications"],
                "correct_answer": 0,
                "explanation": "git status reports the state of the working directory and staging area."
            },
            {
                "question_text": "What happens when git init is executed inside an existing Git repository?",
                "options": ["It reinitializes the repository without deleting its existing history", "It deletes all commits", "It automatically pushes all files", "It creates a GitHub account"],
                "correct_answer": 0,
                "explanation": "Running git init in an existing repository is safe and does not erase its history."
            },
            {
                "question_text": "Which command shows the commit history in a compact one-line format?",
                "options": ["git log --oneline", "git status --short", "git branch --all", "git remote -v"],
                "correct_answer": 0,
                "explanation": "git log --oneline displays each commit using a short hash and subject."
            },
            {
                "question_text": "What does the command git add README.md do?",
                "options": ["Stages README.md for the next commit", "Commits README.md immediately", "Deletes README.md", "Uploads README.md to GitHub immediately"],
                "correct_answer": 0,
                "explanation": "git add stages the file but does not create a commit or push it."
            },
            {
                "question_text": "What does git commit -m \"Initial commit\" do?",
                "options": ["Creates a commit with the supplied message", "Creates a new remote repository", "Downloads the latest changes", "Deletes the staging area"],
                "correct_answer": 0,
                "explanation": "The command records staged changes in a commit with the given message."
            },
            {
                "question_text": "Which command shows the changes introduced by the latest commit?",
                "options": ["git show", "git init", "git remote", "git clean"],
                "correct_answer": 0,
                "explanation": "git show displays information and changes for a commit, defaulting to HEAD."
            },
            {
                "question_text": "What is the purpose of a commit message?",
                "options": ["Describe the changes recorded in a commit", "Store the GitHub password", "Name the computer", "Configure the internet connection"],
                "correct_answer": 0,
                "explanation": "A commit message briefly explains the purpose of the recorded changes."
            },
            {
                "question_text": "Which command creates a new branch named testing?",
                "options": ["git branch testing", "git commit testing", "git remote testing", "git tag testing"],
                "correct_answer": 0,
                "explanation": "git branch testing creates a branch named testing without switching to it."
            },
            {
                "question_text": "Which command switches to the main branch using the switch command?",
                "options": ["git switch main", "git branch main", "git add main", "git merge main"],
                "correct_answer": 0,
                "explanation": "git switch main checks out the existing main branch."
            },
            {
                "question_text": "Which command deletes a local branch named old-feature safely?",
                "options": ["git branch -d old-feature", "git branch -D old-feature", "git rm old-feature", "git delete old-feature"],
                "correct_answer": 0,
                "explanation": "git branch -d deletes a branch when Git considers it safely merged."
            },
            {
                "question_text": "What does the command git branch -a display?",
                "options": ["Local and remote-tracking branches", "Only deleted branches", "Only commit messages", "All files ignored by Git"],
                "correct_answer": 0,
                "explanation": "git branch -a lists both local branches and remote-tracking branches."
            },
            {
                "question_text": "What does git switch - do?",
                "options": ["Switches to the previously checked-out branch", "Deletes the current branch", "Creates an empty repository", "Removes the latest commit"],
                "correct_answer": 0,
                "explanation": "git switch - returns to the previously checked-out branch."
            },
            {
                "question_text": "What does the command git clone create?",
                "options": ["A local copy of a repository", "A new Git programming language", "A new operating system", "A database table"],
                "correct_answer": 0,
                "explanation": "git clone copies a repository and its available history to the local machine."
            },
            {
                "question_text": "What is the purpose of the command git pull origin main?",
                "options": ["Fetches and integrates updates from origin's main branch", "Uploads local changes to main", "Deletes the remote main branch", "Creates a new local repository"],
                "correct_answer": 0,
                "explanation": "git pull fetches from the specified remote branch and integrates the updates into the current branch."
            },
            {
                "question_text": "What does git push origin main mean?",
                "options": ["Pushes the current local main branch to the origin remote", "Downloads the remote main branch", "Deletes the origin remote", "Creates a new GitHub account"],
                "correct_answer": 0,
                "explanation": "The command pushes local main branch commits to the origin remote."
            },
            {
                "question_text": "Which command renames a configured remote from origin to upstream?",
                "options": ["git remote rename origin upstream", "git branch rename origin upstream", "git remote change origin upstream", "git config rename origin upstream"],
                "correct_answer": 0,
                "explanation": "git remote rename changes the name of an existing remote."
            },
            {
                "question_text": "Which command removes a remote named origin from local Git configuration?",
                "options": ["git remote remove origin", "git branch -d origin", "git rm origin", "git delete remote origin"],
                "correct_answer": 0,
                "explanation": "git remote remove deletes the remote configuration entry without deleting the remote repository itself."
            },
            {
                "question_text": "What is the main purpose of a README.md file on GitHub?",
                "options": ["Provide project information and usage instructions", "Store private authentication tokens", "Replace the Git repository", "Automatically fix code errors"],
                "correct_answer": 0,
                "explanation": "GitHub commonly displays README.md to introduce the repository."
            },
            {
                "question_text": "Which file format is commonly used for GitHub README documentation?",
                "options": ["Markdown", "Executable binary", "Database backup", "Audio format"],
                "correct_answer": 0,
                "explanation": "Markdown files use readable text formatting and are commonly used for project documentation."
            },
            {
                "question_text": "What does the # symbol represent in a basic Markdown heading?",
                "options": ["A heading marker", "A code execution command", "A Git branch name", "A file deletion instruction"],
                "correct_answer": 0,
                "explanation": "Markdown uses one or more # characters to represent heading levels."
            },
            {
                "question_text": "Which GitHub feature is commonly used to explain how people can contribute to a project?",
                "options": ["CONTRIBUTING.md", "package-lock.json", "favicon.ico", "desktop.ini"],
                "correct_answer": 0,
                "explanation": "CONTRIBUTING.md documents contribution guidelines and project workflows."
            },
            {
                "question_text": "What is the purpose of a LICENSE file in a repository?",
                "options": ["Describe the permissions and conditions for using the project", "List all Git branches", "Store user passwords", "Record computer hardware details"],
                "correct_answer": 0,
                "explanation": "A license explains the legal terms under which others may use and distribute project code."
            },
            {
                "question_text": "What does a public GitHub repository allow?",
                "options": ["Anyone can view its contents", "Only its owner can view it", "Nobody can clone it", "It cannot contain source code"],
                "correct_answer": 0,
                "explanation": "Public repositories are visible to anyone, subject to GitHub access and service rules."
            },
            {
                "question_text": "What does a private GitHub repository mean?",
                "options": ["Access is restricted to authorized users", "Every internet user can edit it", "It has no commit history", "It cannot contain branches"],
                "correct_answer": 0,
                "explanation": "Private repositories restrict visibility and access to permitted users."
            },
            {
                "question_text": "What is the purpose of a GitHub organization?",
                "options": ["Manage repositories and collaborate as a group", "Replace the Git command-line tool", "Automatically write application code", "Store only personal photographs"],
                "correct_answer": 0,
                "explanation": "Organizations provide shared repository and team management."
            },
            {
                "question_text": "What is a collaborator on a GitHub repository?",
                "options": ["A person granted access to work on the repository", "A Git command", "A commit identifier", "A type of file extension"],
                "correct_answer": 0,
                "explanation": "A collaborator is a person who has been granted repository access."
            },
            {
                "question_text": "What is the purpose of GitHub notifications?",
                "options": ["Inform users about relevant repository activity", "Automatically modify source code", "Delete old commits", "Create local branches"],
                "correct_answer": 0,
                "explanation": "Notifications alert users to activity such as mentions, issues, and pull request updates."
            },
            {
                "question_text": "What does starring a GitHub repository do?",
                "options": ["Marks it as a repository of interest", "Gives the user administrator access", "Automatically forks it", "Deletes its issues"],
                "correct_answer": 0,
                "explanation": "A star is a way to bookmark or show interest in a repository."
            },
            {
                "question_text": "What is the purpose of watching a GitHub repository?",
                "options": ["Receive notifications about selected repository activity", "Automatically merge all pull requests", "Change the repository owner", "Make a private repository public"],
                "correct_answer": 0,
                "explanation": "Watching lets users receive notifications about repository discussions and activity."
            },
            {
                "question_text": "Which command unstages a file while keeping its working-tree changes?",
                "options": ["git restore --staged filename", "git rm filename", "git clean filename", "git reset --hard"],
                "correct_answer": 0,
                "explanation": "git restore --staged removes the file from the staging area while preserving its working-tree modifications."
            },
            {
                "question_text": "Which command discards unstaged changes in a tracked file?",
                "options": ["git restore filename", "git add filename", "git push filename", "git tag filename"],
                "correct_answer": 0,
                "explanation": "git restore filename restores the working-tree file from the index by default, discarding its unstaged changes."
            },
            {
                "question_text": "What does git reset --soft HEAD~1 do?",
                "options": ["Moves HEAD back one commit while keeping changes staged", "Deletes every repository file", "Pushes the previous commit", "Removes all remote branches"],
                "correct_answer": 0,
                "explanation": "A soft reset moves the branch reference but keeps the changes in the staging area."
            },
            {
                "question_text": "What does git reset --hard HEAD do?",
                "options": ["Resets the index and working tree to the current commit", "Creates a new commit", "Uploads all files", "Creates a remote branch"],
                "correct_answer": 0,
                "explanation": "A hard reset makes the index and working tree match HEAD and can discard local changes."
            },
            {
                "question_text": "What is the purpose of git stash?",
                "options": ["Temporarily saves local changes for later use", "Permanently deletes the repository", "Creates a GitHub pull request", "Changes the repository license"],
                "correct_answer": 0,
                "explanation": "git stash saves local modifications so the working directory can be cleaned temporarily."
            },
            {
                "question_text": "Which command reapplies the most recent stash and removes it from the stash list if successful?",
                "options": ["git stash pop", "git stash list", "git stash clear", "git stash show"],
                "correct_answer": 0,
                "explanation": "git stash pop reapplies the latest stash and drops that stash entry when successful."
            },
            {
                "question_text": "Which command lists saved Git stashes?",
                "options": ["git stash list", "git stash show-all-files", "git branch --stash", "git log --stash-only"],
                "correct_answer": 0,
                "explanation": "git stash list displays the saved stash entries."
            },
            {
                "question_text": "What does git clean -n do?",
                "options": ["Shows which untracked files would be removed without deleting them", "Deletes all tracked files", "Creates a clean commit", "Removes all remote branches"],
                "correct_answer": 0,
                "explanation": "The -n option performs a dry run and previews the files that git clean would remove."
            },
            {
                "question_text": "Which command displays the names of files changed in a commit?",
                "options": ["git show --name-only", "git init --files", "git remote --names", "git clean --tracked"],
                "correct_answer": 0,
                "explanation": "git show --name-only displays the files affected by the selected commit."
            },
            {
                "question_text": "What is the purpose of the command git blame filename?",
                "options": ["Shows who last modified each line and the related commit", "Deletes lines written by other developers", "Checks whether a file contains malware", "Creates a new file"],
                "correct_answer": 0,
                "explanation": "git blame annotates lines with information about the commits that last changed them."
            },
            {
                "question_text": "Which command searches for a text pattern in tracked files?",
                "options": ["git grep pattern", "git search-remote pattern", "git find-branch pattern", "git log-pattern"],
                "correct_answer": 0,
                "explanation": "git grep searches tracked files for matching text patterns."
            },
            {
                "question_text": "What is the purpose of the command git diff --name-only?",
                "options": ["Lists names of files with differences", "Displays all commit messages", "Lists all GitHub users", "Deletes changed files"],
                "correct_answer": 0,
                "explanation": "The --name-only option prints only the names of changed files."
            },
            {
                "question_text": "What is a remote-tracking branch?",
                "options": ["A local reference that records the state of a branch on a remote", "A branch stored only in a text editor", "A branch that cannot be updated", "A GitHub issue label"],
                "correct_answer": 0,
                "explanation": "Remote-tracking branches represent the last known state of branches on a remote repository."
            },
            {
                "question_text": "What does the command git fetch origin do?",
                "options": ["Downloads updates from the origin remote without merging them into the current branch", "Deletes the origin repository", "Commits all local files", "Creates a new GitHub account"],
                "correct_answer": 0,
                "explanation": "git fetch origin downloads objects and updates remote-tracking references."
            },
            {
                "question_text": "What is the purpose of a pull request review?",
                "options": ["Evaluate proposed code changes and provide feedback", "Change the Git installation directory", "Automatically erase commit history", "Create a new programming language"],
                "correct_answer": 0,
                "explanation": "Reviews help maintain code quality by allowing others to inspect proposed changes."
            },
            {
                "question_text": "What does closing a GitHub issue indicate?",
                "options": ["The issue is considered resolved or no longer needs to remain open", "The entire repository is deleted", "The GitHub account is suspended", "All branches are merged automatically"],
                "correct_answer": 0,
                "explanation": "Closing an issue marks the discussion or tracked task as no longer open."
            },
            {
                "question_text": "Why should developers review files before committing them?",
                "options": ["To ensure only intended changes are included", "To increase the repository size", "To remove all commit messages", "To disable version control"],
                "correct_answer": 0,
                "explanation": "Reviewing staged changes helps prevent accidental files or unrelated edits from entering a commit."
            }
        ]
    }
]

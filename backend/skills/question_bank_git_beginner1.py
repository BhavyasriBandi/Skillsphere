
QUESTION_BANK_GIT_BEGINNER1 = [
    {
        "skill": "Git & GitHub",
        "difficulty": "beginner",
        "questions": [
            {
                "question_text": "What is Git?",
                "options": ["A distributed version control system", "A programming language", "A database", "A web browser"],
                "correct_answer": 0,
                "explanation": "Git is a distributed version control system used to track changes in files."
            },
            {
                "question_text": "What is GitHub?",
                "options": ["A cloud-based platform for hosting and collaborating on Git repositories", "A programming language", "A database engine", "An operating system"],
                "correct_answer": 0,
                "explanation": "GitHub hosts Git repositories and provides collaboration features."
            },
            {
                "question_text": "Who created Git?",
                "options": ["Linus Torvalds", "James Gosling", "Guido van Rossum", "Brendan Eich"],
                "correct_answer": 0,
                "explanation": "Linus Torvalds created Git in 2005."
            },
            {
                "question_text": "What is a Git repository?",
                "options": ["A location where project files and their version history are stored", "A programming language compiler", "A web server", "A spreadsheet"],
                "correct_answer": 0,
                "explanation": "A Git repository contains project files and version-control metadata."
            },
            {
                "question_text": "Which command initializes a new Git repository?",
                "options": ["git init", "git start", "git create", "git new"],
                "correct_answer": 0,
                "explanation": "git init creates a new Git repository in the current directory."
            },
            {
                "question_text": "Which command displays the current working tree status?",
                "options": ["git status", "git showall", "git check", "git state"],
                "correct_answer": 0,
                "explanation": "git status displays staged, unstaged, and untracked changes."
            },
            {
                "question_text": "Which command stages a specific file?",
                "options": ["git add filename", "git commit filename", "git push filename", "git save filename"],
                "correct_answer": 0,
                "explanation": "git add stages the specified file for the next commit."
            },
            {
                "question_text": "Which command stages all changes in the current directory?",
                "options": ["git add .", "git commit .", "git push .", "git init ."],
                "correct_answer": 0,
                "explanation": "git add . stages changes under the current directory."
            },
            {
                "question_text": "Which command records staged changes in the repository history?",
                "options": ["git commit", "git add", "git status", "git clone"],
                "correct_answer": 0,
                "explanation": "git commit creates a new commit from staged changes."
            },
            {
                "question_text": "Which command adds a message to a Git commit?",
                "options": ["git commit -m \"message\"", "git add -m \"message\"", "git push -m \"message\"", "git status -m \"message\""],
                "correct_answer": 0,
                "explanation": "The -m option supplies a commit message directly."
            },
            {
                "question_text": "Which command displays the commit history?",
                "options": ["git log", "git history", "git commits", "git records"],
                "correct_answer": 0,
                "explanation": "git log displays the repository's commit history."
            },
            {
                "question_text": "What is a commit in Git?",
                "options": ["A recorded snapshot of staged repository changes", "A remote hosting website", "A folder used for images", "A programming language"],
                "correct_answer": 0,
                "explanation": "A commit records a snapshot of the repository at a particular point in history."
            },
            {
                "question_text": "What is a branch in Git?",
                "options": ["An independent line of development", "A deleted repository", "A text editor", "A database connection"],
                "correct_answer": 0,
                "explanation": "A branch provides a separate line of development within a repository."
            },
            {
                "question_text": "Which command lists local Git branches?",
                "options": ["git branch", "git list", "git show-branches", "git status -b"],
                "correct_answer": 0,
                "explanation": "git branch lists local branches by default."
            },
            {
                "question_text": "Which command creates a branch named feature-login?",
                "options": ["git branch feature-login", "git create feature-login", "git init feature-login", "git add feature-login"],
                "correct_answer": 0,
                "explanation": "git branch followed by a name creates a new branch."
            },
            {
                "question_text": "Which command switches to an existing branch?",
                "options": ["git switch branch-name", "git branch branch-name", "git init branch-name", "git commit branch-name"],
                "correct_answer": 0,
                "explanation": "git switch changes the currently checked-out branch."
            },
            {
                "question_text": "Which command creates and switches to a new branch?",
                "options": ["git switch -c feature", "git switch feature", "git add feature", "git merge feature"],
                "correct_answer": 0,
                "explanation": "git switch -c creates a branch and switches to it."
            },
            {
                "question_text": "What is the default branch commonly named in newly created GitHub repositories?",
                "options": ["main", "master-only", "root", "default-branch"],
                "correct_answer": 0,
                "explanation": "GitHub commonly uses main as the default branch name."
            },
            {
                "question_text": "What does merging branches mean?",
                "options": ["Combining changes from one branch into another", "Deleting the entire repository", "Uploading a file to email", "Creating a new Git account"],
                "correct_answer": 0,
                "explanation": "Merging integrates changes from one branch into the currently checked-out branch."
            },
            {
                "question_text": "Which command merges another branch into the current branch?",
                "options": ["git merge branch-name", "git join branch-name", "git add branch-name", "git push branch-name"],
                "correct_answer": 0,
                "explanation": "git merge integrates the specified branch into the current branch."
            },
            {
                "question_text": "What is a merge conflict?",
                "options": ["A situation where Git cannot automatically combine changes", "A successful commit", "A GitHub login error only", "A new repository"],
                "correct_answer": 0,
                "explanation": "A merge conflict occurs when Git needs help deciding how overlapping changes should be combined."
            },
            {
                "question_text": "Which command downloads a remote repository as a local copy?",
                "options": ["git clone", "git copy", "git download", "git init"],
                "correct_answer": 0,
                "explanation": "git clone creates a local copy of a remote repository."
            },
            {
                "question_text": "Which command downloads updates from a remote repository and integrates them into the current branch?",
                "options": ["git pull", "git push", "git init", "git commit"],
                "correct_answer": 0,
                "explanation": "git pull fetches remote updates and integrates them into the current branch."
            },
            {
                "question_text": "Which command uploads local commits to a remote repository?",
                "options": ["git push", "git pull", "git fetch", "git status"],
                "correct_answer": 0,
                "explanation": "git push sends local commits to a remote repository."
            },
            {
                "question_text": "Which command downloads remote changes without integrating them into the current branch?",
                "options": ["git fetch", "git pull", "git push", "git merge"],
                "correct_answer": 0,
                "explanation": "git fetch downloads remote references and objects without merging them into the current branch."
            },
            {
                "question_text": "What is a remote repository?",
                "options": ["A repository hosted elsewhere and accessed over a network", "A file stored only in RAM", "A local text editor", "A Git commit message"],
                "correct_answer": 0,
                "explanation": "A remote repository is another repository that can be accessed over a network."
            },
            {
                "question_text": "Which command lists configured remote repositories?",
                "options": ["git remote -v", "git branch -v", "git log -v", "git status -r"],
                "correct_answer": 0,
                "explanation": "git remote -v displays remote names and their fetch and push URLs."
            },
            {
                "question_text": "What is the commonly used name for the primary remote repository?",
                "options": ["origin", "main", "master", "source-code"],
                "correct_answer": 0,
                "explanation": "origin is the conventional default name for the remote created by git clone."
            },
            {
                "question_text": "Which command adds a remote named origin?",
                "options": ["git remote add origin URL", "git add remote URL", "git init origin URL", "git branch origin URL"],
                "correct_answer": 0,
                "explanation": "git remote add configures a remote name and its repository URL."
            },
            {
                "question_text": "What is a README file commonly used for?",
                "options": ["Explain the project and how to use it", "Store Git passwords", "Replace all source code", "Run database migrations"],
                "correct_answer": 0,
                "explanation": "A README introduces a project and commonly documents setup and usage instructions."
            },
            {
                "question_text": "What is a .gitignore file used for?",
                "options": ["Specify intentionally untracked files that Git should ignore", "Delete all Git commits", "Store remote repository URLs", "Create a new branch"],
                "correct_answer": 0,
                "explanation": ".gitignore contains patterns for files and directories Git should ignore when they are untracked."
            },
            {
                "question_text": "Which file is commonly ignored in a Python project because it contains generated bytecode?",
                "options": ["__pycache__/", "README.md", "manage.py", "requirements.txt"],
                "correct_answer": 0,
                "explanation": "__pycache__ contains generated Python bytecode files and is commonly excluded from version control."
            },
            {
                "question_text": "Should passwords and API secret keys normally be committed to a public Git repository?",
                "options": ["No, they should be kept in secure configuration or secret storage", "Yes, every developer needs them publicly", "Only in README files", "Only in commit messages"],
                "correct_answer": 0,
                "explanation": "Secrets should not be committed because repository history may expose them."
            },
            {
                "question_text": "What is the purpose of GitHub pull requests?",
                "options": ["Propose and review changes before merging them", "Automatically delete all branches", "Install Git on a computer", "Create database tables"],
                "correct_answer": 0,
                "explanation": "Pull requests provide a place to discuss, review, and merge proposed changes."
            },
            {
                "question_text": "What is a GitHub repository?",
                "options": ["A project space that stores files and version history", "A programming language", "A local operating system account", "A web browser extension"],
                "correct_answer": 0,
                "explanation": "A GitHub repository hosts project files and Git version history."
            },
            {
                "question_text": "What is the purpose of forking a GitHub repository?",
                "options": ["Create a personal copy of another user's repository under your account", "Delete the original repository", "Merge every branch automatically", "Install GitHub Desktop"],
                "correct_answer": 0,
                "explanation": "A fork is a separate copy of a repository under another account or organization."
            },
            {
                "question_text": "What is a GitHub issue commonly used for?",
                "options": ["Track bugs, tasks, and feature requests", "Store compiled Python bytecode", "Replace Git commits", "Configure a computer's keyboard"],
                "correct_answer": 0,
                "explanation": "Issues help teams track and discuss work related to a repository."
            },
            {
                "question_text": "What is a Git tag commonly used for?",
                "options": ["Mark a specific point in repository history, often a release", "Ignore all source files", "Create a new GitHub account", "Delete remote branches"],
                "correct_answer": 0,
                "explanation": "Tags identify specific commits and are often used to mark software releases."
            },
            {
                "question_text": "Which command creates a lightweight Git tag named v1.0?",
                "options": ["git tag v1.0", "git branch v1.0", "git commit v1.0", "git remote v1.0"],
                "correct_answer": 0,
                "explanation": "git tag followed by a name creates a lightweight tag at the current commit."
            },
            {
                "question_text": "Which command displays differences in unstaged working-tree changes?",
                "options": ["git diff", "git log", "git remote", "git tag"],
                "correct_answer": 0,
                "explanation": "git diff shows changes that have not yet been staged."
            },
            {
                "question_text": "Which command displays changes staged for the next commit?",
                "options": ["git diff --staged", "git status --remote", "git log --staged", "git branch --staged"],
                "correct_answer": 0,
                "explanation": "git diff --staged compares the staging area with the latest commit."
            },
            {
                "question_text": "What does HEAD usually represent in Git?",
                "options": ["The currently checked-out commit or branch reference", "The first file in a repository", "The remote server address", "The GitHub account password"],
                "correct_answer": 0,
                "explanation": "HEAD identifies the current checkout position, usually the tip of the current branch."
            },
            {
                "question_text": "Which command displays the current branch name?",
                "options": ["git branch --show-current", "git remote -v", "git diff --name-only", "git tag --list"],
                "correct_answer": 0,
                "explanation": "git branch --show-current prints the current branch name."
            },
            {
                "question_text": "What is the staging area in Git?",
                "options": ["An area where selected changes are prepared for a commit", "A remote hosting website", "A backup of the operating system", "A list of GitHub users"],
                "correct_answer": 0,
                "explanation": "The staging area holds changes selected for the next commit."
            },
            {
                "question_text": "What is an untracked file in Git?",
                "options": ["A file Git is not currently tracking", "A file already committed", "A file stored in every remote branch", "A deleted commit"],
                "correct_answer": 0,
                "explanation": "An untracked file is present in the working directory but has not been added to Git's tracking."
            },
            {
                "question_text": "Which command removes a tracked file from the working tree and stages its deletion?",
                "options": ["git rm filename", "git delete filename", "git remove-only filename", "git clean filename"],
                "correct_answer": 0,
                "explanation": "git rm removes the file and stages the deletion."
            },
            {
                "question_text": "Which command renames a tracked file and stages the change?",
                "options": ["git mv oldname newname", "git rename oldname newname", "git change oldname newname", "git branch oldname newname"],
                "correct_answer": 0,
                "explanation": "git mv moves or renames a file and stages the resulting change."
            },
            {
                "question_text": "What is the purpose of git config?",
                "options": ["Set Git configuration values such as username and email", "Create a remote repository automatically", "Merge all branches", "Delete the Git history"],
                "correct_answer": 0,
                "explanation": "git config manages Git configuration settings."
            },
            {
                "question_text": "Which command sets a global Git username?",
                "options": ["git config --global user.name \"Bhavya\"", "git user set Bhavya", "git config username Bhavya", "git init --user Bhavya"],
                "correct_answer": 0,
                "explanation": "The --global option sets the username for the current user's Git configuration."
            },
            {
                "question_text": "Which command sets a global Git email address?",
                "options": ["git config --global user.email \"name@example.com\"", "git email set name@example.com", "git remote email name@example.com", "git init --email name@example.com"],
                "correct_answer": 0,
                "explanation": "The user.email configuration value sets the email recorded in commits."
            },
            {
                "question_text": "What is GitHub Desktop?",
                "options": ["A graphical application for working with Git repositories", "A programming language", "A database management system", "A web hosting protocol"],
                "correct_answer": 0,
                "explanation": "GitHub Desktop provides a graphical interface for common Git and GitHub workflows."
            },
            {
                "question_text": "What is the main purpose of version control?",
                "options": ["Track changes and support collaboration over time", "Increase computer screen resolution", "Replace the operating system", "Automatically write all project code"],
                "correct_answer": 0,
                "explanation": "Version control records project history and supports coordinated development."
            }
        ]
    }
]

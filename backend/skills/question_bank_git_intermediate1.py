
QUESTION_BANK_GIT_INTERMEDIATE1 = [
    {
        "skill": "Git & GitHub",
        "difficulty": "intermediate",
        "questions": [
            {
                "question_text": "What is the main difference between git merge and git rebase?",
                "options": ["Merge combines histories while rebase reapplies commits onto another base", "Merge deletes commits while rebase deletes branches", "Both always produce identical commit histories", "Rebase only works with remote repositories"],
                "correct_answer": 0,
                "explanation": "Merge integrates histories, while rebase replays commits on top of another base commit."
            },
            {
                "question_text": "Which command rebases the current branch onto main?",
                "options": ["git rebase main", "git merge --rebase main", "git branch main --rebase", "git reset main"],
                "correct_answer": 0,
                "explanation": "git rebase main reapplies the current branch commits on top of main."
            },
            {
                "question_text": "Which command continues a rebase after conflicts have been resolved and staged?",
                "options": ["git rebase --continue", "git rebase --finish", "git merge --continue", "git commit --continue"],
                "correct_answer": 0,
                "explanation": "After resolving and staging conflicts, git rebase --continue resumes the rebase."
            },
            {
                "question_text": "Which command stops an in-progress rebase and restores the original branch state?",
                "options": ["git rebase --abort", "git rebase --skip", "git reset --continue", "git merge --abort"],
                "correct_answer": 0,
                "explanation": "git rebase --abort aborts the rebase and returns to the pre-rebase state."
            },
            {
                "question_text": "What does git rebase --skip do?",
                "options": ["Skips the current commit being replayed", "Skips every branch in the repository", "Deletes the remote repository", "Stages all conflict files"],
                "correct_answer": 0,
                "explanation": "It tells Git to omit the current commit from the rebase operation."
            },
            {
                "question_text": "What is an interactive rebase commonly used for?",
                "options": ["Editing, reordering, squashing, or dropping commits", "Creating remote repositories only", "Changing file permissions only", "Downloading all GitHub issues"],
                "correct_answer": 0,
                "explanation": "Interactive rebase allows developers to modify a sequence of commits."
            },
            {
                "question_text": "Which command starts an interactive rebase for the last four commits?",
                "options": ["git rebase -i HEAD~4", "git merge -i HEAD~4", "git commit -i HEAD~4", "git reset -i HEAD~4"],
                "correct_answer": 0,
                "explanation": "The -i option starts interactive rebase for the selected commit range."
            },
            {
                "question_text": "In an interactive rebase, what does the squash command do?",
                "options": ["Combines a commit with the previous commit", "Deletes the entire branch", "Creates a remote tag", "Downloads missing objects"],
                "correct_answer": 0,
                "explanation": "squash combines the selected commit with the preceding commit and allows commit-message editing."
            },
            {
                "question_text": "In an interactive rebase, what does the fixup command do?",
                "options": ["Combines a commit with the previous commit while discarding its message", "Creates a backup branch", "Stops the rebase permanently", "Changes the repository URL"],
                "correct_answer": 0,
                "explanation": "fixup combines changes into the previous commit and discards the fixup commit message."
            },
            {
                "question_text": "What is the purpose of git cherry-pick?",
                "options": ["Apply changes from a specific existing commit onto the current branch", "Merge every remote branch", "Delete selected files permanently", "Create a GitHub fork"],
                "correct_answer": 0,
                "explanation": "Cherry-pick applies the changes introduced by selected commits to the current branch."
            },
            {
                "question_text": "Which command applies commit abc123 to the current branch?",
                "options": ["git cherry-pick abc123", "git merge --commit abc123", "git apply-commit abc123", "git branch abc123"],
                "correct_answer": 0,
                "explanation": "git cherry-pick accepts a commit reference and applies its changes."
            },
            {
                "question_text": "What does git revert HEAD do?",
                "options": ["Creates a new commit that reverses the changes of HEAD", "Deletes HEAD from repository history", "Moves the branch to an older commit without a new commit", "Deletes all untracked files"],
                "correct_answer": 0,
                "explanation": "git revert creates a new commit that undoes the changes introduced by the selected commit."
            },
            {
                "question_text": "How does git revert differ from git reset?",
                "options": ["Revert creates a new undo commit, while reset moves a branch reference", "Reset always creates a new commit, while revert deletes one", "Both permanently delete remote history", "Revert only works on untracked files"],
                "correct_answer": 0,
                "explanation": "Revert preserves history by recording an inverse commit; reset changes the current reference and possibly the index or working tree."
            },
            {
                "question_text": "What is the purpose of git reflog?",
                "options": ["Show recent movements of HEAD and reference updates", "List all GitHub contributors", "Display only remote URLs", "Track operating-system login history"],
                "correct_answer": 0,
                "explanation": "The reflog records local updates to references, helping locate commits after branch movements."
            },
            {
                "question_text": "Which command can help locate a commit after an accidental reset?",
                "options": ["git reflog", "git remote -v", "git clean", "git status --ignored"],
                "correct_answer": 0,
                "explanation": "The reflog can reveal earlier HEAD positions and commit identifiers."
            },
            {
                "question_text": "What does git reset --mixed HEAD~1 do?",
                "options": ["Moves HEAD back one commit and unstages the changes while keeping them in the working tree", "Deletes all working-tree files", "Keeps changes staged and moves HEAD back", "Creates a revert commit"],
                "correct_answer": 0,
                "explanation": "Mixed reset updates HEAD and the index, leaving the changes in the working tree."
            },
            {
                "question_text": "What does git reset --soft HEAD~1 preserve?",
                "options": ["Changes in both the staging area and working tree", "Only remote-tracking branches", "No local changes", "Only ignored files"],
                "correct_answer": 0,
                "explanation": "Soft reset moves HEAD but leaves the index and working tree unchanged."
            },
            {
                "question_text": "What is the primary purpose of git bisect?",
                "options": ["Find the commit that introduced a bug using binary search", "Merge two remote repositories", "Compress repository objects", "Rename every branch"],
                "correct_answer": 0,
                "explanation": "git bisect tests commits through a binary-search process to identify a problematic change."
            },
            {
                "question_text": "Which command starts a bisect session?",
                "options": ["git bisect start", "git bug start", "git search start", "git log --bisect-start"],
                "correct_answer": 0,
                "explanation": "git bisect start begins a binary-search debugging session."
            },
            {
                "question_text": "Which command marks the current commit as containing the bug during git bisect?",
                "options": ["git bisect bad", "git bisect broken", "git bisect fail", "git bisect error"],
                "correct_answer": 0,
                "explanation": "git bisect bad marks the current commit as a bad revision."
            },
            {
                "question_text": "Which command marks a tested commit as working during git bisect?",
                "options": ["git bisect good", "git bisect pass", "git bisect clean", "git bisect safe"],
                "correct_answer": 0,
                "explanation": "git bisect good marks a revision as one where the bug is absent."
            },
            {
                "question_text": "Which command ends a bisect session?",
                "options": ["git bisect reset", "git bisect stop-all", "git bisect clear-history", "git bisect finish"],
                "correct_answer": 0,
                "explanation": "git bisect reset ends the session and returns to the original branch or state."
            },
            {
                "question_text": "What is a fast-forward merge?",
                "options": ["Moving the current branch pointer forward when no divergent history exists", "Creating a merge commit for every merge", "Rewriting all remote commits", "Deleting the source branch before merging"],
                "correct_answer": 0,
                "explanation": "A fast-forward merge advances the branch pointer without creating a merge commit."
            },
            {
                "question_text": "Which command forces Git to create a merge commit even when a fast-forward is possible?",
                "options": ["git merge --no-ff branch-name", "git merge --fast branch-name", "git rebase --no-ff branch-name", "git commit --merge branch-name"],
                "correct_answer": 0,
                "explanation": "The --no-ff option creates a merge commit rather than advancing the pointer directly."
            },
            {
                "question_text": "What does git merge --abort do?",
                "options": ["Attempts to return to the state before the current merge", "Deletes the target branch", "Completes all unresolved conflicts automatically", "Pushes the merge to origin"],
                "correct_answer": 0,
                "explanation": "git merge --abort cancels an in-progress merge and restores the pre-merge state when possible."
            },
            {
                "question_text": "What is the purpose of git worktree?",
                "options": ["Manage multiple working trees attached to one repository", "Create a new GitHub organization", "Store only binary files", "Replace the staging area"],
                "correct_answer": 0,
                "explanation": "Git worktree allows multiple branches to be checked out into separate working directories."
            },
            {
                "question_text": "Which command adds a separate working directory for branch feature-x?",
                "options": ["git worktree add ../feature-x feature-x", "git branch --worktree feature-x", "git clone --worktree feature-x", "git checkout --directory feature-x"],
                "correct_answer": 0,
                "explanation": "git worktree add creates an additional working tree at the specified path."
            },
            {
                "question_text": "What is a detached HEAD state?",
                "options": ["HEAD points directly to a commit instead of a branch reference", "The repository has no commits", "All remote branches are deleted", "The staging area is disconnected from Git"],
                "correct_answer": 0,
                "explanation": "In detached HEAD state, HEAD references a commit directly rather than the tip of a branch."
            },
            {
                "question_text": "What is the safest way to preserve new commits made in detached HEAD state?",
                "options": ["Create a branch pointing to the current commit", "Run git clean -fd", "Delete the .git directory", "Run git remote remove origin"],
                "correct_answer": 0,
                "explanation": "Creating a branch preserves a named reference to the new commits."
            },
            {
                "question_text": "What does git tag -a v2.0 -m \"Release 2.0\" create?",
                "options": ["An annotated tag with a message", "A new branch named v2.0", "A merge commit", "A remote repository"],
                "correct_answer": 0,
                "explanation": "The -a option creates an annotated tag, and -m supplies its message."
            },
            {
                "question_text": "Which command lists tags in a Git repository?",
                "options": ["git tag --list", "git branch --tags-only", "git remote --tags", "git log --tag-list"],
                "correct_answer": 0,
                "explanation": "git tag --list displays available tags."
            },
            {
                "question_text": "Which command pushes a specific tag named v2.0 to origin?",
                "options": ["git push origin v2.0", "git tag push v2.0", "git push --branch v2.0", "git remote add v2.0"],
                "correct_answer": 0,
                "explanation": "git push origin v2.0 pushes the named tag to the origin remote."
            },
            {
                "question_text": "What does git push --tags do?",
                "options": ["Pushes local tags that are not already present on the remote", "Pushes only the current branch", "Deletes remote tags", "Downloads all remote tags"],
                "correct_answer": 0,
                "explanation": "The --tags option pushes all local tags that are not already present on the remote."
            },
            {
                "question_text": "What is the purpose of git archive?",
                "options": ["Create an archive of selected repository files", "Delete old commits", "List remote branches", "Start an interactive rebase"],
                "correct_answer": 0,
                "explanation": "git archive creates an archive file from a tree or commit."
            },
            {
                "question_text": "What does git ls-files display?",
                "options": ["Files tracked in the index", "All files on a remote server", "Every GitHub issue", "Only deleted files"],
                "correct_answer": 0,
                "explanation": "git ls-files lists files known to the Git index."
            },
            {
                "question_text": "What is the purpose of git cat-file?",
                "options": ["Inspect the contents or type of Git objects", "Display repository collaborators", "Create a new branch", "Upload files to GitHub"],
                "correct_answer": 0,
                "explanation": "git cat-file provides information about objects stored in Git's object database."
            },
            {
                "question_text": "What does git rev-parse HEAD return?",
                "options": ["The object ID of the commit referenced by HEAD", "The current remote URL", "The list of staged files", "The number of branches"],
                "correct_answer": 0,
                "explanation": "git rev-parse resolves HEAD to its commit object ID."
            },
            {
                "question_text": "What is the purpose of git show-ref?",
                "options": ["List references available in the repository", "Show only changed source-code lines", "Display GitHub pull request reviews", "Remove remote-tracking branches"],
                "correct_answer": 0,
                "explanation": "git show-ref lists references such as branches and tags with their object IDs."
            },
            {
                "question_text": "What does git remote prune origin remove?",
                "options": ["Stale remote-tracking references that no longer exist on origin", "All local branches", "All local commits", "The origin repository itself"],
                "correct_answer": 0,
                "explanation": "Pruning removes obsolete remote-tracking references after branches have been deleted on the remote."
            },
            {
                "question_text": "Which command removes stale remote-tracking branches from origin?",
                "options": ["git fetch --prune origin", "git push --delete origin", "git branch --remove-all", "git reset --prune"],
                "correct_answer": 0,
                "explanation": "git fetch --prune updates remote references and removes stale tracking references."
            },
            {
                "question_text": "What is the purpose of git clean -fd?",
                "options": ["Remove untracked files and directories", "Remove all tracked files from the repository history", "Delete every branch", "Undo the last commit"],
                "correct_answer": 0,
                "explanation": "The -f option forces cleaning and -d includes untracked directories; preview first when unsure."
            },
            {
                "question_text": "What does the -u option in git stash -u include?",
                "options": ["Untracked files in the stash", "All remote branches", "User configuration files only", "Unreachable commits"],
                "correct_answer": 0,
                "explanation": "The -u option includes untracked files when creating a stash."
            },
            {
                "question_text": "What is the difference between git stash apply and git stash pop?",
                "options": ["Apply keeps the stash entry, while pop removes it after successful application", "Apply deletes the stash, while pop keeps it", "Both always delete all stash entries", "Pop creates a new branch"],
                "correct_answer": 0,
                "explanation": "git stash apply reapplies without dropping the entry; pop applies and then drops it if successful."
            },
            {
                "question_text": "What does git diff main...feature compare?",
                "options": ["The changes on feature since its merge base with main", "Only the latest commit messages on both branches", "All files in the working directory against the remote", "The two branch names alphabetically"],
                "correct_answer": 0,
                "explanation": "The three-dot diff compares the merge base of the branches with the feature side."
            },
            {
                "question_text": "What does git diff main..feature compare?",
                "options": ["The tips of main and feature", "Only their common ancestor", "The local repository with GitHub settings", "Only staged changes"],
                "correct_answer": 0,
                "explanation": "For git diff, two-dot notation compares the two endpoint trees."
            },
            {
                "question_text": "What is the purpose of a Git submodule?",
                "options": ["Include another Git repository at a specific path in a parent repository", "Combine every repository into one commit", "Automatically install all programming languages", "Replace Git branches with folders"],
                "correct_answer": 0,
                "explanation": "A submodule records a reference to a specific commit of another repository."
            },
            {
                "question_text": "Which command initializes and updates configured submodules recursively?",
                "options": ["git submodule update --init --recursive", "git clone --all-submodules-only", "git branch --submodule", "git remote update --submodule"],
                "correct_answer": 0,
                "explanation": "This command initializes submodules and checks out their recorded commits, including nested submodules."
            },
            {
                "question_text": "What is a Git hook?",
                "options": ["A script that Git runs at certain points in its workflow", "A remote repository URL", "A special type of branch", "A GitHub star"],
                "correct_answer": 0,
                "explanation": "Hooks are scripts triggered by events such as committing or receiving pushes."
            },
            {
                "question_text": "Which Git hook runs before a commit is created?",
                "options": ["pre-commit", "post-commit", "post-receive", "pre-push"],
                "correct_answer": 0,
                "explanation": "The pre-commit hook runs before Git creates the commit."
            },
            {
                "question_text": "What is the purpose of the pre-push Git hook?",
                "options": ["Run checks before Git sends commits to a remote", "Run after every file is opened", "Automatically create GitHub issues", "Delete local commit messages"],
                "correct_answer": 0,
                "explanation": "The pre-push hook can run validation before a push proceeds."
            }
        ]
    }
]


QUESTION_BANK_GIT_ADVANCED1 = [
    {
        "skill": "Git & GitHub",
        "difficulty": "advanced",
        "questions": [
            {
                "question_text": "Which Git object stores the contents of a file?",
                "options": ["Blob", "Tree", "Commit", "Tag"],
                "correct_answer": 0,
                "explanation": "A blob stores file contents without storing the filename or directory structure."
            },
            {
                "question_text": "Which Git object represents a directory structure?",
                "options": ["Tree", "Blob", "Commit", "Ref"],
                "correct_answer": 0,
                "explanation": "A tree object records directory entries, including names, modes, and object IDs."
            },
            {
                "question_text": "What information does a Git commit object contain?",
                "options": ["A tree reference, parent references, author, committer, and message", "Only the changed file contents", "Only branch names", "Only remote URLs"],
                "correct_answer": 0,
                "explanation": "A commit object identifies a tree, its parent commit or commits, metadata, and a message."
            },
            {
                "question_text": "Which Git command writes a blob object without creating a commit?",
                "options": ["git hash-object -w filename", "git commit-object filename", "git tree-write filename", "git save-blob filename"],
                "correct_answer": 0,
                "explanation": "git hash-object -w writes the file contents as a blob object into the object database."
            },
            {
                "question_text": "What does git write-tree create?",
                "options": ["A tree object representing the current index", "A new branch", "A commit message", "A remote-tracking reference"],
                "correct_answer": 0,
                "explanation": "git write-tree creates a tree object from the current index."
            },
            {
                "question_text": "Which command creates a commit object directly from a tree and parent information?",
                "options": ["git commit-tree", "git write-tree", "git hash-object", "git update-ref"],
                "correct_answer": 0,
                "explanation": "git commit-tree creates a commit object using a tree and optional parent commits."
            },
            {
                "question_text": "What is the purpose of git fsck?",
                "options": ["Verify the connectivity and validity of objects in the repository", "Format all source files", "Synchronize every remote branch", "Create a GitHub release"],
                "correct_answer": 0,
                "explanation": "git fsck checks the object database for integrity and connectivity problems."
            },
            {
                "question_text": "What does git gc primarily do?",
                "options": ["Perform repository housekeeping and optimize storage", "Delete all branches", "Generate source-code documentation", "Change remote authentication"],
                "correct_answer": 0,
                "explanation": "git gc performs maintenance such as packing objects and pruning eligible unreachable objects."
            },
            {
                "question_text": "What is a Git packfile?",
                "options": ["A compressed collection of Git objects", "A list of GitHub users", "A branch protection configuration", "A collection of untracked files only"],
                "correct_answer": 0,
                "explanation": "Packfiles store multiple Git objects efficiently, often using compression and delta encoding."
            },
            {
                "question_text": "What is the purpose of git repack?",
                "options": ["Reorganize repository objects into packfiles", "Recreate deleted GitHub accounts", "Rename all local branches", "Reset every commit message"],
                "correct_answer": 0,
                "explanation": "git repack repacks objects into new packfiles to improve storage efficiency."
            },
            {
                "question_text": "What does git count-objects -v provide?",
                "options": ["Statistics about loose objects and packed storage", "The number of GitHub contributors", "The count of open pull requests", "The number of source-code lines"],
                "correct_answer": 0,
                "explanation": "The command reports object-storage statistics, including loose objects and pack information."
            },
            {
                "question_text": "What is a dangling Git object?",
                "options": ["An object that is not reachable from a reference or another reachable object", "A file currently staged for a commit", "A remote branch with an upstream", "A commit signed by a developer"],
                "correct_answer": 0,
                "explanation": "A dangling object is not reachable from the repository's references or other reachable objects."
            },
            {
                "question_text": "What does git prune remove?",
                "options": ["Eligible unreachable loose objects", "All tracked source files", "Every local branch", "All annotated tags"],
                "correct_answer": 0,
                "explanation": "git prune removes unreachable loose objects that are eligible for pruning."
            },
            {
                "question_text": "What is the purpose of git replace?",
                "options": ["Create replacement references that make Git substitute one object for another", "Replace every remote URL", "Rename all commits permanently", "Convert a Git repository into SVN"],
                "correct_answer": 0,
                "explanation": "Replacement references allow Git commands to treat one object as a replacement for another."
            },
            {
                "question_text": "What does git notes add to a commit?",
                "options": ["Additional metadata without changing the commit object itself", "A new parent commit", "A new file in the working tree", "A new remote branch"],
                "correct_answer": 0,
                "explanation": "Git notes attach additional information to objects without modifying those objects."
            },
            {
                "question_text": "Which command adds a note to the current commit?",
                "options": ["git notes add -m \"Review completed\"", "git commit --note \"Review completed\"", "git tag --note \"Review completed\"", "git branch --note \"Review completed\""],
                "correct_answer": 0,
                "explanation": "git notes add attaches a note to an object, defaulting to HEAD when no object is specified."
            },
            {
                "question_text": "What is the purpose of git filter-repo?",
                "options": ["Rewrite repository history to filter or transform files and commits", "Run unit tests on every branch", "Automatically merge pull requests", "Create repository backups only"],
                "correct_answer": 0,
                "explanation": "git filter-repo is a tool for rewriting repository history, such as removing sensitive files or changing paths."
            },
            {
                "question_text": "Why should history rewriting be coordinated when working on a shared repository?",
                "options": ["It can change commit IDs and disrupt collaborators' existing history", "It always deletes the GitHub organization", "It prevents all future commits", "It changes source-code file extensions"],
                "correct_answer": 0,
                "explanation": "Rewritten commits have different identities, so collaborators may need to resynchronize their local branches."
            },
            {
                "question_text": "What is the main purpose of git bundle?",
                "options": ["Package Git objects and references into a file for transfer", "Bundle Python dependencies", "Create a GitHub team", "Compress only working-tree files"],
                "correct_answer": 0,
                "explanation": "git bundle creates a portable file containing repository data and references."
            },
            {
                "question_text": "Which command creates a bundle containing all references?",
                "options": ["git bundle create backup.bundle --all", "git archive create backup.bundle --all", "git pack create backup.bundle --all", "git clone create backup.bundle --all"],
                "correct_answer": 0,
                "explanation": "git bundle create can package references and their reachable objects into a transferable bundle."
            },
            {
                "question_text": "What is the purpose of git worktree lock?",
                "options": ["Prevent a linked working tree from being pruned automatically", "Lock every branch against commits", "Prevent users from reading repository files", "Disable remote pushes"],
                "correct_answer": 0,
                "explanation": "Locking a worktree protects it from automatic pruning, often when it is stored on removable media."
            },
            {
                "question_text": "What does git worktree prune remove?",
                "options": ["Administrative information for worktrees that no longer exist", "All active working trees", "Every remote branch", "All repository tags"],
                "correct_answer": 0,
                "explanation": "git worktree prune removes stale administrative data for missing working trees."
            },
            {
                "question_text": "What is the purpose of git sparse-checkout?",
                "options": ["Limit the working tree to selected repository paths", "Compress commits into a smaller history", "Ignore all remote branches", "Delete files outside the current branch"],
                "correct_answer": 0,
                "explanation": "Sparse checkout allows only selected paths from a repository to appear in the working tree."
            },
            {
                "question_text": "Which command initializes sparse-checkout in cone mode?",
                "options": ["git sparse-checkout init --cone", "git checkout --sparse --cone", "git init --sparse-cone", "git config sparse-checkout cone"],
                "correct_answer": 0,
                "explanation": "git sparse-checkout init --cone enables sparse checkout using cone mode."
            },
            {
                "question_text": "What is the purpose of a partial clone?",
                "options": ["Avoid downloading some repository objects until they are needed", "Clone only the README file permanently", "Download commits without branches or references", "Convert a remote repository into a local tag"],
                "correct_answer": 0,
                "explanation": "Partial clone allows Git to defer downloading certain objects, reducing initial transfer size."
            },
            {
                "question_text": "Which option is commonly used to request a blob-filtered partial clone?",
                "options": ["--filter=blob:none", "--skip=all-blobs", "--ignore=blob", "--compress=none"],
                "correct_answer": 0,
                "explanation": "The blob:none filter omits file-content blobs initially and fetches them when needed."
            },
            {
                "question_text": "What does git clone --depth 1 create?",
                "options": ["A shallow clone with a limited commit history", "A clone containing every historical commit", "A repository without a working tree", "A clone with only Git tags"],
                "correct_answer": 0,
                "explanation": "The depth option limits the history fetched, and depth 1 generally fetches only the latest commit history for the selected branch."
            },
            {
                "question_text": "What is a shallow repository?",
                "options": ["A repository whose history is truncated at a specified boundary", "A repository without any tracked files", "A repository with no branches", "A repository containing only tags"],
                "correct_answer": 0,
                "explanation": "A shallow repository has incomplete ancestry because history was limited during cloning or fetching."
            },
            {
                "question_text": "Which command can deepen the history of a shallow repository by 20 commits?",
                "options": ["git fetch --deepen=20", "git pull --history=20", "git clone --expand=20", "git log --deepen=20"],
                "correct_answer": 0,
                "explanation": "git fetch --deepen extends the shallow history by the specified number of commits."
            },
            {
                "question_text": "What does git fetch --unshallow do?",
                "options": ["Convert a shallow repository into a complete repository when the remote provides the required history", "Remove all commits from the repository", "Create a shallow clone from a full repository", "Delete unreachable tags"],
                "correct_answer": 0,
                "explanation": "The --unshallow option fetches the remaining history to remove the shallow boundary when possible."
            },
            {
                "question_text": "What is the purpose of git format-patch?",
                "options": ["Create patch files representing commits for email-based review or application", "Format every source file", "Create a GitHub release", "Generate a repository tree object"],
                "correct_answer": 0,
                "explanation": "git format-patch generates patch files that represent commits and can be shared or applied elsewhere."
            },
            {
                "question_text": "Which command applies a patch generated by git format-patch while preserving commit information?",
                "options": ["git am patch-file.patch", "git apply --commit patch-file.patch", "git merge patch-file.patch", "git cherry-pick patch-file.patch"],
                "correct_answer": 0,
                "explanation": "git am applies mailbox-format patches and creates commits using their metadata."
            },
            {
                "question_text": "What is the difference between git apply and git am?",
                "options": ["git apply applies patch changes, while git am applies mailbox patches and creates commits", "git apply creates branches, while git am deletes them", "Both only download remote objects", "git am can only apply binary images"],
                "correct_answer": 0,
                "explanation": "git apply changes the working tree or index, while git am processes formatted patches as commits."
            },
            {
                "question_text": "What does git apply --check do?",
                "options": ["Check whether a patch can be applied without applying it", "Apply a patch and commit it", "Delete a patch after use", "Create a branch from a patch"],
                "correct_answer": 0,
                "explanation": "The --check option tests whether the patch applies cleanly without modifying files."
            },
            {
                "question_text": "What is the purpose of git rerere?",
                "options": ["Record and reuse previous conflict resolutions", "Automatically revert every merge", "Remove remote references", "Rewrite author information"],
                "correct_answer": 0,
                "explanation": "Reuse Recorded Resolution can remember how conflicts were resolved and reuse those resolutions later."
            },
            {
                "question_text": "Which command enables rerere for the current repository?",
                "options": ["git config rerere.enabled true", "git rerere start --global-only", "git merge --rerere-enable", "git config merge.autoResolve true"],
                "correct_answer": 0,
                "explanation": "Setting rerere.enabled to true enables recording and reuse of conflict resolutions."
            },
            {
                "question_text": "What does git rerere status display?",
                "options": ["Paths with recorded or pending conflict-resolution information", "All repository collaborators", "The current remote branch URL", "Every commit that failed CI"],
                "correct_answer": 0,
                "explanation": "git rerere status reports paths for which rerere has recorded or is tracking conflict information."
            },
            {
                "question_text": "What is the purpose of git merge-tree?",
                "options": ["Perform or inspect a merge calculation without updating the working tree", "Create a permanent merge commit automatically", "Delete a branch's tree objects", "Generate a visual repository diagram"],
                "correct_answer": 0,
                "explanation": "git merge-tree computes merge results without performing a normal working-tree merge."
            },
            {
                "question_text": "What does git range-diff compare?",
                "options": ["Two versions of a commit series", "Two remote repository URLs", "Two .gitignore files only", "The number of branches in two repositories"],
                "correct_answer": 0,
                "explanation": "git range-diff compares two versions of a patch series, helping review changes after rebasing or revising commits."
            },
            {
                "question_text": "What is the purpose of git rev-list?",
                "options": ["List commit objects reachable from specified revisions", "List every file in the working directory", "Display all GitHub issues", "Create remote-tracking branches"],
                "correct_answer": 0,
                "explanation": "git rev-list lists commits reachable from the supplied revision arguments."
            },
            {
                "question_text": "Which command counts commits reachable from HEAD?",
                "options": ["git rev-list --count HEAD", "git branch --count HEAD", "git status --commits HEAD", "git remote --count HEAD"],
                "correct_answer": 0,
                "explanation": "git rev-list --count counts the commits selected by the revision expression."
            },
            {
                "question_text": "What is the purpose of git for-each-ref?",
                "options": ["Display references using customizable formatting", "Create a new reference for every file", "Fetch every remote repository", "Delete all tags and branches"],
                "correct_answer": 0,
                "explanation": "git for-each-ref iterates over references and formats their information."
            },
            {
                "question_text": "What does git update-ref do?",
                "options": ["Safely create, update, or delete references", "Update the contents of every tracked file", "Change the Git executable version", "Modify GitHub organization settings"],
                "correct_answer": 0,
                "explanation": "git update-ref manages references such as branch pointers."
            },
            {
                "question_text": "What is the purpose of git symbolic-ref?",
                "options": ["Read or update symbolic references such as HEAD", "Create a signed commit", "Compress repository objects", "Compare two commit trees"],
                "correct_answer": 0,
                "explanation": "git symbolic-ref reads or changes symbolic references that point to other references."
            },
            {
                "question_text": "What does git rev-parse --show-toplevel return?",
                "options": ["The absolute path of the working tree's top-level directory", "The latest commit message", "The remote repository name", "The number of tracked files"],
                "correct_answer": 0,
                "explanation": "The command prints the root directory of the current working tree."
            },
            {
                "question_text": "What is the purpose of git rev-parse --git-dir?",
                "options": ["Show the path to the Git directory", "Display all branches in graph form", "List all GitHub collaborators", "Show the repository license"],
                "correct_answer": 0,
                "explanation": "The option prints the path to the Git directory containing repository metadata."
            },
            {
                "question_text": "What is the purpose of git verify-commit?",
                "options": ["Verify the cryptographic signature on a commit", "Check whether a commit contains syntax errors", "Confirm that a commit has been pushed", "Check whether every file is tracked"],
                "correct_answer": 0,
                "explanation": "git verify-commit checks the GPG signature associated with a signed commit."
            },
            {
                "question_text": "What is the purpose of git verify-tag?",
                "options": ["Verify the cryptographic signature on an annotated tag", "Check whether a tag name is unique on GitHub", "Merge the tagged commit into main", "Delete unsigned tags"],
                "correct_answer": 0,
                "explanation": "git verify-tag verifies the signature attached to a signed annotated tag."
            },
            {
                "question_text": "What does git commit -S request?",
                "options": ["Create a commit with a cryptographic signature", "Create a shallow commit", "Skip the commit hooks", "Squash all previous commits"],
                "correct_answer": 0,
                "explanation": "The -S option requests signing the commit with a configured signing key."
            },
            {
                "question_text": "What is the purpose of git fsck --lost-found?",
                "options": ["Write dangling objects into the lost-found area for inspection", "Delete every unreachable object immediately", "Recover a deleted GitHub account", "Restore all remote branches automatically"],
                "correct_answer": 0,
                "explanation": "The --lost-found option writes dangling objects into .git/lost-found so they can be inspected."
            }
        ]
    }
]

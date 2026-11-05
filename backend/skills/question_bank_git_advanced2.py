
QUESTION_BANK_GIT_ADVANCED2 = [
    {
        "skill": "Git & GitHub",
        "difficulty": "advanced",
        "questions": [
            {
                "question_text": "What is the purpose of the Git attributes file?",
                "options": ["Define path-specific attributes that affect Git behavior", "Store remote authentication passwords", "Create new commit objects", "Configure GitHub organization members"],
                "correct_answer": 0,
                "explanation": ".gitattributes defines attributes for paths, such as text handling, diff behavior, and merge behavior."
            },
            {
                "question_text": "Which file commonly stores repository-specific Git attributes?",
                "options": [".gitattributes", ".gitconfig", ".gitmodules", ".gitrefs"],
                "correct_answer": 0,
                "explanation": "A .gitattributes file stores path-specific attribute patterns in a repository."
            },
            {
                "question_text": "What does the text attribute in .gitattributes help control?",
                "options": ["Whether Git treats a path as text for line-ending normalization", "Whether a file is executable on every operating system", "Whether a commit is signed", "Whether a branch can be merged"],
                "correct_answer": 0,
                "explanation": "The text attribute controls Git's text and line-ending normalization behavior."
            },
            {
                "question_text": "What is the purpose of the export-ignore attribute?",
                "options": ["Exclude matching paths from archives created by git archive", "Ignore matching files during every commit", "Remove matching files from the repository history", "Prevent matching files from being cloned"],
                "correct_answer": 0,
                "explanation": "export-ignore excludes matching paths from archives produced by git archive."
            },
            {
                "question_text": "What does the diff attribute in .gitattributes configure?",
                "options": ["How Git generates or handles diffs for matching paths", "How Git pushes commits to a remote", "How Git names branches", "How Git stores user credentials"],
                "correct_answer": 0,
                "explanation": "The diff attribute can select diff drivers or control whether paths are treated as binary for diff purposes."
            },
            {
                "question_text": "What is a custom Git merge driver used for?",
                "options": ["Apply specialized merge logic to matching files", "Authenticate users before pushing", "Compress commit objects", "Create remote-tracking branches"],
                "correct_answer": 0,
                "explanation": "A custom merge driver allows specialized logic to resolve or process merges for selected file types."
            },
            {
                "question_text": "What is the purpose of the clean filter in Git attributes?",
                "options": ["Transform file content when it is added to the index", "Delete untracked directories", "Remove old commit objects", "Clean up remote branches"],
                "correct_answer": 0,
                "explanation": "A clean filter transforms content as it enters the Git index."
            },
            {
                "question_text": "What is the purpose of the smudge filter in Git attributes?",
                "options": ["Transform content when Git checks it out into the working tree", "Transform commit messages during a push", "Delete ignored files", "Compress all repository objects"],
                "correct_answer": 0,
                "explanation": "A smudge filter transforms stored content as Git writes it into the working tree."
            },
            {
                "question_text": "What is Git Large File Storage (LFS) designed to handle?",
                "options": ["Large files by storing pointer files in Git and file contents in separate storage", "Large numbers of branch names only", "Automatic conversion of source code into binaries", "Storage of GitHub issue comments"],
                "correct_answer": 0,
                "explanation": "Git LFS keeps lightweight pointers in Git while storing large file contents in LFS storage."
            },
            {
                "question_text": "What does a Git LFS pointer file contain?",
                "options": ["Metadata identifying the LFS object, including its content hash and size", "The complete binary content of the large file", "A list of all repository commits", "The private SSH key of the repository owner"],
                "correct_answer": 0,
                "explanation": "An LFS pointer records information such as the object identifier and size of the external file."
            },
            {
                "question_text": "What is the purpose of git lfs track?",
                "options": ["Configure file patterns to be managed by Git LFS", "Track the location of every Git commit", "Monitor remote branch activity", "Create a GitHub issue"],
                "correct_answer": 0,
                "explanation": "git lfs track configures patterns so matching files are handled by Git LFS."
            },
            {
                "question_text": "What is the purpose of a Git reference transaction?",
                "options": ["Update multiple references together with consistency guarantees", "Combine multiple source files into one blob", "Create multiple GitHub accounts", "Download multiple repositories in parallel only"],
                "correct_answer": 0,
                "explanation": "Reference transactions allow related reference updates to be handled as a coordinated operation."
            },
            {
                "question_text": "What does git update-ref --stdin allow?",
                "options": ["Read multiple reference update commands from standard input", "Read source files from the staging area", "Create commits from standard input automatically", "Fetch remote branches using a text file"],
                "correct_answer": 0,
                "explanation": "The --stdin option lets git update-ref process reference operations supplied through standard input."
            },
            {
                "question_text": "What is the purpose of Git's commit-graph file?",
                "options": ["Accelerate commit graph traversal and history-related operations", "Store the full contents of every working-tree file", "Replace the index permanently", "Store GitHub pull request discussions"],
                "correct_answer": 0,
                "explanation": "The commit-graph file stores commit graph information to speed up certain history operations."
            },
            {
                "question_text": "Which command writes or updates the commit-graph data?",
                "options": ["git commit-graph write", "git graph commit --save", "git log --write-graph", "git gc --commit-graph-only"],
                "correct_answer": 0,
                "explanation": "git commit-graph write generates or updates commit-graph data."
            },
            {
                "question_text": "What is a multi-pack index in Git?",
                "options": ["An index that helps locate objects across multiple packfiles", "A list of multiple GitHub repositories", "A shared index of every user's working tree", "A file containing all commit messages"],
                "correct_answer": 0,
                "explanation": "The multi-pack index provides an object lookup structure across multiple packfiles."
            },
            {
                "question_text": "Which Git command manages the multi-pack index?",
                "options": ["git multi-pack-index", "git pack-list", "git index-remote", "git object-index"],
                "correct_answer": 0,
                "explanation": "git multi-pack-index provides operations for writing, verifying, and maintaining a multi-pack index."
            },
            {
                "question_text": "What is the purpose of the Git alternates mechanism?",
                "options": ["Allow an object database to borrow objects from another object database", "Create alternate commit messages", "Switch automatically between GitHub accounts", "Store two versions of every branch"],
                "correct_answer": 0,
                "explanation": "Alternates let one repository use objects stored in another object database."
            },
            {
                "question_text": "Where can Git object alternates be configured for a repository?",
                "options": ["In the objects/info/alternates file", "In README.md", "In the current branch name", "In .gitignore"],
                "correct_answer": 0,
                "explanation": "Git reads alternate object database locations from the objects/info/alternates file."
            },
            {
                "question_text": "What is the purpose of the Git quarantine environment on a receiving server?",
                "options": ["Temporarily isolate incoming objects while receive-side checks run", "Encrypt all existing commits permanently", "Hide every remote branch from collaborators", "Store rejected pull request comments"],
                "correct_answer": 0,
                "explanation": "Git can place incoming objects in a quarantine area before accepting them into the main object database."
            },
            {
                "question_text": "Which server-side hook can reject a push before reference updates are applied?",
                "options": ["pre-receive", "post-commit", "prepare-commit-msg", "post-checkout"],
                "correct_answer": 0,
                "explanation": "The pre-receive hook runs before updates are accepted and can reject the entire push."
            },
            {
                "question_text": "What is the purpose of the update Git server-side hook?",
                "options": ["Inspect and accept or reject an individual reference update", "Run after a developer changes branches locally", "Format commit messages in the working tree", "Download missing LFS files"],
                "correct_answer": 0,
                "explanation": "The update hook is invoked separately for each proposed reference update and can reject individual updates."
            },
            {
                "question_text": "When does the post-receive hook run on a Git server?",
                "options": ["After a push has successfully updated references", "Before a local commit is created", "Before files are staged", "Whenever a developer runs git status"],
                "correct_answer": 0,
                "explanation": "The post-receive hook runs after successful reference updates and can be used for notifications or deployment tasks."
            },
            {
                "question_text": "What is the purpose of the pre-rebase hook?",
                "options": ["Run checks before a rebase starts", "Run after every successful push", "Validate a remote repository URL", "Automatically resolve all rebase conflicts"],
                "correct_answer": 0,
                "explanation": "The pre-rebase hook can prevent a rebase from starting when configured conditions are not met."
            },
            {
                "question_text": "Which hook can prepare or modify a commit message before the editor is opened?",
                "options": ["prepare-commit-msg", "post-merge", "post-rewrite", "pre-push"],
                "correct_answer": 0,
                "explanation": "prepare-commit-msg runs before the commit message editor is started and can modify the message file."
            },
            {
                "question_text": "What is the purpose of the commit-msg hook?",
                "options": ["Validate or modify the proposed commit message", "Check remote branch permissions", "Run after a repository is cloned", "Clean unreachable Git objects"],
                "correct_answer": 0,
                "explanation": "The commit-msg hook receives the proposed message file and can reject an invalid message."
            },
            {
                "question_text": "What does the post-rewrite hook receive?",
                "options": ["Information about commits replaced by history-rewriting commands", "A list of every tracked file", "The password used for an HTTPS push", "The contents of all remote repositories"],
                "correct_answer": 0,
                "explanation": "The post-rewrite hook can receive old and new commit IDs after commands such as amend or rebase."
            },
            {
                "question_text": "What is the purpose of git notes copy?",
                "options": ["Copy a note from one Git object to another", "Copy a repository to a remote server", "Copy all branches into a new worktree", "Copy ignored files into the index"],
                "correct_answer": 0,
                "explanation": "git notes copy copies a note associated with one object to another object."
            },
            {
                "question_text": "What does git notes merge do?",
                "options": ["Merge notes references and resolve note conflicts when necessary", "Merge source branches into main", "Combine two Git repositories into one", "Merge all tags into a single tag"],
                "correct_answer": 0,
                "explanation": "git notes merge combines notes histories and may require conflict resolution."
            },
            {
                "question_text": "What is the purpose of the notes.rewrite configuration?",
                "options": ["Control whether notes are copied when commits are rewritten", "Control automatic source-code formatting", "Choose the default remote branch", "Set the repository's compression level"],
                "correct_answer": 0,
                "explanation": "notes.rewrite settings control copying notes to replacement commits during supported history-rewriting operations."
            },
            {
                "question_text": "What is a Git namespace?",
                "options": ["A way to group references under a separate reference namespace", "A separate programming language inside Git", "A directory for all untracked files", "A method of encrypting commit contents"],
                "correct_answer": 0,
                "explanation": "Git namespaces provide separate reference spaces within one repository, commonly used by hosting systems."
            },
            {
                "question_text": "Which environment variable can select a Git reference namespace?",
                "options": ["GIT_NAMESPACE", "GIT_BRANCH_MODE", "GIT_REMOTE_SCOPE", "GIT_OBJECT_NAME"],
                "correct_answer": 0,
                "explanation": "GIT_NAMESPACE selects the namespace used for reference operations."
            },
            {
                "question_text": "What is the purpose of git upload-pack?",
                "options": ["Serve Git objects to a client during fetch or clone operations", "Receive and store commits pushed by a client", "Create GitHub releases", "Run local commit hooks"],
                "correct_answer": 0,
                "explanation": "upload-pack is the server-side service used to provide objects for fetch and clone."
            },
            {
                "question_text": "What is the purpose of git receive-pack?",
                "options": ["Receive objects and reference updates sent during a push", "Download objects during a clone", "Create a local commit graph", "List all GitHub organization members"],
                "correct_answer": 0,
                "explanation": "receive-pack is the server-side service that receives pushed objects and updates references."
            },
            {
                "question_text": "What does the Git protocol capability side-band-64k provide?",
                "options": ["Multiplex progress and error information with pack data using larger side-band packets", "Encrypt all Git traffic with a new key", "Transfer only files smaller than 64 kilobytes", "Create 64,000 remote branches"],
                "correct_answer": 0,
                "explanation": "side-band-64k multiplexes data channels and allows larger side-band packet sizes."
            },
            {
                "question_text": "What is the purpose of the Git protocol capability thin-pack?",
                "options": ["Allow pack data to omit some base objects that the receiver is expected to have", "Force every object to be stored uncompressed", "Transfer only commit messages", "Prevent shallow clones"],
                "correct_answer": 0,
                "explanation": "Thin packs can use delta bases expected to exist at the receiver, reducing transferred data."
            },
            {
                "question_text": "What is the purpose of the Git protocol capability ofs-delta?",
                "options": ["Allow delta objects to refer to their bases by offset within a packfile", "Allow commits to use file-system paths as parent IDs", "Enable remote branch deletion", "Compress commit messages using offsets"],
                "correct_answer": 0,
                "explanation": "ofs-delta permits packfile delta bases to be identified by their offset within the same pack."
            },
            {
                "question_text": "What is the purpose of git daemon?",
                "options": ["Provide a Git protocol service for serving repositories over a network", "Run GitHub Actions workflows", "Automatically resolve merge conflicts", "Create signed release tags"],
                "correct_answer": 0,
                "explanation": "git daemon serves repositories using Git's native unauthenticated network protocol, subject to its configuration."
            },
            {
                "question_text": "What does git ls-remote display?",
                "options": ["References and object IDs advertised by a remote repository", "All files in a remote working tree", "Every commit message in full", "All users with access to the remote"],
                "correct_answer": 0,
                "explanation": "git ls-remote lists references and their object IDs without creating a local clone."
            },
            {
                "question_text": "Which command lists references advertised by the origin remote?",
                "options": ["git ls-remote origin", "git remote --show-files origin", "git branch --remote-url origin", "git fetch --list-only origin"],
                "correct_answer": 0,
                "explanation": "git ls-remote origin queries the remote and prints its advertised references."
            },
            {
                "question_text": "What is the purpose of git check-ref-format?",
                "options": ["Validate whether a string is a valid Git reference name", "Check the contents of a commit object", "Verify a signed Git tag", "Validate every file's syntax"],
                "correct_answer": 0,
                "explanation": "git check-ref-format checks whether a proposed reference name follows Git's naming rules."
            },
            {
                "question_text": "What does git symbolic-ref HEAD refs/heads/develop do in a normal repository?",
                "options": ["Set HEAD to symbolically refer to the develop branch", "Create a commit on develop", "Merge develop into HEAD", "Delete the current branch"],
                "correct_answer": 0,
                "explanation": "The command updates the symbolic HEAD reference to point to refs/heads/develop."
            },
            {
                "question_text": "What is the purpose of git worktree repair?",
                "options": ["Repair administrative links for linked working trees after their locations change", "Repair corrupted source-code syntax", "Restore deleted remote commits", "Resolve all conflicts in open pull requests"],
                "correct_answer": 0,
                "explanation": "git worktree repair repairs administrative links when working trees have been moved or their locations have changed."
            },
            {
                "question_text": "What is the purpose of git sparse-checkout reapply?",
                "options": ["Reapply sparse-checkout rules to the working tree", "Repeat the last commit message", "Fetch all missing remote branches", "Recreate deleted tags"],
                "correct_answer": 0,
                "explanation": "git sparse-checkout reapply updates the working tree to match the current sparse-checkout patterns."
            },
            {
                "question_text": "What does git maintenance run perform?",
                "options": ["Run configured repository maintenance tasks", "Run all project unit tests", "Deploy the current branch to production", "Automatically merge open pull requests"],
                "correct_answer": 0,
                "explanation": "git maintenance run executes configured maintenance tasks to help keep a repository efficient."
            },
            {
                "question_text": "What is the purpose of git maintenance start?",
                "options": ["Enable scheduled background maintenance for the repository", "Create the first commit", "Start a GitHub Actions workflow manually", "Start an interactive rebase"],
                "correct_answer": 0,
                "explanation": "git maintenance start registers background maintenance according to the platform's scheduling mechanism."
            },
            {
                "question_text": "What does git verify-pack -v inspect?",
                "options": ["The contents and integrity information of a Git pack index", "The syntax of every tracked source file", "The permissions of GitHub collaborators", "The commit messages in a pull request"],
                "correct_answer": 0,
                "explanation": "git verify-pack verifies pack index files and can display information about objects stored in the pack."
            },
            {
                "question_text": "What is the purpose of git index-pack?",
                "options": ["Create a pack index from a packed Git object stream", "Create a list of files for .gitignore", "Create a commit from the current index", "Create a GitHub issue index"],
                "correct_answer": 0,
                "explanation": "git index-pack builds a pack index and can store the received pack in the object database."
            },
            {
                "question_text": "What does git unpack-objects do?",
                "options": ["Unpack objects from a packed archive into the object database", "Remove all objects from the repository", "Unpack a ZIP archive of source files", "Convert a branch into a tag"],
                "correct_answer": 0,
                "explanation": "git unpack-objects reads packed Git objects and writes them as loose objects."
            },
            {
                "question_text": "What is the purpose of git mktag?",
                "options": ["Create a tag object from supplied tag-object content", "Create a new local branch", "Create a GitHub release automatically", "Convert a blob into a tree"],
                "correct_answer": 0,
                "explanation": "git mktag creates a tag object after validating the supplied tag-object content."
            }
        ]
    }
]

# Exam_control_versioning


### Explain the concept of git worktrees [3rd Question]

Git worktrees feature allows to work on multiple branches of a repository simultaneously, each in its own separate working directory
This is useful particularly for managing different branches without need to constantly switch between them in the same working directory.

git worktree add <path> <branch> : this create a new worktree and create the branch if not exist(ed) yet
several command can be used in this respect such as :
- git worktree list : To shows all the worktrees associated with the repository
- git worktree remove <path> : This removes the worktree at <path>
- git worktree prune : To clean up references to worktrees that are no longer valid

To sum up: Is custommary to fix bugs in a separate worktree without interrupting your ongoing feature development.

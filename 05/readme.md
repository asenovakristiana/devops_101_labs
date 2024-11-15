# Prerequisites
* Install Git on your WSL2 Ubuntu 24.04
```bash
sudo apt install git -y
```
**Note:** For alternative installtions, you can check the official [Git](https://git-scm.com/downloads) download page.  

* Create a GitHub account if you don't have one.
* Set up SSH or HTTPS authentication for your GitHub account. For ssh key authentication you can follow the offical [documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui)

# Step 1: Cloning a Repository
1. On GitHub, create a new repository or use an existing one. You can follow the offical [documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

1. Copy the repository URL.
2. Open your terminal and run:
```bash
git clone <repository-url>
```

* Example:
```bash
git clone https://github.com/your-username/your-repo.git
```

* Navigate to the cloned repository
```bash
cd your-repo
```

# Step 2: Creating and Switching to a New Branch
* Create and switch to a new branch named feature-branch:

```bash
git checkout -b feature-branch
```

* Show branches
```bash
git branch
```
**Note:** The current branch will be highlighted.

# Step 3: Making Changes
* Open any file in the repository and make changes, or create a new file:

```bash
echo "Hello, Git!" > hello.txt
```

* View the changes:
```bash
git status
```

# Step 4: Staging Changes
* Stage your changes to prepare them for commit.
* Add the specific file:
```bash
git add hello.txt
```

* Optionally you can add all changes:
```bash
git add .
```

# Step 5: Committing Changes
* Commit your staged changes with a descriptive message:
```bash
git commit -m "Added hello.txt with a greeting"
```

# Step 6: Pushing Changes
* Push your branch to the remote repository.

* Push your changes:
``` bash
git push origin feature-branch
```

* If this is your first push for the branch, you may need:
```bash
git push --set-upstream origin feature-branch
```

# Step 7: Merging Changes
* Merge your feature branch into the main branch.
* Switch to the main branch:
```bash
git checkout main
```

* Merge the feature-branch:
```bash
git merge feature-branch
```

**Note:** In team projects, the main branch is usually protected and you cannot push changes directly to it. You will need to open a pull request which will need to pass any quolity checks/guards and and required peer review approval.

# Step 8: Pulling Latest Changes
Pull the latest changes from the remote repository.

```bash
git pull origin main
```

# Additional Commands
* Viewing Logs:
``` bash
git log
```
**Note:** Use q to exit.

* Unstage a file:
```bash
git reset hello.txt
```

* Revert all uncommitted changes:
```bash
git checkout .
```

* Deleting a Branch:
``` bash
git branch -d feature-branch
```

* Removing a Remote Branch:
```bash
git push origin --delete feature-branch
```
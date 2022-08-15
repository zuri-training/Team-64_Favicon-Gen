## COLLABORATORS' GUIDE

Collaborators on this project are to use the Shared Repository Model. This model allows collaborators push access to a single shared repository but topic (feature) branches must be created when changes need to be made or a feature added.

This repository contains the following branches:

1. The main branch

(WARNING: Do not push to the main branch! Only the Master Merger(s) assigned by the team can do this after pull request reviews on the Dev branches.)

2. Dev branches

i) frontend branch
All subsequent frontend branches created by collaborators will be merged here by the Master merger(s).

ii) Backend branch
All subsequent backend branches created by collaborators will be merged here by the Master merger(s).

3. Topic (Feature) branches
   These branches are made by contributors for each feature, e.g., LogIn, SignUp, etc.

### STEPS TO FOLLOW

Follow the steps below to collaborate here properly.

**A] Clone the repo to your local machine.**

To do this,
Open your code editor and choose "Clone Git Repository", then click on "Clone from GitHub", and enter

`https://github.com/zuri-training/Team-64_Favicon-Gen.git`

to search for this repository.
Next, select the clone directory and "open the cloned repository".

**B] Create a new (feature/ topic) branch**

**Firstly**, run the –set-upstream switch. This informs your new branch of the remote repo to pull changes from to update your local repo.

To do this, run this command in your terminal:

`git remote add upstream https://github.com/zuri-training/Team-64_Favicon-Gen`

**Secondly**, switch to the appropriate dev branch i.e., Backend or frontend.

To do this, run either of these commands in your terminal:

`git checkout frontend`

OR

`git checkout Backend`

**Then**, create a feature branch.

To do this, run this command in your terminal:

`git checkout -b branchname`

Good!

**C] Now, activate your virtual environment and install the project dependencies (run: pip install -r requirements.txt)**

**D] Work in your feature branch:**

i) Add your codes to your feature branch,

ii) stage the changes, and

iii) commit the changes with a clear commit message.

**E] Update from your upstream branch.**

Right before you push your codes to your feature branch, check for any updates to the upstream branch.

To do this, run this command in your terminal:

`git pull upstream frontend`

OR

`git pull upstream Backend`

(Check for any ensuing conflicts, resolve them, and commit the changes before you push)

**F] Publish/ Push your branch.**

Publish your feature branch and the committed changes.

To do this, run this command in your terminal:

`git push origin branchname`

**G] Make a Pull Request.**

When you have made all necessary commits:
Move over to the GitHub repo, and create a Pull Request to the appropriate dev branch i.e., frontend or Backend. Include the changes you made or feature you built in your topic branch, and tag the assigned Master Merger(s) to alert them for a review.

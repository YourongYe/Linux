# Update version
git init (initialising)

git clone  
* cloned the repository from GitHub to local (can do via command)

git add .(everything) <filename> or <foldername> (a group of files) - staging
git add demo.txt
git add file1 file2 file3

git commit -m “message” (not -m, will open a text editor and you can write multiple lines). Commit the changes

git push (to GitHub)

git pull (to bring to local repository)


git status -  to find out information regarding what files are modified and what files are there in the staging area

git log - The log shows the author of each commit, the date of the commit, and the commit message.

# Branch - personal version
git branch test - This command creates the test branch.

git checkout test - Now we are in the test branch.

git branch - You can list out all the branches in local

# Merge your branch to master branch
git checkout master
git pull 
git checkout <the name of your branch>
git merge master
-> then accept the changes 

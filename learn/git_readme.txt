#git cheatsheet with commands. commit,status,stash,push,pull,clone,add 
$git config --global user.name <username>
$git config --global user.email <emailaddress>
$git config --global init.default branch main           #Set default branch to main
$git help config 
$git <command> -h
$git init           #Initialize a new git repository
$git clone <repositoryurl>           #Clone a repository
$git add <filename>            #Add a file to the staging area
$git add --all
$git add -A
$git add .
$git diff
$git commit -m "<message>"         #Commit the staged changes
$git reset
$git status
$git rm <filename>
$git mv <oldfilename> <newfilename>
$git log
$git branch         #List all the local braches 
$git branch <branchname>
$git branch -m <newbranchname>
$git branch -m <oldbranchname> <newbranchname>           #Rename the current branch
$git branch -d <branchname>           #Delete a branch
$git branch -u origin/master master     #to set the upstream branch for local machine 
$git switch <branchname>
$git merge <branchname>       #Merge specified branch into the current branch
$git remote add <name> <repository url>      #Create a connection to a remote repository
$git push <remote> <branch>          #Push the committed changes to a remote directory
$git pull <remoterepository>         #Download the content from a remote repository
$git remote -v # get the repositories push and fetch information 
$git remote remove <origin>
$git fetch origin master 
$git remote set-url origin https://<username>:<TokenID>@github.com/stejareddy/my_local_repo.git         #if authentication issues arise
$git remote set-url origin "<ssh link for github repository>"  #need sshkeypair before using this step 
$git pull origin master 
$git fetch origin # pulls updates without changing existing stuff 
$git remote set-head origin -a #to track correct default branch as head for future pull/push 
$git log origin/master 



#Generating new SSH key pair to connect github with local machine's file system. 
        $ssh-keygen -t ed25519 -C "<emailaddress>" 
    -click enter untill key is generated
        $cat ~/.ssh/id_ed15519.pub 
    -copy the date inside this file and paste it on to a text editor 
    -INBROWSER: settings > SSH and GPG keys > New SSH key 
    -Paste the data here  and save it. 
    -Back to terminal and navigate to the folder that needs to be connected with github  
        $git remote set-url origin <paste the git SSH repo link from github online profile>
        $git remote -v 
    - To add other files to git hub you don't need to do generate key again. just navigate to that folder and use git remote set-url command to connect with it's respective online Repository. 
    


#Token & SSH keys 
1. (Expired Jan 13th 2025) my_local_repo :  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 #This token is if you use https url to connect with github and it doesn't allow password so a token has to be created. 
2. ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMzW0aBxA8REei0/t+ii680wv+N6q5ymYfXkcZTfSkKT steja2396@outlook.com #ssh key for my_local_repo it's found in ~/.ssh/id_ed15519.pub 

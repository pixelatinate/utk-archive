# Practice 0

Welcome to CS445/545. In this class we will be using a variety of
tools that will require some initial configuration. 

1. To start, repository fdac22/Practice0.
2.  You should be able to connect to your
   container via ssh (putty)  
   When you connect, make sure you have your SSH agent forwarded! The option is `-o ForwardAgent=yes` for the cli or `ForwardAgent yes` in the ssh config.  
   This ensures you don't have to store your private key on the server for security reasons.
3. Connect to your docker container (this opens up a terminal with a commmand-line)  
    Ensure you have enabled your SSH agent forwarding and that your SSH key is added to your local agent!
4. Clone the repository to your docker container
  If you have not set these up, please do (replace with your own information):
    ```
	git config --global user.name "Your Name"
	git config --global user.email "netid@vols.utk.edu" # use any email you want that you have linked to github
    ```
    
5. Set up your default editor if you don't like vi (vi is set by default)
    ```
    git config --global core.editor nano
    ```
   
	 You will also need to put your public key on github as described in step 4 of [instructions](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).
    
6. Now clone
    ```
   git clone git@github.com:USERNAME/Practice0.git
    ```
 
7. Please change the name of the notebook from Practice0 to your NETID handle, so I can merge it in the central repository once you submit your pull request.
      on command line 'mv Practice0.ipynb YourNetID.ipynb' .
8. Point your browser to http://localhost:8888.
9. Edit/Run the example in the browser and do requested tasks to complete the assignment.
10. On the docker container commit changes to complete your solution.
    ```
    cd ~/Practice0
    git add YourNetID.ipynb
    git commit -m '<your commit comment>'
    ```
1. Now back in the shell and push/sync the changes to github.

        git push origin master
   
1. At https://github.com/USERNAME/Practice0
   Create a pull request to merge your notebook with the
   original repository fdac22/Practice0.

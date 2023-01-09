Mini Project1 - Text Analysis
===========

Please read the entire assignment.

Workflow
===============
1. To start, [**fork** repository][forking] [github.com/fdac22/MiniProject1][assignment]
    1. Go to github.com/fdac22/MiniProject1
    1. Click on "Fork Repository" button
	1. Select your GitHubID as the organization to fork to
	1. Go to Settings and enable issue tracking
1. Connect to your docker container
1. [**Clone**][ref-clone] the forked repository to your docker container

     ```
     git clone git@github.com:<GHUser>/MiniProject1.git
     ```
1. Copy [Miniproject1.ipynb](https://github.com/fdac22/MiniProject1/blob/master/MiniProject1.ipynb) to YourUTKID.ipynb

       git add YourUTKID.ipynb
       git commit -m "YOUR commit message"
1. Now back in the shell [**Push**][ref-push]/sync the changes to github.

	git push

1. At https://github.com/YourGHUsername/Miniproject1
   Create a [**pull request**][pull-request] on the
   original repository [fdac22/Miniproject1][assignment]  to
   turn in the assignment.
   
Presentations should include
===
* What is the question?
* What was the approach?
* What problems did I encounter?
* What results did I get?
* What new ideas did this generate?


<!-- Links -->
[assignment]: https://github.com/fdac22/Miniproject1
[forking]: https://guides.github.com/activities/forking/
[pull-request]: https://help.github.com/articles/creating-a-pull-request
[ref-clone]: https://help.github.com/en/articles/cloning-a-repository
[ref-commit]: https://readwrite.com/2013/10/02/github-for-beginners-part-2/
[ref-push]: https://help.github.com/en/articles/pushing-commits-to-a-remote-repository

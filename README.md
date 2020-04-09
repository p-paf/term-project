### Align3 - a simple game
This repository covers the development of a simple board game step by step into a modular, maintainable and resuable code base.

### Checking it out
The progress of the code base has marked milestones in different branches.

```
git clone https://github.com/p-paf/term-project.git
cd term-project
```

This downloads the master branch, which contains the first draft for the project code. You can checkout other branches. The examples uses the `stage_1` branch.

```
git fetch origin stage_1
git checkout stage_1
```

If you've made changes to a branch and want to checkout another branch you need to take extra steps. This [SO answer](https://stackoverflow.com/questions/22053757/checkout-another-branch-when-there-are-uncommitted-changes-on-the-current-branch) might help, but a simple set of instructions are given below. It assumes that code you have written was for experimental reasons and can be deleted.

```
git fetch origin stage_1
git checkout stage_1  # gives error because of uncommited changes
git reset --hard HEAD
git checkout stage_1
```

Keep a lookout for other branches as they are pushed.

### Running the game
Run the game with `python3 pipaf3.py`. If this fails you might need to install `python3-tk` library for your python version.

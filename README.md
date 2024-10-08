# Calculator Collaboration Test

## Project Introduction

Welcome to the Calculator Collaboration Test project!

### 1. Purpose
The primary goal of this project is to provide a hands-on experience in collaborating on a shared codebase using GitHub. As students, this project will help us understand the basics of version control, branching, pull requests, code reviews, and conflict resolution in a real-world setting.

### 2. Why a Calculator?
A calculator is an ideal project for collaboration due to its simplicity and modular nature. Each arithmetic operation (addition, subtraction, multiplication, division...) can be implemented independently, allowing us to divide the tasks easily among the team. This modular approach will help us practice:

- **Branching:** Working on separate branches for each feature.
- **Pull Requests:** Submitting and reviewing code changes.
- **Code Reviews:** Providing feedback and improving code quality.
- **Conflict Resolution:** Handling merge conflicts when integrating different branches.

## Initial Setup

### 1. Clone the repository:  
`git clone https://github.com/malhaouit/calculator-collaboration-test.git`  

### 2. Change directory to your new repository: 
`cd calculator-collaboration-test`  


## Workflow for Collaboration

### 1. Creating a New Branch:

- Always create a new branch for each feature or fix:  
`git checkout -b feature-branch-name`  

### 2. Making Changes:  
- Make your changes in the code.  
- Stage the changes:  
`git add .`  
- Commit the changes:  
`git commit -m "Description of the changes"`  

### 3. Pushing Changes to GitHub:
`git push origin feature-branch-name`  

### 4. Reviewing and Merging Pull Requests
- **Reviewing:**  
	+ Other collaborators can review the pull request.
	+ They can leave comments, approve, or request changes.

- **Merging:**
	+ Once approved, you or the repository owner can merge the pull request:
	+ On the pull request page, click "Merge pull request."
	+ Optionally, delete the branch after merging to keep the repository clean.  

Here is a demo video on youtube:  [Reviewing and Merging Pull Requests](https://www.youtube.com/watch?v=k5D37W6h56o)  


## Keeping Your Local Repository Updated  

1. Switch to the Main Branch:     
`git checkout main`  

2. Pull the Latest Changes:  
`git pull origin main`  


## Handling Conflicts

- If there are merge conflicts, Git will prompt you during the merge process.  
- Open the files with conflicts and manually resolve them.  
- After resolving, stage the changes:  
`git add .`  

- Continue the merge:  
`git commit`  


## Best Practices

1. **Regularly Pull Changes:**  

- Frequently pull changes from the main branch to keep your local repository updated.  

2. **Small and Frequent Commits:**  

- Make small, frequent commits with clear messages. This makes tracking changes easier.  

3. **Branch Naming Conventions:**  

- Use clear and consistent branch naming conventions like feature/feature-name, fix/bug-description.  

4. **Code Reviews:**  

- Engage in code reviews to ensure code quality and knowledge sharing.  

## ** Add

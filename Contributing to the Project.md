# Contributing to the Project

Thank you for your interest in contributing to this project! This guide explains how to report issues, suggest features, make changes, and submit contributions.

## 1. How to Report an Issue

If you find a problem in the project:

1. Check whether the issue has already been reported.
2. Describe the problem clearly.
3. Explain the steps needed to reproduce it.
4. Include the expected result and the actual result.

## 2. How to Suggest a Feature

To suggest a new feature:

1. Describe the feature you would like to add.
2. Explain why it would be useful.
3. Provide examples if necessary.
4. Submit your suggestion for discussion.

## 3. How to Create a Branch

Create a separate branch to work on your changes without directly modifying the main branch.

Run the following commands:

```bash
git checkout main
git pull
git checkout -b feature/your-feature-name
```

Replace `your-feature-name` with a short, meaningful name.

## 4. How to Make Changes

1. Open the project files.
2. Make the required changes.
3. Keep changes focused on one task.
4. Save your work.
5. Review your changes before submitting them.

## 5. How to Test Changes

Before submitting your changes:

1. Run the Python program.
2. Check that the modified code works as expected.
3. Test normal inputs and invalid inputs where applicable.
4. Fix any errors you find.
5. Run the program again to verify the changes.

## 6. How to Create a Pull Request

After completing and testing your changes:

1. Stage the changed files:

   ```bash
   git add .
   ```

2. Commit your changes:

   ```bash
   git commit -m "Describe your changes"
   ```

3. Push your branch to the remote repository:

   ```bash
   git push -u origin feature/your-feature-name
   ```

4. Open the project repository on GitHub.
5. Create a pull request from your branch into the main branch.
6. Provide a clear title and description of your changes.
7. Submit the pull request for review.

## 7. Basic Coding Guidelines

- Write clear and readable Python code.
- Use meaningful variable and function names.
- Follow consistent indentation.
- Keep functions simple and focused.
- Add comments when they help explain complex logic.
- Avoid unnecessary changes to existing code.
- Test your changes before submitting them.
- Write clear commit messages.

## Conclusion

Every contribution helps improve the project. Thank you for taking the time to report issues, suggest ideas, fix problems, and contribute to the project!
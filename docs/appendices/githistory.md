# Removing a file from git history

When projects involve sensitive information such as database credentials, secret keys or otherwise protected information, such information can be accidentally committed to version control.

Reversing this kind of mistake is not always easy, particularly if it was more than one commit behind the current state.

## Previously used command
The following code has been used to remove sensitive files from git version control (on Windows) in this project. Note this command will also _delete the current version of the file_.

```
git filter-branch --index-filter "git rm --cached --ignore-unmatch path/to/file.ext"
```

## Notes
- **Back up target file(s)** before running this command
- This code is a variant derived from online help pages
- The double quotes (```"```, not ```'```) are necessary on Windows
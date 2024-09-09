import sys

command_line_arguments = sys.argv[1::]
"""
The command line arguments provided by the user.

The intended format is:

`py scripts/rename-project.py project-top-level-domain project-author-name project-name`

Where:
- `project-top-level-domain` is the top level domain, such as net, com, dev, org, etc.
- `project-author-name` is the new author name of the project.
- `project-name` is the new project name.
"""

try:
    newProjectTopLevelDomain = command_line_arguments[0]
    """
    The top level domain, such as net, com, dev, org, etc.
    """
except:
    print("No new top-level-domain specified! Nothing to rename the project to.")
    print()
    print("Please use the following command format:")
    print("py scripts/rename-project.py project-top-level-domain project-author-name project-name")
    print()
    print("Where:")
    print("'project-top-level-domain' is the top level domain, such as net, com, dev, org, etc.")
    print("'project-author-name' is the new author name of the project.")
    print("'project-name' is the new project name.")
    print()
    print("Surround arguments with quotes if they contain spaces!")
    exit(1)

newProjectAuthorName = command_line_arguments[1] if len(command_line_arguments) >= 2 else None
"""
The new author name of the project.

This may be `None` if none is provided by the user in `command_line_arguments`.
"""

newProjectName = command_line_arguments[2] if len(command_line_arguments) == 3 else None
"""
The new project name.

This may be `None` if none is provided by the user in `command_line_arguments`.
"""

def dll_names():
    # Assigns the filename for the Microsoft Teams exports
    teams = "ms_teams_exports_usernev_dll.txt"

    # Assigns the filename for the OneDrive exports
    onedrive = "onedrive_exports_version_dll.txt"

    # Dictionary mapping simple names to their corresponding export filenames
    file_options = {"teams": teams, "onedrive": onedrive}

    # Returns the dictionary for use in other parts of the application
    return file_options

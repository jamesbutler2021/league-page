from github import Github
import os
import io

def export_to_github(players, format='1QB', tep=0):
    # Modify data for the league's settings
    if format == '1QB':
        header = [f"Updated {date.today().strftime('%m/%d/%y')} at {datetime.now().strftime('%I:%M%p').lower()}", "Position Rank", "Position", "Team", "Value", "Age", "Rookie", "SFPosition Rank", "SFValue", "RdrftPosition Rank", "RdrftValue"]
        # Add player data to the rows database
        rows_data = [[
            player["Player Name"],
            player["Position Rank"],
            player["Position"],
            player["Team"],
            player["Value"],
            player["Age"],
            player["Rookie"],
            player["SFPosition Rank"],
            player["SFValue"],
            player["RdrftPosition Rank"],
            player["RdrftValue"]
        ] for player in players]
        # Add the header row
        rows_data.insert(0, header)

    elif format == 'SF':
        header = [f"Updated {date.today().strftime('%m/%d/%y')} at {datetime.now().strftime('%I:%M%p').lower()}", "Position Rank", "Position", "Team", "Value", "Age", "Rookie", "1QBPosition Rank", "1QBValue", "RdrftPosition Rank", "RdrftValue"]
        # Add player data to the rows database
        rows_data = [[
            player["Player Name"],
            player["SFPosition Rank"],
            player["Position"],
            player["Team"],
            player["SFValue"],
            player["Age"],
            player["Rookie"],
            player["Position Rank"],
            player["Value"],
            player["SFRdrftPosition Rank"],
            player["SFRdrftValue"]
        ] for player in players]
        # Add the header row
        rows_data.insert(0, header)

    else:
        sys.exit(f"Error: invalid format -- {format}")

    # Adjust player values by TEP setting
    rows_data = tep_adjust(rows_data, tep)

    # Make player values unique for indexing and searchability
    rows_data = make_unique(rows_data)

    # Create the CSV content as a string
    output = io.StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerows(rows_data)
    csv_content = output.getvalue()

    # Authentication and repository details
    github_token = "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"  # Ensure your token is set as an environment variable or replace this line with your token directly
    g = Github(github_token)
    repo = g.get_repo("jamesbutler2021/league-page")  # Replace with your GitHub username/repo
    file_path = "/scripts/ktc.csv"  # Path to the file in your repo
    commit_message = f"Update KTC CSV for {date.today().strftime('%B %d, %Y')}"

    try:
        # Try to get the file if it exists
        file = repo.get_contents(file_path)
        # Update the file if it exists
        repo.update_file(file.path, commit_message, csv_content, file.sha)
        print(f"CSV file updated at {file_path} in the GitHub repository.")

    except Exception as e:
        # If the file doesn't exist, create it
        repo.create_file(file_path, commit_message, csv_content)
        print(f"CSV file created at {file_path} in the GitHub repository.")

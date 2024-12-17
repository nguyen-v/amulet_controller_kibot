import argparse
import re
import sys

def parse_changelog(file_path, version, show_title, spaces):
    try:
        with open(file_path, 'r') as f:
            changelog = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    underscores = int(spaces/2)

    # Regex to match the version block and stop at the next version or any line with square brackets
    version_pattern = re.compile(rf"## \[{version}\] - (\d{{4}}-\d{{2}}-\d{{2}})\n(.*?)(?=## \[|\[Unreleased\]:|\[\d+\.\d+\.\d+\]:|$)", re.DOTALL)
    match = version_pattern.search(changelog)

    if not match:
        print(f"Version {version} not found.")
        return

    date, content = match.groups()

    if show_title:
        print(f"Version {version} - {date}")
    else:
        content = re.sub(r'^(###.*?)$', '_' * underscores + r'\n\1', content, flags=re.MULTILINE)

        cleaned_content = re.sub(r'### ', '', content)  # Remove ###
        cleaned_content = re.sub(r'-\s+', '- ', cleaned_content)  # Remove space after '-'

        cleaned_content = re.sub(r'\n{2,}', ' ' * spaces + ' ' + ' ' * spaces, cleaned_content.strip())

        cleaned_content = re.sub(r'\n', ' ' * spaces + ' ' + ' ' * spaces, cleaned_content)
        print(cleaned_content)

def main():
    parser = argparse.ArgumentParser(description="Extract and format a specific version from CHANGELOG.md")
    parser.add_argument("-e", "--version", required=True, help="Version to extract (e.g., 1.0.1)")
    parser.add_argument("-f", "--file", required=True, help="Path to CHANGELOG.md file")
    parser.add_argument("-s", "--spaces", required=False, type=int, default=70, help="Column width in number of spaces (default: 70)")
    parser.add_argument("-t", action="store_true", help="Print the title only")

    args = parser.parse_args()
    parse_changelog(args.file, args.version, args.t, args.spaces)

if __name__ == "__main__":
    main()

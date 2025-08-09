#!/usr/bin/env python3
"""
GitHub Issue Creator

A flexible tool to automatically create GitHub issues from text files using
configurable JSON templates. Perfect for bulk issue creation, project planning,
and standardized workflows.

Features:
- Template-based issue creation
- Bulk creation from text files
- Configurable labels and assignees
- Duplicate prevention
- Dry run mode for testing
"""

import requests
import argparse
import os
import json
from dotenv import load_dotenv
from pathlib import Path

# Load GitHub token from .env if exists
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def load_config(config_file):
    """Load configuration from JSON file"""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Config file not found: {config_file}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in config file: {e}")
        exit(1)

def prompt_for_param(prompt, validator=None, default=None):
    while True:
        value = input(prompt)
        if not value and default is not None:
            return default
        if validator is None or validator(value):
            return value
        print("Invalid input. Please try again.")

def file_validator(f):
    return f.endswith('.txt') and os.path.isfile(f)

def dryrun_validator(val):
    return val.lower() in ['true', 'false', 't', 'f', 'yes', 'no', 'y', 'n', '']

def parse_dryrun(val):
    return val.lower() in ['true', 't', 'yes', 'y', '']

def get_existing_issue_titles(owner, repo):
    titles = set()
    page = 1
    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ Failed to fetch issues: {response.status_code}")
            break
        issues = response.json()
        if not issues:
            break
        for issue in issues:
            titles.add(issue['title'].strip().lower())
        page += 1
    return titles

def create_issue(config, item, existing_titles, dry_run=True):
    # Format the title using the template and item
    issue_title = config['issue_template']['title_format'].format(item=item)
    title_key = issue_title.lower()

    if title_key in existing_titles:
        print(f"⚠️ Skipped (already exists): {issue_title}")
        return

    # Format the body using the template and item
    issue_body = config['issue_template']['body_template'].format(item=item)

    # Prepare the payload
    payload = {
        "title": issue_title,
        "body": issue_body,
        "assignees": config.get('assignees', []),
        "labels": config.get('labels', [])
    }

    # Add milestone if specified
    if config.get('milestone'):
        payload["milestone"] = config['milestone']

    url = f"https://api.github.com/repos/{config['repository']['owner']}/{config['repository']['name']}/issues"
    print(f"🔍 Would post to: {url}")
    print(f"    Title: {issue_title}")
    print(f"    Labels: {', '.join(config.get('labels', []))}")
    if config.get('assignees'):
        print(f"    Assignees: {', '.join(config['assignees'])}")

    if dry_run:
        print(f"[DRY RUN] Issue not actually created.")
        return

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 201:
        print(f"✅ Created: {issue_title}")
    else:
        print(f"❌ Failed to create: {issue_title} — {response.status_code}")
        print(response.json())

def main():
    parser = argparse.ArgumentParser(description='Create GitHub issues from a config file and input list')
    parser.add_argument('--config', type=str, required=True, help='Path to config JSON file')
    parser.add_argument('--file', type=str, help='Path to input file (.txt) containing items list (overrides config)')
    parser.add_argument('--dry-run', dest='dry_run', action='store_true', help='Dry run (default: True, test only, no issues created)')
    parser.add_argument('--no-dry-run', dest='dry_run', action='store_false', help='Actually create issues')
    parser.set_defaults(dry_run=True)
    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Validate required config sections
    required_sections = ['repository', 'issue_template']
    for section in required_sections:
        if section not in config:
            print(f"❌ Missing required section '{section}' in config file")
            exit(1)

    # Validate repository config
    if 'owner' not in config['repository'] or 'name' not in config['repository']:
        print("❌ Repository config must include 'owner' and 'name'")
        exit(1)

    # Validate issue template config
    if 'title_format' not in config['issue_template'] or 'body_template' not in config['issue_template']:
        print("❌ Issue template config must include 'title_format' and 'body_template'")
        exit(1)

    # Get input file
    input_file = args.file or config.get('input_file')
    if not input_file:
        input_file = prompt_for_param("Enter path to .txt file: ", validator=file_validator)
    elif not file_validator(input_file):
        print(f"❌ Invalid input file: {input_file}")
        exit(1)

    dry_run = args.dry_run

    # Always show dry-run status to user
    print(f"\nDry run is set to: {dry_run} (default is True; set to False to actually create issues)\n")

    print(f"Summary of inputs:")
    print(f"  Config: {args.config}")
    print(f"  Owner: {config['repository']['owner']}")
    print(f"  Repo: {config['repository']['name']}")
    print(f"  Input File: {input_file}")
    print(f"  Target URL: https://github.com/{config['repository']['owner']}/{config['repository']['name']}/issues")
    print(f"  Labels: {', '.join(config.get('labels', []))}")
    if config.get('assignees'):
        print(f"  Assignees: {', '.join(config['assignees'])}")
    print(f"  Dry run: {dry_run}\n")

    if not GITHUB_TOKEN:
        print("❌ Missing GitHub token. Set GITHUB_TOKEN in .env or environment variables.")
        print("Create a .env file with: GITHUB_TOKEN=your_github_token_here")
        return

    existing_titles = get_existing_issue_titles(config['repository']['owner'], config['repository']['name'])

    with open(input_file, 'r') as f:
        for line in f:
            item = line.strip()
            if item:
                create_issue(config, item, existing_titles, dry_run=dry_run)

if __name__ == '__main__':
    main()

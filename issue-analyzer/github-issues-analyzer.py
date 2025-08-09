#!/usr/bin/env python3
"""
GitHub Issues Analyzer

A comprehensive tool to analyze and report on closed GitHub issues with advanced
filtering, analytics, and export capabilities.

Features:
- Filter by specific labels and date ranges
- Export to CSV, JSON, or console
- Detailed analytics and trend analysis
- Support for multiple repositories
"""

import requests
import argparse
import os
import json
import csv
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from dotenv import load_dotenv
from pathlib import Path

# Load GitHub token from .env if exists
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

class GitHubIssueAnalyzer:
    def __init__(self, owner, repo, token=None):
        self.owner = owner
        self.repo = repo
        self.token = token or GITHUB_TOKEN
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def get_closed_issues(self, since_date, until_date=None, labels=None, state='closed'):
        """
        Fetch closed issues from GitHub API with filtering

        Args:
            since_date: Start date for filtering (datetime object)
            until_date: End date for filtering (datetime object, optional)
            labels: List of labels to filter by (optional)
            state: Issue state to filter by (default: 'closed')

        Returns:
            List of issue objects
        """
        issues = []
        page = 1
        per_page = 100

        # Convert dates to ISO format
        since_str = since_date.strftime('%Y-%m-%dT%H:%M:%SZ')

        while True:
            # Build API URL with parameters
            url = f"https://api.github.com/repos/{self.owner}/{self.repo}/issues"
            params = {
                'state': state,
                'since': since_str,
                'per_page': per_page,
                'page': page,
                'sort': 'updated',
                'direction': 'desc'
            }

            # Add labels filter if specified
            if labels:
                params['labels'] = ','.join(labels)

            print(f"📡 Fetching page {page} of issues...")
            response = requests.get(url, headers=self.headers, params=params)

            if response.status_code != 200:
                print(f"❌ Failed to fetch issues: {response.status_code}")
                print(response.text)
                break

            page_issues = response.json()

            if not page_issues:
                break

            # Filter by closed date and until_date if specified
            for issue in page_issues:
                # Skip pull requests (they appear in issues API)
                if 'pull_request' in issue:
                    continue

                closed_at = issue.get('closed_at')
                if not closed_at:
                    continue

                closed_date = datetime.strptime(closed_at, '%Y-%m-%dT%H:%M:%SZ')

                # Check if within date range
                if closed_date >= since_date:
                    if until_date is None or closed_date <= until_date:
                        issues.append(issue)

            page += 1

            # If we're getting issues older than our since_date, we can stop
            if page_issues:
                last_closed = page_issues[-1].get('closed_at')
                if last_closed:
                    last_date = datetime.strptime(last_closed, '%Y-%m-%dT%H:%M:%SZ')
                    if last_date < since_date:
                        break

        return issues

    def analyze_issues(self, issues):
        """
        Analyze issues and generate statistics

        Args:
            issues: List of issue objects

        Returns:
            Dictionary with analysis results
        """
        analysis = {
            'total_count': len(issues),
            'by_label': defaultdict(int),
            'by_assignee': defaultdict(int),
            'by_author': defaultdict(int),
            'by_month': defaultdict(int),
            'by_week': defaultdict(int),
            'labels_combinations': Counter(),
            'avg_days_to_close': 0,
            'issues_detail': []
        }

        total_days = 0

        for issue in issues:
            # Basic counts
            created_at = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            closed_at = datetime.strptime(issue['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
            days_to_close = (closed_at - created_at).days
            total_days += days_to_close

            # Group by time periods
            month_key = closed_at.strftime('%Y-%m')
            week_key = closed_at.strftime('%Y-W%U')
            analysis['by_month'][month_key] += 1
            analysis['by_week'][week_key] += 1

            # Labels analysis
            issue_labels = [label['name'] for label in issue.get('labels', [])]
            for label in issue_labels:
                analysis['by_label'][label] += 1

            # Label combinations
            if issue_labels:
                label_combo = tuple(sorted(issue_labels))
                analysis['labels_combinations'][label_combo] += 1

            # Assignees
            assignees = issue.get('assignees', [])
            if assignees:
                for assignee in assignees:
                    analysis['by_assignee'][assignee['login']] += 1
            else:
                analysis['by_assignee']['unassigned'] += 1

            # Authors
            author = issue['user']['login']
            analysis['by_author'][author] += 1

            # Issue details for export
            analysis['issues_detail'].append({
                'number': issue['number'],
                'title': issue['title'],
                'author': author,
                'assignees': [a['login'] for a in assignees],
                'labels': issue_labels,
                'created_at': issue['created_at'],
                'closed_at': issue['closed_at'],
                'days_to_close': days_to_close,
                'url': issue['html_url'],
                'state': issue['state']
            })

        # Calculate average days to close
        if len(issues) > 0:
            analysis['avg_days_to_close'] = round(total_days / len(issues), 2)

        return analysis

    def generate_report(self, analysis, output_format='console'):
        """
        Generate and output the report

        Args:
            analysis: Analysis results from analyze_issues()
            output_format: 'console', 'csv', or 'json'
        """
        if output_format == 'console':
            self._print_console_report(analysis)
        elif output_format == 'csv':
            return self._export_csv_report(analysis)
        elif output_format == 'json':
            return self._export_json_report(analysis)

    def _print_console_report(self, analysis):
        """Print formatted report to console"""
        print(f"\n" + "="*60)
        print(f"📊 GITHUB ISSUES ANALYSIS REPORT")
        print(f"📁 Repository: {self.owner}/{self.repo}")
        print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"="*60)

        print(f"\n📈 SUMMARY STATISTICS")
        print(f"   Total Closed Issues: {analysis['total_count']}")
        print(f"   Average Days to Close: {analysis['avg_days_to_close']} days")

        if analysis['by_label']:
            print(f"\n🏷️  ISSUES BY LABEL")
            sorted_labels = sorted(analysis['by_label'].items(), key=lambda x: x[1], reverse=True)
            for label, count in sorted_labels:
                percentage = (count / analysis['total_count']) * 100
                print(f"   {label}: {count} ({percentage:.1f}%)")

        if analysis['by_assignee']:
            print(f"\n👥 ISSUES BY ASSIGNEE")
            sorted_assignees = sorted(analysis['by_assignee'].items(), key=lambda x: x[1], reverse=True)
            for assignee, count in sorted_assignees[:10]:  # Top 10
                percentage = (count / analysis['total_count']) * 100
                print(f"   {assignee}: {count} ({percentage:.1f}%)")

        if analysis['by_author']:
            print(f"\n✍️  ISSUES BY AUTHOR")
            sorted_authors = sorted(analysis['by_author'].items(), key=lambda x: x[1], reverse=True)
            for author, count in sorted_authors[:10]:  # Top 10
                percentage = (count / analysis['total_count']) * 100
                print(f"   {author}: {count} ({percentage:.1f}%)")

        if analysis['by_month']:
            print(f"\n📅 ISSUES BY MONTH")
            sorted_months = sorted(analysis['by_month'].items())
            for month, count in sorted_months:
                print(f"   {month}: {count}")

        if analysis['labels_combinations']:
            print(f"\n🔗 TOP LABEL COMBINATIONS")
            sorted_combos = analysis['labels_combinations'].most_common(10)
            for combo, count in sorted_combos:
                combo_str = ', '.join(combo) if combo else 'no labels'
                percentage = (count / analysis['total_count']) * 100
                print(f"   [{combo_str}]: {count} ({percentage:.1f}%)")

        print(f"\n" + "="*60)

    def _export_csv_report(self, analysis):
        """Export detailed report to CSV"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"github_issues_report_{self.owner}_{self.repo}_{timestamp}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'number', 'title', 'author', 'assignees', 'labels',
                'created_at', 'closed_at', 'days_to_close', 'url', 'state'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for issue in analysis['issues_detail']:
                # Convert lists to strings for CSV
                row = issue.copy()
                row['assignees'] = '; '.join(row['assignees'])
                row['labels'] = '; '.join(row['labels'])
                writer.writerow(row)

        print(f"✅ CSV report exported to: {filename}")
        return filename

    def _export_json_report(self, analysis):
        """Export detailed report to JSON"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"github_issues_report_{self.owner}_{self.repo}_{timestamp}.json"

        # Convert defaultdict to regular dict for JSON serialization
        report_data = {
            'metadata': {
                'repository': f"{self.owner}/{self.repo}",
                'generated_at': datetime.now().isoformat(),
                'total_issues': analysis['total_count'],
                'avg_days_to_close': analysis['avg_days_to_close']
            },
            'summary': {
                'by_label': dict(analysis['by_label']),
                'by_assignee': dict(analysis['by_assignee']),
                'by_author': dict(analysis['by_author']),
                'by_month': dict(analysis['by_month']),
                'by_week': dict(analysis['by_week']),
                'labels_combinations': dict(analysis['labels_combinations'])
            },
            'issues': analysis['issues_detail']
        }

        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(report_data, jsonfile, indent=2, ensure_ascii=False)

        print(f"✅ JSON report exported to: {filename}")
        return filename

def main():
    parser = argparse.ArgumentParser(
        description='Analyze and generate reports from closed GitHub issues',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic report for last 30 days
  python github-issues-analyzer.py --owner myorg --repo myrepo

  # Filter by specific labels
  python github-issues-analyzer.py --owner myorg --repo myrepo --labels bug,enhancement

  # Custom date range with CSV export
  python github-issues-analyzer.py --owner myorg --repo myrepo --days 60 --format csv

  # Multiple labels with JSON export
  python github-issues-analyzer.py --owner myorg --repo myrepo --labels "priority-high,bug" --format json
        """
    )

    parser.add_argument('--owner', type=str, required=True,
                       help='GitHub repository owner/organization')
    parser.add_argument('--repo', type=str, required=True,
                       help='GitHub repository name')
    parser.add_argument('--labels', type=str,
                       help='Comma-separated list of labels to filter by (e.g., "bug,enhancement")')
    parser.add_argument('--days', type=int, default=30,
                       help='Number of days to look back (default: 30)')
    parser.add_argument('--since', type=str,
                       help='Start date in YYYY-MM-DD format (overrides --days)')
    parser.add_argument('--until', type=str,
                       help='End date in YYYY-MM-DD format (default: today)')
    parser.add_argument('--format', choices=['console', 'csv', 'json'], default='console',
                       help='Output format (default: console)')
    parser.add_argument('--token', type=str,
                       help='GitHub token (can also use GITHUB_TOKEN env var)')

    args = parser.parse_args()

    # Validate token
    token = args.token or GITHUB_TOKEN
    if not token:
        print("❌ Missing GitHub token. Set GITHUB_TOKEN environment variable or use --token")
        print("Create a .env file with: GITHUB_TOKEN=your_github_token_here")
        return

    # Parse dates
    if args.since:
        try:
            since_date = datetime.strptime(args.since, '%Y-%m-%d')
        except ValueError:
            print("❌ Invalid since date format. Use YYYY-MM-DD")
            return
    else:
        since_date = datetime.now() - timedelta(days=args.days)

    until_date = None
    if args.until:
        try:
            until_date = datetime.strptime(args.until, '%Y-%m-%d')
            until_date = until_date.replace(hour=23, minute=59, second=59)  # End of day
        except ValueError:
            print("❌ Invalid until date format. Use YYYY-MM-DD")
            return

    # Parse labels
    labels = None
    if args.labels:
        labels = [label.strip() for label in args.labels.split(',')]

    print(f"🔍 Analyzing issues for {args.owner}/{args.repo}")
    print(f"📅 Date range: {since_date.strftime('%Y-%m-%d')} to {until_date.strftime('%Y-%m-%d') if until_date else 'now'}")
    if labels:
        print(f"🏷️  Filtering by labels: {', '.join(labels)}")
    print(f"📤 Output format: {args.format}")
    print()

    # Initialize analyzer and fetch data
    analyzer = GitHubIssueAnalyzer(args.owner, args.repo, token)

    try:
        issues = analyzer.get_closed_issues(since_date, until_date, labels)
        print(f"✅ Found {len(issues)} closed issues")

        if not issues:
            print("ℹ️  No issues found matching the criteria")
            return

        # Analyze and generate report
        analysis = analyzer.analyze_issues(issues)
        analyzer.generate_report(analysis, args.format)

    except Exception as e:
        print(f"❌ Error generating report: {str(e)}")
        return

if __name__ == '__main__':
    main()

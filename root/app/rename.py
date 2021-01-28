#!/usr/bin/python3 -u

import argparse
from qbittorrentapi import Client

parser = argparse.ArgumentParser(description='Rewrite a tracker URL across all your qBittorrent torrents')
parser.add_argument('old_tracker', metavar='OLD_TRACKER', help='old tracker URL')
parser.add_argument('new_tracker', metavar='NEW_TRACKER', help='new tracker URL')
parser.add_argument('--host', dest='host', default='http://localhost:8080', help='qBittorrent host URL (default: http://localhost:8080)')
parser.add_argument('--user', dest='username', default='admin', help='username (default: admin)')
parser.add_argument('--pass', dest='password', default='adminadmin', help='password (default: adminadmin)')
parser.add_argument('--dry-run', dest='dry_run', action='store_true', help='log actions instead of performing them')
parser.add_argument('--debug', dest='debug', action='store_true', help=argparse.SUPPRESS)

args = parser.parse_args()

if args.debug:
	print('Host:', args.host)
	print('User:', args.username)
	print('Pass:', args.password)
	print('Old tracker:', args.old_tracker)
	print('New tracker:', args.new_tracker)

client = Client(host=args.host, username=args.username, password=args.password)

for torrent in client.torrents.info():
	if args.debug:
		print('---', torrent.name, '---')

	for tracker in torrent.trackers:
		tracker_match = tracker.url == args.old_tracker
		if args.debug:
			print('Tracker:', tracker.url, tracker_match, tracker.status, tracker.msg)
		if tracker_match:
			print('Updating', torrent.name, 'tracker URL to', args.new_tracker)
			if not args.dry_run:
				torrent.editTracker(tracker.url, args.new_tracker)

qBittorrent Tracker Rewriter
============================

Rewrites a tracker URL across all your torrents.
Useful for batch-updating torrents when your passkey or the tracker URL changes.

This tool is provided as a Docker container.

[![Docker Ima ge Version](https://img.shields.io/docker/v/jakewharton/qbt-tracker-rewriter?sort=semver)][hub]
[![Docker Image Size](https://img.shields.io/docker/image-size/jakewharton/qbt-tracker-rewriter)][layers]

 [hub]: https://hub.docker.com/r/jakewharton/qbt-tracker-rewriter/
 [layers]: https://microbadger.com/images/jakewharton/qbt-tracker-rewriter


Usage
-----

The container connects to qBittorrent over its API which is exposed the same way as its web interface.

Only two arguments are required:
 1. The old tracker URL
 2. The new tracker URL

```
$ docker run \
    jakewharton/qbt-tracker-rewriter:trunk \
    http://old.example.com/tracker \
    http://new.example.com/tracker \
```

The default host is http://localhost:8080.
There are three general ways to connect:

 1. Use the qBittorrent container as the network for this container.
 2. Use the qBittorrent container hostname.
 3. Use an explicit hostname/IP that resolves to the container.

Option 2 and option 3 are really the same thing and are the recommended path.

For option 2, ensure your qBittorrent container has a hostname defined.
For `docker run` this means specifying `--hostname qbittorrent`.
For Docker Compose use the `hostname` key in the service definition:
```yaml
services:
  qbittorrent:
    image: linuxserver/qbittorrent
    hostname: qbittorrent
    # …
```

Use the `--host` argument to point the script at your container.

```
$ docker run \
    jakewharton/qbt-tracker-rewriter:trunk \
    --host http://qbittorrent:8080 \
    http://old.example.com/tracker \
    http://new.example.com/tracker \
```

You will also need a valid username and password.
The default username is 'admin', and the default password is 'adminadmin' which reflect the qBittorrent defaults.
If you have a non-default username or password, specify the `--user` and/or `--pass` arguments, respectively.

```
$ docker run \
    jakewharton/qbt-tracker-rewriter:trunk \
    --host http://qbittorrent:8080 \
    --user jake \
    --pass hunter2 \
    http://old.example.com/tracker \
    http://new.example.com/tracker \
```

To print the actions instead of performing them, add the `--dry-run` argument.


LICENSE
======

MIT. See `LICENSE.txt`.

    Copyright 2020 Jake Wharton

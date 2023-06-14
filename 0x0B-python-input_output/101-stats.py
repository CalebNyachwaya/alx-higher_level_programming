#!/usr/bin/python3
import sys

"""
Reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Every 10 lines or upon keyboard interruption (CTRL + C), prints statistics:
- Total file size: <total size> (sum of all previous file sizes)
- Number of lines by status code in ascending order: <status code>: <number>
Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
"""

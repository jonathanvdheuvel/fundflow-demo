#!/usr/bin/env python3
"""Simple local server for the FundFlow prototype."""

from __future__ import annotations

import argparse
import http.server
import os
import socketserver
from pathlib import Path


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a local web server for FundFlow")
    parser.add_argument("--port", type=int, default=4173, help="Port to serve on (default: 4173)")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind (default: 127.0.0.1)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    os.chdir(Path(__file__).resolve().parent)
    handler = http.server.SimpleHTTPRequestHandler

    with ReusableTCPServer((args.host, args.port), handler) as httpd:
        print(f"Serving FundFlow at http://{args.host}:{args.port}/fundflow.html")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")


if __name__ == "__main__":
    main()

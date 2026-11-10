#!/usr/bin/env python3
import http.server,os,webbrowser
from pathlib import Path
os.chdir(Path(__file__).parent/'viewer'); port=8000
print(f'Explorer: http://localhost:{port}'); http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,port=port)

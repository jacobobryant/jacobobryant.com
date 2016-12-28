#!/bin/bash
set -e
hugo
rsync -av ./public/ doserver:chocoserve/nginx/static/site/

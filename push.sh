#!/bin/bash
hugo && rsync -av ./public/ doserver:chocoserve/nginx/static/

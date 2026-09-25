#!/usr/bin/env bash
curl -s --max-time 1.5 "wttr.in/?format=%c+%t" 2>/dev/null | tr -d '+' || echo "☁ 16°C"

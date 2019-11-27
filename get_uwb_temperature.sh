#!/usr/bin/zsh
curl -s http://meteo.uwb.edu.pl/ \
	| tr '\n' '\r' \
	| sed -n -E "s/.*<td>Temperature<\/td>\r[[:space:]]+<td>([-0-9,]+)&.*/Temp at UWB:\r\1*C\r/p" \
	| tr '\r,' '\n.'

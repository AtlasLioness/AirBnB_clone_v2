#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

if ! [ -x "$(command -v nginx)" ]; then
	apt update
	apt install -y nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo '<html>
<head>
</head>
<body>
Hello World
</body>
</html>' | tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/^\tserver_name.*;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

service nginx restart

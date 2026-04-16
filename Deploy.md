🚀 PHASE 1 — Create Droplet (Server)
1. Go to DigitalOcean → Create Droplet

Choose:

OS: Ubuntu 24.04
Plan: $6 (1GB RAM)
Region: Singapore (or closest)
Authentication: Password (for now)

Click:
👉 Create Droplet

🌐 PHASE 2 — Connect to Server

On your PC:

ssh root@your_server_ip

Example:

ssh root@168.144.39.187
🔄 PHASE 3 — Update Server
apt update && apt upgrade -y
reboot

Reconnect after reboot:

ssh root@your_server_ip
📦 PHASE 4 — Install Required Software
apt install python3-pip python3-venv nginx mysql-server git -y

Start MySQL:

systemctl start mysql
systemctl enable mysql
🔐 PHASE 5 — Secure MySQL
mysql_secure_installation

Answers:

Validate password plugin? → n
Remove anonymous users? → y
Disallow root login remotely? → y
Remove test database? → y
Reload privilege tables? → y
🗄️ PHASE 6 — Create Database

Enter MySQL:

mysql

Run:

CREATE DATABASE myprojectdb;
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'StrongPass123!';
GRANT ALL PRIVILEGES ON myprojectdb.* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
📁 PHASE 7 — Upload Django Project
Option A: GitHub (recommended)
git clone https://github.com/your-username/your-project.git
cd your-project
Option B: Manual (zip upload)

(Skip for now unless needed)

🐍 PHASE 8 — Setup Python Environment
python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install django gunicorn mysqlclient
⚙️ PHASE 9 — Configure Django

Edit settings:

nano yourproject/settings.py
Add your server IP
ALLOWED_HOSTS = ['your_server_ip']
Configure MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myprojectdb',
        'USER': 'myuser',
        'PASSWORD': 'StrongPass123!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
🧪 PHASE 10 — Run Django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000

Open:

http://your_server_ip:8000
⚙️ PHASE 11 — Setup Gunicorn
gunicorn --bind 0.0.0.0:8000 yourproject.wsgi:application
🌐 PHASE 12 — Setup Nginx

Create config:

nano /etc/nginx/sites-available/myproject

Paste:

server {
    listen 80;
    server_name your_server_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

Enable it:

ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
nginx -t
systemctl restart nginx
🔥 PHASE 13 — Firewall
ufw allow 'Nginx Full'
ufw enable
🎉 FINAL RESULT

Open browser:

http://your_server_ip

👉 Your Django app is LIVE

🧠 WHAT YOU BUILT
Internet
   ↓
Nginx
   ↓
Gunicorn
   ↓
Django
   ↓
MySQL
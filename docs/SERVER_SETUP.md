# Настройка Ubuntu-сервера и деплой

## 1. Система и утилиты

```bash
apt update && apt upgrade -y
apt install -y curl wget git ufw fail2ban nano
```

## 2. Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

## 3. Docker Compose

```bash
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

## 4. Пользователь (не root)

```bash
adduser developer
usermod -aG sudo developer
usermod -aG docker developer
```

Дальше работать под `developer`.

## 5. Файрвол (UFW)

```bash
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 8000/tcp
echo "y" | ufw enable
ufw status
```

Порт 8000 — для приложения (или тот, что задан в `.env` как `PORT`).

## 6. Fail2ban

```bash
systemctl enable fail2ban
systemctl start fail2ban
```

## 7. Папка под проект

```bash
mkdir -p /home/developer/projects
chown developer:developer /home/developer/projects
```

## 8. Проверка

```bash
docker --version
docker-compose --version
ufw status
```

---

## Локальный запуск и деплой образа

**Локально (разработка):** в корне проекта — `cp docker-compose.override.yml.example docker-compose.override.yml`, заполнить `.env`, затем `docker-compose up -d`. Образ собирается из текущей папки, код подмонтирован.

**Сборка образа под сервер (linux/amd64) и пуш в реестр:**

```bash
docker build --platform linux/amd64 -t ghcr.io/ВЛАДЕЛЕЦ/РЕПО:latest .
docker push ghcr.io/ВЛАДЕЛЕЦ/РЕПО:latest
```

Логин в ghcr.io (если образ приватный):

```bash
echo "ТОКЕН" | docker login ghcr.io -u ЛОГИН --password-stdin
```

**На сервере:** в папке с `docker-compose.yml` и `.env` (в `.env` — `IMAGE_NAME=ghcr.io/ВЛАДЕЛЕЦ/РЕПО:latest` и остальные переменные):

```bash
docker-compose pull
docker-compose up -d
```

**Обновление на сервере:** после нового пуша в реестр с тем же тегом (`:latest` или свой) на сервере снова `docker-compose pull` и `docker-compose up -d`.

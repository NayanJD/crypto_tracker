# crypto_tracker

An crypto coin tracking application using Django, Celery and Celery beat workers.

## How to run

```
docker-compose up
```

The api would be available at http://127.0.0.1:8000

## Usage

### API

Call api like http://127.0.0.1:8000/api/prices/btc?limit=2&offset=2. It would return today's paginated price list stored in db.

Or, for a specific date, http://127.0.0.1:8000/api/prices/btc?limit=2&offset=2&date=12-01-2022. But this would return
empty result since the service was not running since 12-01-2022

### Alerting

Set `MAX_PRICE_THRESHOLD`, `MIN_PRICE_THRESHOLD` and `ALERT_EMAIL` to your choosing to get alerts accordingly.

Also, for your personal mailtrap account set below in .env:

```
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT='2525'
```

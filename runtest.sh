#!/bin/sh

docker compose exec -e DJANGO_TEST=true movies poetry run pytest --reuse-db




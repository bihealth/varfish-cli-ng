# syntax=docker/dockerfile:1.3

# ---------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------

FROM python:3.11-slim AS base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN apt-get update && apt-get install -y curl git
RUN apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/


# ---------------------------------------------------------------------------
# Dependencies
# ---------------------------------------------------------------------------

FROM base AS deps

RUN pip install -U pip pipenv
RUN apt-get update

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


# ---------------------------------------------------------------------------
# Runtime
# ---------------------------------------------------------------------------

FROM base AS runtime

ARG version_file=utils/docker/empty-file-dont-remove

COPY --from=deps /.venv /.venv

RUN mkdir /tmp/varfish-cli-ng
COPY . /tmp/varfish-cli-ng/.
RUN /.venv/bin/pip install --no-deps /tmp/varfish-cli-ng && \
    rm -rf /tmp/varfish-cli-ng

COPY utils/docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV PATH="/.venv/bin:$PATH"

# Set the entrypoint.
ENTRYPOINT ["/.venv/bin/varfish-cli"]

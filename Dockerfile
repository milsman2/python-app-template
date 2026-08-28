FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1 \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked


FROM python:3.13-slim-trixie AS runtime

# Update Debian packages to the latest security releases.
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Remove packaging tools from the runtime image.
# The application runs from /app/.venv and does not need
# system pip or setuptools.
RUN rm -rf \
    /usr/local/lib/python3.13/site-packages/pip \
    /usr/local/lib/python3.13/site-packages/pip-*.dist-info \
    /usr/local/lib/python3.13/site-packages/setuptools \
    /usr/local/lib/python3.13/site-packages/setuptools-*.dist-info

RUN groupadd --system --gid 999 nonroot \
    && useradd --system \
        --gid 999 \
        --uid 999 \
        --create-home \
        nonroot

COPY --from=builder --chown=nonroot:nonroot /app /app

ENV PATH="/app/.venv/bin:$PATH"

USER nonroot

WORKDIR /app/src

CMD ["python", "-m", "sample_python_app.main"]


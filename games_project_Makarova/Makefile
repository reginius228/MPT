.PHONY: install VD-games build package-install clean-dist

install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install ../dist/*.whl

clean-dist:
	rm -rf dist/
lint:
	uv run ruff check VD_games


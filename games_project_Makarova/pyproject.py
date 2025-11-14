[project]
name = "games-project-makarova"
version = "0.1.2"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "prompt>=0.4.1",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["VD_games"]

[dependency-groups]
dev = [
    "ruff>=0.10.5",
]

[project.scripts]
VD-games = "VD_games.scripts.VD_games:main"
VD-even = "VD_games.scripts.VD_even:play_game"
Brain-calc = "VD_games.scripts.brain.calc:play_game"
VD-gcd = "VD_games.scripts.VD_gcd:play_game"
VD-progression = "VD_games.scripts.VD_progression:main"

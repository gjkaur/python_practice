"""
Configuration loading for the Configurable Reminder CLI.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "message": "Remember to take a short break.",
    "repeat": 3,
}


def load_config(path: str) -> Dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        print(f"Warning: {path} not found, using defaults.")
        return dict(DEFAULT_CONFIG)

    try:
        text = config_path.read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Warning: failed to load config ({exc!r}), using defaults.")
        return dict(DEFAULT_CONFIG)

    config: Dict[str, Any] = dict(DEFAULT_CONFIG)
    if isinstance(data, dict):
        config.update(data)
    else:
        print("Warning: config root is not an object; using defaults.")

    if not isinstance(config.get("message"), str):
        print("Warning: config 'message' invalid; using default.")
        config["message"] = DEFAULT_CONFIG["message"]

    if not isinstance(config.get("repeat"), int) or config["repeat"] <= 0:
        print("Warning: config 'repeat' invalid; using default.")
        config["repeat"] = DEFAULT_CONFIG["repeat"]

    return config


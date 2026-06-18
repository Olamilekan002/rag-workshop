"""Notebook environment helpers (warning noise reduction)."""

from __future__ import annotations

import logging
import os
import warnings

_WARNINGS_CONFIGURED = False


def suppress_workshop_warnings() -> None:
    """Hide noisy third-party warnings for workshop notebooks."""
    global _WARNINGS_CONFIGURED
    if _WARNINGS_CONFIGURED:
        return

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=UserWarning)

    for logger_name in ("huggingface_hub", "sentence_transformers", "transformers"):
        logging.getLogger(logger_name).setLevel(logging.ERROR)

    os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
    os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")

    _WARNINGS_CONFIGURED = True

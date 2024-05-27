import logging

from discord.utils import _ColourFormatter, stream_supports_colour


def setup_logging():
    handler = logging.StreamHandler()

    if stream_supports_colour(handler.stream):
        formatter = _ColourFormatter()

    else:
        dt_fmt = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(
            "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
        )

    handler.setFormatter(formatter)

    logger = logging.getLogger("tof")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

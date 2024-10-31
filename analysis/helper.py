# These functions are used with multiprocessing. To run them in parallel in a
# Jupyter notebook, it needs to be in an importable file.
from traffic.core import Flight


def aligned_navpoint_(
    flight: Flight,
    navpoint,
    angle_precision: int = 10,
    time_precision: str = "2T",
    min_time: str = "30s",
    min_distance: int = 10,
) -> Flight:
    if aligned := flight.aligned_on_navpoint(
        navpoint, angle_precision, time_precision, min_time, min_distance
    ).next():
        return flight


def add_fuelflow(flight: Flight) -> Flight:
    try:
        return flight.fuelflow()
    except (ValueError, RuntimeError):
        return None

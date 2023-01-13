# MIT License
# (c) 2023 Andreas Motl <andreas.motl@panodata.org>
# https://github.com/earthobservations
import io
import logging
import sys
import typing as t

import numpy as np
import xarray as xr


def round_clipped(value, clipping):
    """
    https://stackoverflow.com/a/7859208
    :param value:
    :param clipping:
    :return:
    """
    return round(float(value) / clipping) * clipping


def setup_logging(level=logging.INFO):
    log_format = "%(asctime)-15s [%(name)-20s] %(levelname)-7s: %(message)s"
    logging.basicConfig(format=log_format, stream=sys.stderr, level=level)

    requests_log = logging.getLogger("botocore")
    requests_log.setLevel(logging.INFO)


def dataset_info(ds: xr.Dataset) -> str:
    buf = io.StringIO()
    ds.info(buf)
    buf.seek(0)
    return buf.read()


def is_sequence(value):
    return not isinstance(value, str) and isinstance(value, (t.Sequence, np.ndarray))


def dataset_get_data_variable_names(ds: xr.Dataset):
    return list(ds.data_vars.keys())


def dataset_without_data(ds: xr.Dataset):
    data_variables = dataset_get_data_variable_names(ds)
    return ds.drop_vars(names=data_variables)

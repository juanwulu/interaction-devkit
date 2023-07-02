"""Dataset utilities.

This module provides a set of tools for working with the INTERACTION dataset:

    - `LOCATIONS`: a list of all the available locations in the dataset.
    - `SPLITS`: a dictionary mapping dataset split to available locations.
"""
# Copyright (c) 2023, Juanwu Lu <juanwu@purdue.edu>.
# Released under the BSD-3-Clause license.
# See https://opensource.org/license/bsd-3-clause/ for licensing details.
from typing import List, Dict

LOCATIONS: List[str] = [
    "DR_CHN_Merging_ZS0",
    "DR_CHN_Merging_ZS2",
    "DR_CHN_Roundabout_LN",
    "DR_DEU_Merging_MT",
    "DR_DEU_Roundabout_OF",
    "DR_Intersection_CM",
    "DR_LaneChange_ET0",
    "DR_LaneChange_ET1",
    "DR_Merging_TR0",
    "DR_Merging_TR1",
    "DR_Roundabout_RW",
    "DR_USA_Intersection_EP0",
    "DR_USA_Intersection_EP1",
    "DR_USA_Intersection_GL",
    "DR_USA_Intersection_MA",
    "DR_USA_Roundabout_EP",
    "DR_USA_Roundabout_FT",
    "DR_USA_Roundabout_SR",
]

SPLITS: Dict[str, List[str]] = {
    "train": [
        "DR_CHN_Merging_ZS0",
        "DR_CHN_Merging_ZS2",
        "DR_CHN_Roundabout_LN",
        "DR_DEU_Merging_MT",
        "DR_DEU_Roundabout_OF",
        "DR_USA_Intersection_EP0",
        "DR_USA_Intersection_EP1",
        "DR_USA_Intersection_GL",
        "DR_USA_Intersection_MA",
        "DR_USA_Roundabout_EP",
        "DR_USA_Roundabout_FT",
        "DR_USA_Roundabout_SR",
    ],
    "val": [
        "DR_CHN_Merging_ZS0",
        "DR_CHN_Merging_ZS2",
        "DR_CHN_Roundabout_LN",
        "DR_DEU_Merging_MT",
        "DR_DEU_Roundabout_OF",
        "DR_USA_Intersection_EP0",
        "DR_USA_Intersection_EP1",
        "DR_USA_Intersection_GL",
        "DR_USA_Intersection_MA",
        "DR_USA_Roundabout_EP",
        "DR_USA_Roundabout_FT",
        "DR_USA_Roundabout_SR",
    ],
    "test_multi-agent": [
        "DR_CHN_Merging_ZS0",
        "DR_CHN_Merging_ZS2",
        "DR_DEU_Merging_MT",
        "DR_DEU_Roundabout_OF",
        "DR_Intersection_CM",
        "DR_LaneChange_ET0",
        "DR_LaneChange_ET1",
        "DR_Merging_TR0",
        "DR_Merging_TR1",
        "DR_Roundabout_RW",
        "DR_USA_Intersection_EP0",
        "DR_USA_Intersection_EP1",
        "DR_USA_Intersection_GL",
        "DR_USA_Intersection_MA",
        "DR_USA_Roundabout_EP",
        "DR_USA_Roundabout_FT",
        "DR_USA_Roundabout_SR",
    ],
    "test_single-agent": [
        "DR_CHN_Merging_ZS0",
        "DR_CHN_Merging_ZS2",
        "DR_DEU_Merging_MT",
        "DR_DEU_Roundabout_OF",
        "DR_Intersection_CM",
        "DR_LaneChange_ET0",
        "DR_LaneChange_ET1",
        "DR_Merging_TR0",
        "DR_Merging_TR1",
        "DR_Roundabout_RW",
        "DR_USA_Intersection_EP0",
        "DR_USA_Intersection_EP1",
        "DR_USA_Intersection_GL",
        "DR_USA_Intersection_MA",
        "DR_USA_Roundabout_EP",
        "DR_USA_Roundabout_FT",
        "DR_USA_Roundabout_SR",
    ],
    "test_conditional-single-agent": [
        "DR_CHN_Merging_ZS0",
        "DR_CHN_Merging_ZS2",
        "DR_DEU_Merging_MT",
        "DR_DEU_Roundabout_OF",
        "DR_Intersection_CM",
        "DR_LaneChange_ET1",
        "DR_Merging_TR0",
        "DR_Roundabout_RW",
        "DR_USA_Intersection_EP0",
        "DR_USA_Intersection_EP1",
        "DR_USA_Intersection_GL",
        "DR_USA_Intersection_MA",
        "DR_USA_Roundabout_EP",
        "DR_USA_Roundabout_FT",
        "DR_USA_Roundabout_SR",
    ],
    "test_conditional-multi-agent": [
        "DR_CHN_Merging_ZS0",
        "DR_CHN_Merging_ZS2",
        "DR_DEU_Merging_MT",
        "DR_DEU_Roundabout_OF",
        "DR_Intersection_CM",
        "DR_LaneChange_ET1",
        "DR_Merging_TR0",
        "DR_Roundabout_RW",
        "DR_USA_Intersection_EP0",
        "DR_USA_Intersection_EP1",
        "DR_USA_Intersection_GL",
        "DR_USA_Intersection_MA",
        "DR_USA_Roundabout_EP",
        "DR_USA_Roundabout_FT",
        "DR_USA_Roundabout_SR",
    ],
}

"""
Define beamline parameters for I24 with Eiger 9M detector.
"""

goniometer_axes = {
    "axes": ["omega", "sam_z", "sam_y", "sam_x"],
    "depends": [".", "omega", "sam_z", "sam_y"],
    "vectors": [(-1, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0)],
    "types": ["rotation", "translation", "translation", "translation"],
    "units": ["deg", "mm", "mm", "mm"],
    "offsets": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "starts": None,
    "ends": None,
    "increments": None,
}

eiger9M_params = {
    "mode": "images",
    "description": "Eiger 2X 9M",
    "detector_type": "Pixel",
    "sensor_material": "CdTe",
    "sensor_thickness": "0.750mm",
    "overload": 50649,  # "_dectris/countrate_correction_count_cutoff",
    "underload": -1,
    "pixel_size": ["0.075mm", "0.075mm"],
    "flatfield": "flatfield",
    "flatfield_applied": "_dectris/flatfield_correction_applied",
    "pixel_mask": "mask",
    "pixel_mask_applied": "_dectris/pixel_mask_applied",
    "image_size": [3262, 3108],  # (slow, fast)
    "axes": ["det_z"],
    "depends": ["."],
    "vectors": [0, 0, 1],
    "types": ["translation"],
    "units": ["mm"],
    "starts": None,
    "ends": None,
    "increments": None,
    "bit_depth_readout": "_dectris/bit_depth_image",
    "bit_depth_image": "_dectris/bit_depth_image",
    "detector_readout_time": "_dectris/detector_readout_time",
    "threshold_energy": "_dectris/threshold_energy",
    "software_version": "_dectris/software_version",
    "serial_number": "_dectris/detector_number",
}

eiger9M_module = {
    "fast_axis": [-1, 0, 0],
    "slow_axis": [0, -1, 0],
    "module_offset": "1",
}

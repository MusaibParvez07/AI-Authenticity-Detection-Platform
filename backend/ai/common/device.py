"""
Device Manager

This module provides a centralized way to determine the best
available device for AI inference.

Priority:
1. Apple Metal (MPS)
2. NVIDIA CUDA
3. CPU

Every AI model in the project should import DEVICE from here.
"""

import platform
import multiprocessing

import torch


# -------------------------------------------------------
# Device Selection
# -------------------------------------------------------

if torch.backends.mps.is_available():
    DEVICE = torch.device("mps")
    DEVICE_TYPE = "Apple Metal (MPS)"

elif torch.cuda.is_available():
    DEVICE = torch.device("cuda")
    DEVICE_TYPE = "NVIDIA CUDA"

else:
    DEVICE = torch.device("cpu")
    DEVICE_TYPE = "CPU"


# -------------------------------------------------------
# System Information
# -------------------------------------------------------

TORCH_VERSION = torch.__version__

PYTHON_VERSION = platform.python_version()

OPERATING_SYSTEM = (
    f"{platform.system()} {platform.release()}"
)

PROCESSOR = platform.processor()

CPU_CORES = multiprocessing.cpu_count()


# -------------------------------------------------------
# CUDA Information
# -------------------------------------------------------

CUDA_AVAILABLE = torch.cuda.is_available()

CUDA_DEVICE_NAME = (
    torch.cuda.get_device_name(0)
    if CUDA_AVAILABLE
    else None
)

CUDA_DEVICE_COUNT = (
    torch.cuda.device_count()
    if CUDA_AVAILABLE
    else 0
)


# -------------------------------------------------------
# Apple MPS Information
# -------------------------------------------------------

MPS_AVAILABLE = torch.backends.mps.is_available()


# -------------------------------------------------------
# Device Information
# -------------------------------------------------------

def get_device_info() -> dict:
    """
    Returns detailed runtime information
    about the current AI device.
    """

    return {

        "device": str(DEVICE),

        "device_type": DEVICE_TYPE,

        "torch_version": TORCH_VERSION,

        "python_version": PYTHON_VERSION,

        "operating_system": OPERATING_SYSTEM,

        "processor": PROCESSOR,

        "cpu_cores": CPU_CORES,

        "cuda_available": CUDA_AVAILABLE,

        "cuda_device_name": CUDA_DEVICE_NAME,

        "cuda_device_count": CUDA_DEVICE_COUNT,

        "mps_available": MPS_AVAILABLE,

    }


# -------------------------------------------------------
# Print Device (Optional)
# -------------------------------------------------------

def print_device_info() -> None:
    """
    Prints device information
    in a readable format.
    """

    info = get_device_info()

    print("\n========== AI DEVICE ==========")

    for key, value in info.items():

        print(f"{key}: {value}")

    print("===============================\n")
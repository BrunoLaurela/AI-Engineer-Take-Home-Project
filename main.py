"""
Sports Motion Detection Script
------------------------------

This script detects motion in a sports video by:
1. Extracting frames from the video.
2. Identifying motion areas using frame differencing.
3. Visualizing motion with bounding boxes and saving results.

Usage:
------
Run the script from the command line:

    python main.py --video input.mp4 --output results --fps 5

Arguments:
----------
--video  : Path to the input video file (required).
--output : Directory to save results (default: 'output').
--fps    : Frames per second for processing (default: 5).

Dependencies:
-------------
- OpenCV (cv2)
- NumPy
- argparse
- frame_processor.py
- motion_detector.py
- visualizer.py

Author:
-------
Bruno Laurela Lunelli
Date: March 2025
"""

import os
import argparse
import cv2
import numpy as np

from frame_processor import process_video
from motion_detector import detect_motion
from visualizer import visualize_results


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Sports Motion Detection")
    parser.add_argument(
        "--video", type=str, required=True, help="Path to input video file"
    )
    parser.add_argument("--output", type=str, default="output", help="Output directory")
    parser.add_argument("--fps", type=int, default=5, help="Target frames per second")
    return parser.parse_args()


def main():
    """Main function to run the motion detection pipeline."""
    # Parse arguments
    args = parse_args()

    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)

    print(f"Processing video: {args.video}")

    # Step 1: Extract frames from video
    frames = process_video(args.video, args.fps)
    print(f"Extracted {len(frames)} frames")

    # Step 2: Detect motion in frames
    motion_results = []
    for i, frame in enumerate(frames):
        print(f"Processing frame {i + 1}/{len(frames)}")

        # Pass the entire frames list and the current index to detect_motion
        # This allows the function to access both current and previous frames
        # for frame comparison and motion detection
        motion_boxes = detect_motion(frames, i)
        motion_results.append(motion_boxes)

    # Step 3: Visualize and save results
    visualize_results(frames, motion_results, args.output)

    print(f"Processing complete. Results saved to {args.output}")


if __name__ == "__main__":
    main()





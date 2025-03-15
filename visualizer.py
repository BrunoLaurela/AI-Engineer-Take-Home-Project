
import os
import cv2
import numpy as np


def visualize_results(frames, motion_results, output_dir):
    """
    Create visualization of motion detection results.

    Args:
        frames: List of video frames
        motion_results: List of motion detection results for each frame
        output_dir: Directory to save visualization results
    """
    # Create output directory for frames
    frames_dir = os.path.join(output_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)

    # Get dimensions for the output video
    height, width = frames[0].shape[:2]

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_path = os.path.join(output_dir, "motion_detection.mp4")
    video_writer = cv2.VideoWriter(video_path, fourcc, 5, (width, height))

    # TODO: Implement visualization
    # 1. Process each frame
    #    a. Create a copy of the frame for visualization
    #    b. Skip motion drawing for the first frame (it has no motion data)
    #    c. For subsequent frames, draw bounding boxes around motion regions
    #       (hint: cv2.rectangle with green color (0, 255, 0))
    #    d. Add frame number to the visualization (hint: cv2.putText)
    #    e. Save each visualization frame as an image
    #    f. Write each frame to the video writer
    # 2. Release the video writer when done

  
    # Process each frame
    for i, frame in enumerate(frames):
        # Create a copy of the frame for visualization
        vis_frame = frame.copy()

        # Draw bounding boxes around detected motion regions
        if motion_results[i]:  # Ensure there is motion data for the frame
            for (x, y, w, h) in motion_results[i]:
                # Draw bounding box around the detected motion (green color)
                cv2.rectangle(vis_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Add the original frame to the visualization
        original_frame_with_text = frame.copy()
        cv2.putText(original_frame_with_text, f"Frame {i+1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Stack original frame and visualized frame for side-by-side comparison
        stacked_frame = np.hstack((original_frame_with_text, vis_frame))

        # Add frame number to the visualization (on the original frame)
        cv2.putText(stacked_frame, f"Frame {i+1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Save each visualization frame as an image
        frame_filename = os.path.join(frames_dir, f"frame_{i+1}.jpg")
        cv2.imwrite(frame_filename, stacked_frame)

        # Write each frame to the video writer
        video_writer.write(stacked_frame)

    # Release the video writer when done
    video_writer.release()

    print(f"Visualization saved to {video_path}")
    print(f"Individual frames saved to {frames_dir}")
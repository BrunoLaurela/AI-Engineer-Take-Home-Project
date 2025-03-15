# Sports Motion Detection - README

## Description

This script detects motion in a sports video by analyzing differences between consecutive frames. Frames are extracted at a specific frame rate, pixel differences are analyzed, and regions with significant movement are highlighted.

## Instalación y Dependencias

Make sure you have the following Python libraries installed before running the script:

```bash
pip install opencv-python numpy
```

## Uso

Run the script from the command line, specifying the input video path and output directory:

```bash
python sports_motion_detection.py --video ruta/al/video.mp4 --output ruta/al/directorio/salida --fps 5
```

### Parameters
--video: Path to the input video file.
--output: Directory where the results (processed images and motion-detection video) will be saved.
--fps: Number of frames per second to extract from the video (default: 5).

## Explicación de Decisiones de Diseño

1. **Frame Extraction:**

   - Frames are extracted at a specific frequency to reduce unnecessary processing and focus on relevant changes.

2. **Image Preprocessing:**

   - Frames are converted to grayscale, and a Gaussian filter is applied to reduce noise.

3. **Motion Detection:**

   - the absolute difference between consecutive frames is computed and thresholded to identify significant changes.
   - Contours with a minimum area are filtered to avoid false detections.

4. **Result Visualization:**

   - Rectangles are drawn around motion areas, and an output video with the detections is generated.

## Salida
- A folder containing processed frame images.
- A motion_detection.mp4 video with highlighted detections.

## Consideraciones

- Ajuste `--fps` para mejorar el rendimiento o capturar más detalles del movimiento.
- Modify the `threshold` and `min_area` values in `detect_motion` to fine-tune motion detection based on the analyzed sport.

## Challenges
The challenges presented were detecting the players who are farther away and detecting each player in motion as an independent square.

To better detect the distant players, some parameters were adjusted.
-  First, I tried using smaller Gaussian filter kernels. This way, it would better recognize the details. 
- Then, I tested lower detection thresholds.

In addition, to separate the players into different boxes, I tried performing an erosion followed by dilation, but this didn't work. The best option was to reduce the minimum area that was detected.


Another challenge was that, on some occasions, things that were not moving on the grass were detected


## Simple ideas for future improvements
I would recommend adjusting the detection threshold dynamically based on the distance to the camera. For distant players, lowering the threshold would help detect more subtle movements. Additionally, optimizing parameters based on the scale of the player or object in the frame could improve detection accuracy.

To address static objects like the grass, using background subtraction techniques or a background model can help differentiate between moving players and the stationary ground. If the field is flat, applying geometric transformations could further improve the detection by focusing on areas where player movement is expected, reducing the chance of detecting the grass as moving.
## Autor

Bruno Laurela




# analyse video for text

 Toolset to find given text in a video

Warning: this is something I made for my own purposes, you might find it useful, you might not.

## Usage

You can call the main.py script, everything is done for you.

```powershell
python main.py --video myvideo.mp4 --text "my spaghet"
```

Or, you can use the individual scripts:

```powershell
python actions\extract_frames_from_video.py --video video.mp4 --output frames
python actions\ocr_scan_image.py --input frames --output ocr
python actions\find_text_in_files.py --input ocr --text "my spaghet"
```

I've not bothered to parallelise the processing, so it's not very fast on large videos.

import click
import os

from actions.extract_frames_from_video import extract_frames_from_video
from actions.ocr_scan_image import ocr_scan_image
from actions.find_text_in_files import find_text_in_files

@click.command()
@click.argument("--video", "--video_filepath", type=str, required=True)
@click.argument("--text", "--target_text", type=str, required=True)
def main(video_filepath, target_text):
	extract_frames_from_video(video_filepath, "frames", 120)

	for filename in os.listdir("frames"):
		ocr_scan_image(f"frames/{filename}", "ocr")

	found_matches = find_text_in_files(target_text, "ocr", True)
	print(f"Found {len(found_matches)} matches: {found_matches}")

if __name__ == "__main__":
	main()

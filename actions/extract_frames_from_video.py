import cv2

def extract_frames_from_video(video_filepath, output_directory: str, frame_divisor=1):
	cap = cv2.VideoCapture(video_filepath)
	frame_count = 0
	while cap.isOpened():
		ret, frame = cap.read()
		if ret:
			if frame_count % frame_divisor == 0:
				cv2.imwrite(f"{output_directory}/{video_filepath}-{frame_count}.jpg", frame)
			frame_count += 1
		else:
			break
	cap.release()

if __name__ == "__main__":
	import click

	@click.command()
	@click.option("--video_filepath", "--video", required=True, type=str)
	@click.option("--output_directory", "--output", required=True, type=str)
	@click.option("--frame_divisor", "--divisor", default=1, type=int)
	def main(video_filepath, output_directory, frame_divisor):
		extract_frames_from_video(video_filepath, output_directory, frame_divisor)

	main()

import pytesseract
from PIL import Image
import os

def ocr_scan_image(image_filepath, output_directory: str, override=False):
	image_filename = os.path.basename(image_filepath)

	if os.path.exists(f"{output_directory}/{image_filename}.txt") and not override:
		return

	image = Image.open(image_filepath)
	image_text = pytesseract.image_to_string(image)
	
	with open(f"{output_directory}/{image_filename}.txt", "w") as file:
		file.write(image_text)

if __name__ == "__main__":
	import click

	@click.command()
	@click.option("--image_filepath", "--image", type=str)
	@click.option("--input_directory", "--input", type=str)
	@click.option("--output_directory", "--output", required=True, type=str)
	def main(image_filepath, input_directory, output_directory):
		assert ((image_filepath is not None) ^ (input_directory is not None)), "image_filepath and input_directory are mutually exclusive"

		if image_filepath:
			ocr_scan_image(image_filepath, output_directory)
		
		if input_directory:
			for image_filepath in os.listdir(input_directory):
				ocr_scan_image(f"{input_directory}/{image_filepath}", output_directory)
	
	main()

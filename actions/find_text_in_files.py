import os

def in_validator(target_text):
	def validator(text):
		return target_text in text
	
	return validator

def find_text_in_files(target_text, input_directory, stop_on_first_match=False):
	found_matches = []

	validator = in_validator(target_text)

	for filename in os.listdir(input_directory):
		with open(f"{input_directory}/{filename}", "r") as file:
			file_text = file.read()

			if validator(file_text):
				print(f"'{filename}' contains '{target_text}'")
				found_matches.append(filename)

				if stop_on_first_match:
					return
				
	return found_matches

if __name__ == "__main__":
	import click

	@click.command()
	@click.option("--target_text", "--text", type=str)
	@click.option("--input_directory", "--input", type=str)
	def main(target_text, input_directory):
		found_matches = find_text_in_files(target_text, input_directory)
		print(f"Found {len(found_matches)} matches: {found_matches}")
	
	main()

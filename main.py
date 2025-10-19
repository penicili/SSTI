import os
import secrets


# This script generates a CTF flag and writes it into ./flag/flag.txt
def generate_flag():
	token = secrets.token_hex(12)
	flag = f"CTF{{{token}}}"
	return flag


def write_flag_to_file(flag, folder='flag', filename='flag.txt'):
	os.makedirs(folder, exist_ok=True)
	path = os.path.join(folder, filename)
	with open(path, 'w', encoding='utf-8') as f:
		f.write(flag + "\n")
	return path


if __name__ == '__main__':
	flag = generate_flag()
	path = write_flag_to_file(flag)
	print(f"Generated flag: {flag}")
	print(f"Flag written to: {path}")
	print()
	print("Next steps:")
	print("  1) Build the Docker image: docker build -t ctf-proto .")
	print("  2) Run the container: docker run --rm -p 5000:5000 ctf-proto")
import os

def merge_js_files(output_filename="merged_js_scripts.txt"):
    # Open the output file in write mode
    with open(output_filename, "w") as outfile:
        # Iterate over all files in the current directory
        for filename in os.listdir("."):
            # Check if the file is a JavaScript file
            if filename.endswith(".js"):
                # Write the filename as a header
                outfile.write(f"\n\n--- {filename} ---\n\n")
                # Read and write the content of the JavaScript file
                with open(filename, "r") as infile:
                    outfile.write(infile.read())
                outfile.write("\n")  # Add a newline after each file

if __name__ == "__main__":
    merge_js_files()

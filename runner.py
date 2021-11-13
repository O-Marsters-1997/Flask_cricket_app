# Just for testing sass compilation

import sass

# Map scss source files to css destination files
sass_map = {"static/scss/style.scss": "static/style.css"}


def compile_sass_to_css(sass_map):

    print("Compiling scss to css:")

    for source, dest in sass_map.items():
        with open(dest, "w") as outfile:
            outfile.write(sass.compile(filename=source))
        print(f"{source} compiled to {dest}")


if __name__ == "__main__":
    print()
    print("Starting runner")
    print("--------------------")
    compile_sass_to_css(sass_map)
    print("--------------------")

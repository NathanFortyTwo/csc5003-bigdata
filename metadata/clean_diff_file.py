def main():
    with open("diff.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    # remove all spaces
    lines = [line.replace(" ", "") for line in lines]
    # if 2 lines are the same, remove both of them
    lines = list(set(lines))
    # if 2 consecutive lines start with @ remove the first
    i = 0
    while i < len(lines) - 1:
        if lines[i].startswith("@") and lines[i + 1].startswith("@"):
            lines.pop(i)
        else:
            i += 1

    # write to file
    with open("cleaned_diff.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()

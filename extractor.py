# modified date 10-28-2019
# added check for reference directory with destination directory

import re
import os


def extract(chapter, chapter_footnotes):
    remove_pattern = r'[\*]{3}[^\*]*[\*]{3}'

    split = re.split(remove_pattern, chapter)

    recombined = ""
    for x in range(len(split)):
        recombined = recombined + split[x]

    verses = re.split(r'[0-9]+', recombined)

    if len(verses) > 0:
        current_verse = 0
        extracted_text = ""
        delimiter = "*"
        for verse in verses:
            if re.search(r'\w', verse):
                current_verse = current_verse + 1

                # remove new lines
                compact_verse = verse.replace("\n", "")

                extracted_text = extracted_text + str(current_verse) + delimiter + compact_verse
                # check if there is/ are footnotes
                footnote_pattern = r'\[[a-z]\]'
                footnotes = re.findall(footnote_pattern, compact_verse)

                if len(footnotes) > 0:
                    extracted_text = extracted_text + delimiter
                    for footnote in footnotes:
                        matched_footnote = ""
                        for fn in chapter_footnotes:
                            if fn.startswith(footnote[1:2] + "."):
                                if fn.endswith("\n"):
                                    fn = fn[:-2]

                                matched_footnote = fn
                                break

                        if matched_footnote == "":
                            print("Verse {}. No footnote matched for {}".format(current_verse, footnote))
                        else:
                            extracted_text = extracted_text + matched_footnote + ";"

                # make sure to end with new line
                extracted_text = extracted_text + "\n"

        return extracted_text

    return None


def main():
    destination_folder_name = "ExtractedBibleVersions"

    print("Input references folder to be extracted:")
    reference_path = input("Enter Bible versions directory:\n")

    destination_base_path = input("Input destination folder of extracted files:\n")

    if destination_base_path.startswith(reference_path):
        print("Destination directory should not the same nor inside the sub-directory of reference directory.")
        print("Please change the directory.")
        return

    # get version paths
    bible_version_paths = [p for p in os.listdir(reference_path)
                           if os.path.isdir(reference_path + "\\" + p)]
    print(bible_version_paths)
    print("Found {0} versions.".format(str(len(bible_version_paths))))
    # for version in bible_version_paths:
    #     print(version)

    for version in bible_version_paths:
        print("extracting {0}...".format(version))
        print("checking books for {0} version...".format(version))
        version_dir = reference_path + "\\" + version
        books = [p for p in os.listdir(version_dir)
                 if os.path.isdir(version_dir + "\\" + p)]
        print("found {0} books for {1}".format(str(len(books)), version))
        for book in books:
            print("checking chapters for book of {0}...".format(book))
            book_dir = version_dir + "\\" + book
            book_directories_item = os.listdir(book_dir)
            chapters = [f for f in book_directories_item
                        if os.path.isfile(book_dir + "\\" + f)]

            # get footnotes
            footnote_path = [p for p in book_directories_item
                             if os.path.isdir(book_dir + "\\" + p)]

            # print("footnote_path {}".format(footnote_path))
            footnote_files = []
            if len(footnote_path) > 0:
                footnote_files = [f for f in os.listdir(book_dir + "\\" + footnote_path[0])
                                  if os.path.isfile(book_dir + "\\" + footnote_path[0] + "\\" + f)]

            try:
                os.makedirs(destination_base_path + "\\" + destination_folder_name + "\\" + version + "\\" + book)
            except Exception as e:
                print(e)
                print("Error in creation of directory")
                if not str(e).find("file already exist"):
                    return

            print("Found {0} chapters for book of {1}.".format(str(len(chapters)), book))

            chapter_footnotes_filename = ""
            book_name = book.replace("_raw", "")
            chapter_footnote_files = [f for f in footnote_files
                                      if f.startswith(book_name)]
            current_chapter = 0
            for chapter in chapters:
                current_chapter = current_chapter + 1
                print("extracting chapter {}...".format(current_chapter))
                reference_chapter_filename = book_dir + "\\" + chapter
                destination_full_path = destination_base_path + "\\" + destination_folder_name + "\\" + version + "\\" + book
                extracted_content = ""
                # print(chapter_footnote_files)
                if len(chapter_footnote_files) > 0:
                    footnote_chapter_pattern = r'Chapter{}'.format(current_chapter)
                    # print(footnote_chapter_pattern)
                    for fn in chapter_footnote_files:
                        if re.search(footnote_chapter_pattern, fn):
                            chapter_footnotes_filename = fn

                chapter_footnotes_full_path = "" if len(footnote_path) == 0 else book_dir + "\\" + footnote_path[
                    0] + "\\" + chapter_footnotes_filename
                chapter_footnotes = []
                if chapter_footnotes_filename is not "":
                    try:
                        with open(chapter_footnotes_full_path, 'r') as f:
                            # print("footnote full filename {}".format(chapter_footnotes_full_path))
                            chapter_footnotes = f.readlines()
                            # print(chapter_footnotes)
                    except Exception as e:
                        print("Error reading footnotes {}".format(e))

                try:
                    with open(reference_chapter_filename, "r") as f:
                        content = f.read()
                        extracted_content = extract(content, chapter_footnotes)
                except Exception as e:
                    print(e)
                    print("Error in reading and extracting file.")
                    print("Corrupted content")
                    return

                if content is not None:
                    with open(
                            destination_full_path + "\\" + "Extracted" + chapter,
                            "w") as f:
                        f.write(extracted_content)


if __name__ == '__main__':
    main()

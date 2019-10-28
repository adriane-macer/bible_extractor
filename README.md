# bible_extractor
This extracts the verses from files.

Make sure that the reference directory to be extracted has the structured as this:

    <ReferenceFolder>
        |
         - <Version 1 Dir> eg. NRSV
            |
              - <Book 1 Dir>
                |
                  - <Chapter 1 file>  (filename must be end with "_raw.txt") eg. NRSVGenesisChapter1_raw.txt
                  - <Chapter 2 file>  (filename must be end with "_raw.txt")
                  - <Chapter 3 file>  (filename must be end with "_raw.txt")
                  .
                  .
                  .
                  - <Chapter <nth> file> (filename must be end with "_raw.txt")
                  - <Book footnotes Dir>
                    |
                      - <Chapter footnotes file> eg. NRSVGenesisFootnotes.txt
                <Book 2 Dir> eg. Exodus
                |
                  - <Chapter 1 file>  (filename must be end with "_raw.txt") eg. NRSVExodusChapter1_raw.txt
                  - <Chapter 2 file>  (filename must be end with "_raw.txt")
                  - <Chapter 3 file>  (filename must be end with "_raw.txt")
                  .
                  .
                  .
                  - <Chapter <nth> file> (filename must be end with "_raw.txt")
                  - <Book footnotes Dir>
                    |
                      - <Chapter footnotes file> eg. NRSVExodusFootnotes.txt
        |
         - <Version 2 Dir> eg. KJV
            |
              - <Book 1 Dir>
                |
                  - <Chapter 1 file>  (filename must be end with "_raw.txt") eg. NRSVGenesisChapter1_raw.txt
                  - <Chapter 2 file>  (filename must be end with "_raw.txt")
                  - <Chapter 3 file>  (filename must be end with "_raw.txt")
                  .
                  .
                  .
                  - <Chapter <nth> file> (filename must be end with "_raw.txt")
                  - <Book footnotes Dir>
                    |
                      - <Chapter footnotes file> eg. KJVGenesisFootnotes.txt
                <Book 2 Dir> eg. Exodus
                |
                  - <Chapter 1 file>  (filename must be end with "_raw.txt") eg. KJVExodusChapter1_raw.txt
                  - <Chapter 2 file>  (filename must be end with "_raw.txt")
                  - <Chapter 3 file>  (filename must be end with "_raw.txt")
                  .
                  .
                  .
                  - <Chapter <nth> file> (filename must be end with "_raw.txt")
                  - <Book footnotes Dir>
                    |
                      - <Chapter footnotes file> eg. KJVExodusFootnotes.txt
        .
        .
        .
        <Other versions>

# Say, Wizard!

Press shortcut keys to have your Mac read aloud phrases from a text file.

Designed for running a Wizard of Oz voice interface test on OSX using `say`.

## Instructions

Download and unzip this script to your Mac.

Edit the text file `script.txt` in the unzipped `saywizard` folder with your phrases.

- Newlines will not affect the number of keys you need to use.
- You can add comments by starting lines with "#"

Double-click `startSayWizard.command` to run a test. 

- If Mac security settings prevent this, right-click on it, Choose: Open With > Terminal, and click Open. You can also add executable permissions to the file with `chmod u+x startSayWizard.command` or right-click --> Get Info --> Sharing & Permissions.

Press the relevant key to have your Mac say your phrases. 

- If you make changes to `script.txt` while Say Wizard is running, you can press the reload key ("!") to refresh the script without ending Say Wizard. 
- To quit, you can hit the exit key ("~"), use Ctrl+C, or close the window.
- All keys can be added, deleted, and edited in `wizardofoz.py`, including the reload and exit keys.

Written by @bensauer. Hat-tip to @jonesabi at Google for the idea. 

mkdir script
cd script/
su
vim err.txt
i
error
:wq
cat err.txt
grep -iRl "error" /home/user/script
(доп -n - показать номер строки, в которой находится фраза; -w - показать место, где слово попадается;)
vim scriptdelete.sh

#!/bin/bash
find -type f -exec grep -q error {} \; -delete
cat scriptdelete.sh
bash ./scriptdelete.sh
sudo chmod +x scripterror.sh (Что бы сделать скрипт исполняемым, нужно или установить спец флаг в разрешениях файла)
ls -la
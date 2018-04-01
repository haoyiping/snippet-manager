date '+%Y-%m-%d %H:%M:%S' // 2018-03-16 11:01:57

date -r 1234567890                                          # *BSD
date -d @1234567890                                         # Linux
date -d '1970-01-01 UTC + 1234567890 seconds'               # old GNU
perl -le 'print scalar localtime $ARGV[0]' 1234567890       # cross platform

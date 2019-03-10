#!/bin/sh
# usage: gbk2utf8.sh <cat|more|less> <file>

PROGNAME=`basename $0`
if [ $# -lt 2 ]; then
    echo "Usage: $PROGNAME <cat|more|less> <file>"
    exit;
fi

encode=`file $2`
test=${encode/UTF-8/}

if [ "$encode" = "$test" ]
then
    # gbk
    iconv -f gbk -t utf-8 $2 | $1
else
    # utf8
    $1 $2
fi

#自动转换GBK编码文件为UTF8编码，用于封装cat，more，less等工具
#Usage: gbk2utf8.sh {cat|more|less} {file}
#!/bin/bash
for fastq in `find ./ -name \*.fastq`; do
  python -m kvarq.cli -d show "$fastq" 2>"$0_error.log"
  err="$?"
  echo $err $fastq
  if [ $err -ne 0 ]; then
    # file format error
    base=`basename "$fastq"`
    mv "$0_error.log" "${base%.fastq}.log"
  fi
done
rm "$0_error.log"

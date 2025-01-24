#!/bin/bash

# Ստեղծել թղթապանակ վերականգնման համար
mkdir -p restored_blobs

echo "Վերականգնվում են dangling blob-երը..."

# Վերականգնել բոլոր dangling blob-երը
for blob in $(git fsck --lost-found | grep "dangling blob" | awk '{print $3}'); do
    echo "Վերականգնվում է blob $blob..."
    git show $blob > restored_blobs/$blob.txt
done

# Բոլոր ֆայլերը համատեղել մեկ ֆայլի մեջ
echo "Համատեղվում են բոլոր blob-երը..."
cat restored_blobs/*.txt > combined_recovery.txt

echo "Վերականգնումը ավարտված է։ Ստուգիր combined_recovery.txt ֆայլը կամ restored_blobs թղթապանակը։"

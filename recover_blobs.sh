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

# Փոխարկել blob-երի բովանդակությունը ճիշտ տեղ
mv restored_blobs/*.txt  # Պատահական օրինակ

# Ավելացնել դրանք Git-ում
git add .

# Կատարել նոր commit
git commit -m "Recovered lost changes"
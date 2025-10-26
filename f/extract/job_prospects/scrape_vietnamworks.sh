for i in {2..180}; do
    scrapy crawl vietnamworks -o $(date +%Y-%m-%d)_vietnamworks_$i.json -a i=$i
done

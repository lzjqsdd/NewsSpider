#!/bin/bash

echo "Start Crawl..."
cd tools
python Init.py
echo "Init File Done."
cd ../news_spider
scrapy crawlall
echo "Crawl Data Done."
cd ../tools
python preprocess.py
cd ../web
python main.py 1111

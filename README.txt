
1. save yours targets in domains.txt

2. cat check_domains.txt | python3 crawler.py -d 10 > crawl_results.txt

3. Open crawl_results.txt, this file with results.

4. nuclei -l crawl_results.txt -t nuclei-templates/http/vulnerabilities/

5. lostools+crawl_results.txt

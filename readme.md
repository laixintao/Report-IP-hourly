## useage
	git clone https://github.com/laixintao/Report-IP-hourly.git /root/rootcrons/
	mv /root/rootcrons/Report-IP-hourly/report-ip.py /root/rootcrons/reportip.py
	mv /root/Report-IP-hourly/rootcron /root/rootcrons/rootcron
	touch /root/rootcrons/lastip.txt
	rm -rf /root/rootcrons/Report-IP-hourly/
	crontab /root/rootcrons/rootcron
	/etc/init.d/cron restart
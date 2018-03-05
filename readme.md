# Report your IP to email hourly

This script could report ip to your email houly(or minutely,depent on your settings).

Use this script you could make your RaspberryPI a vps.Once you get the ip, you can use ssh to login.

## GUIDE

[中文指南](http://www.kawabangga.com/posts/1398) 

## usage
	git clone https://github.com/laixintao/Report-IP-hourly.git /root/rootcrons/
	# change your e-mail config
	# ..............done
	crontab /root/rootcrons/rootcron
	/etc/init.d/cron restart
	
## Notice

The email config should be settings,**DO NOT** leave anything about your real e-mail on github,commit or PR .

## License

	The MIT License (MIT)
	
	Copyright (c) 2015 Viktor Arsovski
	
	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:
	
	The above copyright notice and this permission notice shall be included in
	all copies or substantial portions of the Software.
	
	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
	THE SOFTWARE.

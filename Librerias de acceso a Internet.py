import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line: # Buscamos la hora del este
        print line

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@ejemplo.org', 'jcaesar@ejemplo.org',
                """To: jcaesar@ejemplo.org
                From: soothsayer@ejemplo.org

                Ojo al piojo.
                """)
server.quit()

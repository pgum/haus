from sh import ssmtp, echo
import urllib2
import mypasswords as mp
import xmltodict

class GmailTalker():
    def __init__(self):
        self._user='ditto.borg'
        self._passwd= mp.getDittoBorgMailPasswd()

    def getMails(self):
        auth_handler = urllib2.HTTPBasicAuthHandler()
        auth_handler.add_password(
            realm='mail.google.com',
            uri='https://mail.google.com',
            user='%s@gmail.com' % self._user,
            passwd=self._passwd
        )
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        feed = urllib2.urlopen('https://mail.google.com/mail/feed/atom')
        xml_from_feed= feed.read()
        untangled= xmltodict.parse(xml_from_feed)

        return untangled

    def sendMail(self,message):
        msg="From: " + self._user + "\nSubject: Borg-mail\n" + message
        ssmtp("killmepl@gmail.com", _in=echo(msg))


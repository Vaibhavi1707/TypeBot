import random
import webbrowser
import wikipedia
from datetime import * 
import pyowm
def run(inst):
	owm=pyowm.OWM('11174303549c909a9c5094d4f4872157')
	bangalore=owm.three_hours_forecast('Bengaluru, India')
	greetings=['hello','hi, there','hey','hi','heyy','heyyy, there','heyyyyyyyyy','hellliiioooo','hellllloooooo','hiiiii','hii',
	'helllllloooo','hello there','heyyy there']
	howdy=['how are you?','how you doin?','hbu','you fine?','how r u','how r u?']
	answers=['i am fine','i am good','okay','i m 5n','i m fyn','i m gud']
	creator=['who created you','who made you','who made you?','who created you?','kisne banaya teko']
	cmd_jokes=['tell me a joke','make me laugh','jokes']
	youtube=['open youtube','want to watch a video','youtube']
	primevideo=['i wanna binge watch','open amazon prime','amazon prime']
	netflix=['put netflix','open netflix','netflix']
	zee5=['put zee5','open zee5','zee5']
	hotstar=['put hotstar','open hotstar','hotstar']
	cmd_web=['open google','connect to the web','google']
	jokes=['Why is advanced math to be taken easy?......because it is as easy as pi','Why did the scarecrow get an award?....He was outstanding in his field'
	,'What do you give a sick lemon?......lemon-aid']
	bye=['bye','bye....talk to you later','Happy to have helped you','byeeeee']
	cmd_date=['what is the date today',"what's the date today",'date',"what's the date today?",'what is the date today?']
	cmd_time=["what's the time",'what is the time','time','tell me the time',"what's the time?",'what is the time?']
	cmd_weather=['weather',"will it rain?","will it rain",'how is the weather?','how is the weather','how is the weather today','how is the weather today?']
	if (inst in greetings):
		r_greet=random.choice(greetings)
		return r_greet
	elif inst in howdy:
		r_ans=random.choice(answers)
		r_q=random.choice(howdy)
		return r_ans+' '+r_q
	elif inst in cmd_date:
		return "Today's date is"+' '+datetime.today().strftime("%d.%m.%Y")
	elif inst in cmd_time:
		return "The time is"+' '+datetime.now().strftime("%H:%M:%S")
	elif inst in creator:
		return 'I was made by Vaibhavi'
	elif inst in cmd_jokes:
		r_jokes=random.choice(jokes)
		return r_jokes
	elif inst in cmd_weather:
		blr=owm.weather_at_place('Bengaluru, India')
		wea=blr.get_weather()
		if(bangalore.will_have_rain()):
			return 'It will rain today.'+'Temperature is '+str(wea.get_temperature('celsius')['temp'])+' '+'celsius.'
		else:
			return 'It will not rain today.'+'Temperature is '+str(wea.get_temperature('celsius')['temp'])+' '+'celsius.'
	elif inst in cmd_web:
		return "Opened Google"
		webbrowser.open("https://www.google.com/")
	elif inst in youtube:
		webbrowser.open("https://www.youtube.com/")
		return "Here, I have opened Youtube"
	elif inst in netflix:
		webbrowser.open("https://www.netflix.com/")
		return "Here, I have opened Netflix"
	elif inst in hotstar:
		webbrowser.open("https://www.hotstar.com/")
		return "Here, I have opened Hotstar"
	elif inst in zee5:
		webbrowser.open("https://www.zee5.com/")
		return "Here, I have opened ZEE5"
	elif inst in primevideo:
		webbrowser.open("https://www.primevideo.com/")
		return "Here,I have opened Amazon Prime Video...Login and enjoy your binge"
	elif inst=='wish jahanvi a happy birthday':
		return "HAPPY BIRTHDAY JAHANVI"
		webbrowser.open("https://www.youtube.com/watch?v=bV2GklFBaT8")
	else:
		return"Please Wait"+' '+wikipedia.summary(inst)
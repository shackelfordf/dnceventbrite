from eventbrite import Eventbrite  
#eventbrite = Eventbrite ('F7T2P7A27KSJCPDD6RHL')
eventbrite = Eventbrite ('BGRKOZMNI6NQRUNPD6BZ')

#event details

user = eventbrite.get_user()						#name of the eventbrite user 
#print user

userId = user['id']
#print userId

userEvents = '/users/'+ userId + '/owned_events/'
#print userEvents

print eventbrite.get(userEvents)


eventName = userEvents['multipart-text'] 			#event name

eventOrganizer = userEvents['organizer']			#organizer of the event

eventUrl = userEvents['url']						#event posting url 

eventDate = userEvents['datetime-tz']				#event time 

eventOrganizer = userEvents['organizer']			#organizer of the event





"""
organizerAllEvents = eventbrite.get_event()			#organizer of the id
print (organizerAllEvents['organizer.id'])



eventDate = eventbrite.get_event()					#event time 
print (eventName['datetime-tz']) 

eventLocation = eventbrite.get_venue()				#event address 
print (eventLocation['address'])



eventAttendees = eventbrite.get_order()				#list of event attendees
print (eventAttendees['attendee'])


#attendee details 
attendeeName =  eventbrite.get_attendee()		#attendee name 
print (attendeeFirstName['name'])

attendeeEmail = eventbrite.get_attendee()
print (attendeeFirstName['email'])

attendeePhone = eventbrite.get_attendee()
print (attendeePhone['cell_phone'])

attendeeAddress = eventbrite.get_attendee()
print (attendeeAddress['address'])

attendeeEvent = eventbrite.get_attendee()
print (attendeeEvent['event_id'])




#price details 

"""






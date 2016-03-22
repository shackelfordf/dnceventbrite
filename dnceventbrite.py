from eventbrite import Eventbrite  
eventbrite = Eventbrite ('F7T2P7A27KSJCPDD6RHL')

#event details
eventName = eventbrite.get_event()
print (eventName['multipart-text']) 

eventOrganizer = eventbrite.get_event()
print (eventOrganizer['organizer']) 

eventUrl = eventbrite.get_event()
print (eventUrl ['url'])

eventDate = eventbrite.get_event()
print (eventName['datetime-tz']) 

eventLocation = eventbrite.get_venue()
print (eventLocation['address'])






#attendee details 
attendeeFirstName =  eventbrite.get_attendee()
print (attendeeFirstName['first_name'])

attendeeLastName =  eventbrite.get_attendee()
print (attendeeLastName['last_name'])

attendeeEmail = eventbrite.get_attendee()
print (attendeeFirstName['email'])

attendeePhone = eventbrite.get_attendee()
print (attendeePhone['cell_phone'])

attendeeAddress = eventbrite.get_attendee()
print (attendeeAddress['address'])

attendeeEvent = eventbrite.get_attendee()
print (attendeeEvent['event_id'])


#price details 






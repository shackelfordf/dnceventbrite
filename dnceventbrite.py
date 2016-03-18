from eventbrite import Eventbrite  
eventbrite = Eventbrite ('F7T2P7A27KSJCPDD6RHL')

#event details
eventName = eventbrite.get_event()
print (eventName['multipart-text']) 

eventDate = eventbrite.get_event()
print (eventName['datetime-tz']) 

eventOrganizer = eventbrite.get_event()
print (eventOrganizer['organizer']) 

eventLocation = eventbrite.get_venue()
print (eventLocation['address'])




#attendee details 
attendeeFirstName =  eventbrite.get_attendeeFirstName()
print (attendeeFirstName['first_name'])

attendeeLastName =  eventbrite.get_attendeeLastName()
print (attendeeFirstName['last_name'])

attendeeEmail = eventbrite.get_attendeeEmail()
print (attendeeFirstName['email'])

attendeePhone = eventbrit.get_attendeePhone()
print (attendeePhone['cell_phone'])

attendeeAddress = eventbrite.get_attendeeAddress()
print (attendeeAddress['address'])

attendeeEvent = eventbrite.get_attendeeEvent()
print (attendeeEvent['event_id'])


#price details 






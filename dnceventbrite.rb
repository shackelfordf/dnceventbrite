require 'ruby-2.2.0'
require 'eventbrite'
require 'json_converter'

​
Eventbrite.token = "BGRKOZMNI6NQRUNPD6BZ"
​
events = Eventbrite::User.owned_events({ user_id: 165365079997  })
attendees = Eventbrite::User.owned_event_attendees({ user_id: 165365079997  })
attendees_json = attendees.to_json
events_json = events.to_json
#users = # Grab all users who have authorized us
​
# users.each do |user|
#   @events = Eventbrite::User.owned_events({ user_id: user.id  })
#   @attendees = Eventbrite::User.owned_event_attendees({ user_id: user.id  })
# end
​
converter = JsonConverter.new
converter.write_to_csv attendees_json, 'attendees.csv'
converter.write_to_csv events_json, 'events.csv'
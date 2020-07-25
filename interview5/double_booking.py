'''
Given an array of bookings, which includes start date and end date. Check if that booking is not double booking.
Return number of valid bookings
end date cannot be equal to start date
bookings = ['20190101', '20190106', '20190105', '20190107'], output = 1
bookings = ['20190101', '20190131', '20190105', '20190107', '20190109', '20190111'], output = 1
bookings = ['20190101', '20190131', '20190105', '20190107', '20190109', '20190111', '20190201', '20190204'], output = 2
bookings = ['20190101', '20190104', '20190105', '20190106', '20190102', '20190103'], output = 2

bookings = [1, 6, 5, 7], output = 1
bookings = [1, 31, 5, 7, 9, 11], output = 1
bookings = [1, 4, 5, 6, 2, 3], output = 2
'''


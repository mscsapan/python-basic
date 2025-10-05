class Room:
    def __init__(self, room_number, room_type, price_per_night, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available
    
    def book_room(self):
        # Mark room as booked (unavailable)
        if self.is_available:
            self.is_available = False
            print(f"Room {self.room_number} has been booked")
            return True
        else:
            print(f"Room {self.room_number} is already booked")
            return False
    
    def checkout_room(self):
        # Mark room as available again
        if not self.is_available:
            self.is_available = True
            print(f"Room {self.room_number} is now available")
            return True
        else:
            print(f"Room {self.room_number} was not booked")
            return False
    
    def get_room_info(self):
        status = "Available" if self.is_available else "Booked"
        return f"Room {self.room_number} - {self.room_type} - ${self.price_per_night}/night - {status}"
    
    def __str__(self):
        return self.get_room_info()
    


class Guest:
    def __init__(self, guest_id, name, email, phone):
        self.guest_id = guest_id
        self.name = name
        self.email = email
        self.phone = phone
        
    def get_guest_info(self):
        return f'Name : {self.name} - Email : {self.email} - Phone {self.phone}'
    
    def __str__(self):
        return self.get_guest_info()
    


class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_data, check_out_date):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_data = check_in_data
        self.check_out_date = check_out_date
        self.total_night = self.calculate_nights()
        self.total_cost = self.calculate_cost()
        
    
    def calculate_cost(self):
        return self.room.price_per_night * self.total_night
        
        
    
    def calculate_nights(self):
        # Simple approach: assume dates are in format "YYYY-MM-DD"
        from datetime import datetime
        
        check_in = datetime.strptime(self.check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(self.check_out_date, "%Y-%m-%d")
        
        nights = (check_out - check_in).days
        return nights
    
    
    def cancel_reservation(self):
        """Cancel the reservation and make room available again"""
        if not self.is_cancelled:
            self.is_cancelled = True
            self.room.checkout_room()  # Make room available
            print(f"Reservation {self.reservation_id} has been cancelled")
            return True
        else:
            print(f"Reservation {self.reservation_id} is already cancelled")
            return False
    
    def get_reservation_details(self):
        """Return formatted reservation information"""
        status = "Cancelled" if self.is_cancelled else "Active"
        return (f"Reservation ID: {self.reservation_id}\n"
                f"Guest: {self.guest.name}\n"
                f"Room: {self.room.room_number} ({self.room.room_type})\n"
                f"Check-in: {self.check_in_date}\n"
                f"Check-out: {self.check_out_date}\n"
                f"Total Nights: {self.total_nights}\n"
                f"Total Cost: ${self.total_cost}\n"
                f"Status: {status}")
    
    def __str__(self):
        return self.get_reservation_details()
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 14:29:03 2018

@author: Sunny
"""

import pytest
from server import system
from src.Location import Location
from datetime import datetime
from src.Car import *

class TestBackend(object):
    
    def setup_method(self):
        self.system = system
        self.user = system.validate_login('Matt', 'pass')
        self.small_car = SmallCar('Holden', 'Commodore', 12345)
        self.system.add_car(self.small_car)
        self.medium_car = MediumCar('Ford', 'Falcon', 123456)
        self.system.add_car(self.medium_car)
        self.large_car = LargeCar('Subaru', 'WRX', 1234567)
        self.system.add_car(self.large_car)
        self.premium_car = PremiumCar('Lamborghini', 'Diablo', 12345678)
        self.system.add_car(self.premium_car)
        
        
    def teardown_method(self):
        pass
    
    def setup_class(self):
        pass
    
    def teardown_class(self):
        pass
    
    def test_system(self):
        assert len(self.system.cars) > 4
    
    def test_booking(self):
        location = Location('A', 'B')
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime("2018-04-12", date_format)
        end_date = datetime.strptime("2018-04-12", date_format)
        diff = end_date - start_date
        car = self.system.get_car('0')
        assert car is not None
        booking = self.system.make_booking(self.user, diff.days, car, location)
        assert booking is not None
        assert booking.location == location
        assert booking.booking_fee == 0
        
    def test_large_car_long_period(self):
        location = Location('A', 'B')
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime("2018-04-12", date_format)
        end_date = datetime.strptime("2018-04-22", date_format)
        diff = end_date - start_date
        car = self.large_car
        booking = self.system.make_booking(self.user, diff.days, car, location)
        assert booking is not None
        assert booking.booking_fee == 10*100*0.95

    def test_large_car_short_period(self):
        location = Location('A', 'B')
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime("2018-04-12", date_format)
        end_date = datetime.strptime("2018-04-17", date_format)
        diff = end_date - start_date
        car = self.large_car
        booking = self.system.make_booking(self.user, diff.days, car, location)
        assert booking is not None
        assert booking.booking_fee == 5*100
        
    def test_premium_car(self):
        location = Location('A', 'B')
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime("2018-04-12", date_format)
        end_date = datetime.strptime("2018-04-17", date_format)
        diff = end_date - start_date
        car = self.premium_car
        booking = self.system.make_booking(self.user, diff.days, car, location)
        assert booking is not None
        assert booking.booking_fee == 5*150*1.15
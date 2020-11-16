# -*- coding: utf-8 -*-
import requests as request;
from datetime import datetime,timezone;
from dateutil import tz;
import astropy.coordinates as coord;
from astropy.time import Time;
import astropy.units as u;


class predict_glare:

    def __init__(self):
        self.url = "http://api.timezonedb.com/v2.1/get-time-zone"
        self.api_key = 'ECBFAQT2XHJQ'

    def get_local_timezone(self, latitude, longitude):
        params = dict(key=self.api_key, format='json', by='position', lat=latitude, lng=longitude);
        response = request.get(
            self.url,
            params=params
        );
        return (dict(response.json())["zoneName"])

    def get_localtime(self, epoch_time, tz1):
        datetime_time_utc = datetime.utcfromtimestamp(epoch_time);
        to_zone = tz.gettz(str(tz1));
        local_input = datetime_time_utc.replace(tzinfo=timezone.utc).astimezone(tz=to_zone)
        return (local_input);

    def get_car_azimuth(self, orientation):
        if (orientation < 0):
            return (360 - abs(orientation));
        else:
            return (orientation);

    def get_sun_azimuth_altitude(self, latitude, longitude, Obstime):
        loc = coord.EarthLocation(lon=longitude * u.deg, lat=latitude * u.deg)
        altaz = coord.AltAz(location=loc, obstime=Obstime)
        sun = coord.get_sun(Time(Obstime))
        return (dict(azimuth=sun.transform_to(altaz).az.value, altitude=sun.transform_to(altaz).alt.value))

    def get_azimuthal_difference(self, angle1, angle2):
        return (abs(angle1 - angle2))

    def get_is_possible_glare(self, azimuthal_difference, altitude):
        if (abs(azimuthal_difference) <= 30) and (altitude <= 45 and altitude > 0):
            return True;
        else:
            return False;

    def detect_glare(self, latitude, longitude, epoch, orientation):
        local_timezone = self.get_local_timezone(latitude, longitude);
        local_time = self.get_localtime(epoch, local_timezone);
        car_azimuth = self.get_car_azimuth(orientation)
        sun_params = self.get_sun_azimuth_altitude(latitude, longitude, local_time);
        azimuthal_difference = self.get_azimuthal_difference(sun_params['azimuth'], car_azimuth)
        return self.get_is_possible_glare(azimuthal_difference, sun_params['altitude'])


# Test Code Here
# install astropy and request from pip before running this code
# pip install astropy
# pip install requests









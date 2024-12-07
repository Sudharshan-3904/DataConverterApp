from logging import PlaceHolder
import tkinter
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class DataConversion:
    def __init__(self) -> None:
        self.__input_unit = ""
        self.__output_unit = ""
        self.__input_data = 0

        # Digital Data Storage Conversion Map
        self.__dscMap = {"bytes": 0, "kb": 1, "mb": 2, "gb": 3, "tb": 4}

        # Length Conversion Map
        self.__lcMap = {
            "m": 1, "pm": 10**(-12), "nm": 10**(-10), "mim": 10**(-6), "mm": 10**(-3), "km": 10**(3),
            "ft": 0.3048, "in": 11.99999996952, "mi": 0.0001894027197121078656, "yd": 0.3333333333333333325632, "nmi": 0.00016459199974982016, "fur": 0.001515160797696955584
        }
        
        # Area Conversion Map
        self.__acMap = {
            "m": 1, "mm": 1000000, "cm": 10000, "km": 0.000001, "ha": 0.0001,
            "ac": 0.0002471054, "yd": 1.1959900463, "ft": 10.763910417, "in": 1550.0031
        }
        
        # Volume Conversion Map
        self.__vcMap = {
            "m": 1, "mm": 1000000000, "cm": 1000000, "l": 1000, "ml": 1000000, "cc": 1000000, 
            "yd": 1.3079506193, "ft": 35.314666721, "in": 61023.744095, "uk-gal": 219.9692483, "us-gal": 264.17205236
        }

        # Weight Conversion Map
        self.__wcMap = {
            "kg": 1, "g": 1000, "mg": 1000000, "t": 0.001, 
            "lb": 2.2046226218, "oz": 35.27396195
        }

        # Speed Conversion Map
        self.__scMap = {"m/s": 1, "km/h": 3.6, "m/h": 2.2369362921, "mach": 0.0030184123}

        # Pressure Conversion Map
        self.__pcMap = {"pa": 1, "kpa": 0.001, "mmhg": 0.0075006376, "bar": 0.00001, "mbar": 0.01, "psi": 0.0001450377, "atm": 0.0000098692}

        # Power Conversion Map
        self.__pocMap = {"w": 1, "kw": 0.001, "j/s": 1, "hp": 0.0013410221, "kcal/s": 0.0002388459}

        # Time Conversion Map
        self.__tcMap = {
            "day": 1, "ps": (86400 * (10**(-12))), "ns": (86400 * (10**(-10))), "mis": (86400 * (10**(-6))), "ms": (86400 * (10**(-3))), "s": 86400, "min": 1440, "hr": 24,
            "week": 0.1428571429, "month": 0.0328767123, "year": 0.0027378508, "decade": 0.0002737851, "century": 0.0000273785, "millennium": 0.0000027379
        }

    def setInputUnit(self, ipUnit):
        self.__input_unit = ipUnit

    def setInputData(self, ipData):
        self.__input_data = ipData

    def setOutputUnit(self, opUnit):
        self.__output_unit = opUnit

    def clearUnits(self):
        self.__output_unit = ""
        self.__input_unit = ""
        self.__input_data = 0

    def dataStorageConversion(self):
        returnList = []
        baseQuantity =  self.__input_data * (1024 ** self.__dscMap[self.__input_unit])

        if self.__output_unit == "":
            for unit in self.__dscMap.keys():
                size = baseQuantity / (1024 ** self.__dscMap[unit])
                returnList.append(round(number=size, ndigits=2))
            return returnList
        else:
            return baseQuantity / (1024 ** self.__dscMap[self.__output_unit])

    def lengthConversion(self):
        baseQuantity =  self.__input_data *  self.__lcMap[self.__input_unit]
        final = baseQuantity / (self.__lcMap[self.__output_unit])
        return final

    def areaConversion(self):
        baseQuantity =  self.__input_data *  self.__acMap[self.__input_unit]
        return (baseQuantity / self.__acMap[self.__output_unit])

    def volumeConversion(self):
        baseQuantity =  self.__input_data *  self.__vcMap[self.__input_unit]
        return (baseQuantity / self.__vcMap[self.__output_unit])

    def weightConversion(self):
        baseQuantity =  self.__input_data *  self.__wcMap[self.__input_unit]
        return (baseQuantity / self.__wcMap[self.__output_unit])
    
    def temperatureConversion(self):
        if self.__input_unit == "C":
            if self.__output_unit == "F":
                return self.__input_data + 274.15
            elif self.__output_unit == "K":
                return ((self.__input_data * (9 / 5)) + 32)
            else:
                return self.__input_data
            
        elif self.__input_unit == "F":
            if self.__output_unit == "C":
                return self.__input_data + 274.15
            elif self.__output_unit == "K":
                return ((self.__input_data + 459.67) * (5 / 9))
            else:
                return self.__input_data
            
        elif self.__input_unit == "K":
            if self.__output_unit == "C":
                return self.__input_data - 274.15
            elif self.__output_unit == "F":
                return (((self.__input_data - 274.15) * (9 / 5)) + 32)
            else:
                return self.__input_data
        
        else:
            return None

    def speedConversion(self):
        baseQuantity =  self.__input_data *  self.__scMap[self.__input_unit]
        return (baseQuantity / self.__scMap[self.__output_unit])

    def pressureConversion(self):
        baseQuantity =  self.__input_data *  self.__pcMap[self.__input_unit]
        return (baseQuantity / self.__pcMap[self.__output_unit])
    
    def powerConversion(self):
        baseQuantity =  self.__input_data *  self.__pocMap[self.__input_unit]
        return (baseQuantity / self.__pocMap[self.__output_unit])

    def timeConversion(self):
        baseQuantity =  self.__input_data *  self.__tcMap[self.__input_unit]
        return (baseQuantity / self.__tcMap[self.__output_unit])

    # TODO - Number system Bug
    def numberSystemConversion(self, output_base=10, input_base=10, input_num=0):
        if input_base == output_base:
            return input_num
        elif output_base == 2:
            return bin(input_num)
        elif output_base == 8:
            return oct(input_num)
        elif output_base == 10:
            return int(str(input_num), input_base)
        elif output_base == 16:
            return hex(input_num)
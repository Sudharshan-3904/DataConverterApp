class Converter:
    def  __init__(self) -> None:
        self.conversionMap = dict()
        self.unitMap = dict()
        self.input_unit = None
        self.output_unit = None
        self.input_value = 0
    
    def converter(self) -> float:
        self.checkInput()
        self.checkUnits()
        baseQuantity =  self.input_value *  self.conversionMap[self.input_unit]
        final = baseQuantity / (self.conversionMap[self.output_unit])
        return final
    
    def clearUnits(self) -> None:
        self.input_unit = None
        self.output_unit = None
        self.input_value = None
    
    def checkInput(self):
        self.input_value = float(self.input_value)
    
    def checkUnits(self):
        if self.input_unit not in list(self.conversionMap.keys()):
            self.input_unit = self.unitMap[self.input_unit]

        if self.output_unit not in list(self.conversionMap.keys()):
            self.output_unit = self.unitMap[self.output_unit]

class LengthConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {
            "m": 1, "pm": 10**(-12), "nm": 10**(-10), "mim": 10**(-6), "mm": 10**(-3), "km": 10**(3),
            "ft": 0.3048, "in": 11.99999996952, "mi": 0.0001894027197121078656, "yd": 0.3333333333333333325632, "nmi": 0.00016459199974982016, "fur": 0.001515160797696955584
        }
        self.unitMap = {
            "Picometer (pm)": "pm", "Nanometer (nm)": "nm", "Micrometer (μm)": "mim", "Millimeter (nm)": "mm", "meter (m)": "m", "Kilometer (km)": "km",
            "Feet (ft)": "ft", "Inch (in)": "in", "Mile (mi)": "mi", "Yard (yd)": "yd", "Nautical Mile (nmi)": "nmi", "Furlong (fur)": "fur"
        }

class AreaConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {
            "m": 1, "mm": 1000000, "cm": 10000, "km": 0.000001, "ha": 0.0001,
            "ac": 0.0002471054, "yd": 1.1959900463, "ft": 10.763910417, "in": 1550.0031
        }
        self.unitMap = {
            "Millimeter Sq. (mm²)": "mm", "Centimeter Sq. (cm²)": "cm", "Meter Sq. (m²)": "m", "Kilometer Sq. (km²)": "km", "Hectare (Ha)": "ha",
            "Meter Sq. (m²)": "m", "Acre (ac)": "ac", "Yard Sq. (yd²)": "yd", "Feet Sq. ft²)": "ft", "Inch Sq. (in²)": "in"
        }

class VolumeConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {
            "m": 1, "mm": 1000000000, "cm": 1000000, "l": 1000, "ml": 1000000, "cc": 1000000, 
            "yd": 1.3079506193, "ft": 35.314666721, "in": 61023.744095, "uk-gal": 219.9692483, "us-gal": 264.17205236
        }
        self.unitMap = {
            "Millimeter (mm³)": "mm", "Centimeter (cm³)": "cm", "Meter (m³)": "m", "Liter (l)": "l", "Milliliter (ml)": "ml", "Cubic Centimeter (cc)": "cc",
            "Meter Sq. (m³)": "m", "Yard Sq. (yd³)": "yd", "Feet (ft³)": "ft", "Inch (in³)": "in", "UK Gallon (gal)": "uk-gal", "US Gallon (gal)": "us-gal"
        }

class WeightConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {
            "kg": 1, "g": 1000, "mg": 1000000, "t": 0.001, 
            "lb": 2.2046226218, "oz": 35.27396195
        }
        self.unitMap = {
            "Gram (g)": "g", "Kilogram (kg)": "kg", "Milligram (mg)": "mg", "Metric Ton (t)": "t",
            "Kilogram (kg)": "kg", "Pounds (lbs)": "lb", "Ounce (ozs)": "oz"
        }

class SpeedConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {"m/s": 1, "km/h": 3.6, "m/h": 2.2369362921, "mach": 0.0030184123}
        self.unitMap = {"Meter per Sec (m/s)": "m/s", "Kilometer per Hour (km/h)": "km/h", "Meter per Hour (m/h)": "m/h", "Mach (mach)": "mach"}

class PressureConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {"pa": 1, "kpa": 0.001, "mmhg": 0.0075006376, "bar": 0.00001, "mbar": 0.01, "psi": 0.0001450377, "atm": 0.0000098692}
        self.unitMap = {"Pascal (pa)": "pa", "Kilopascal (kpa)": "kpa", "Millimeter Mercury (mmHg)": "mmHg", "Bar (bar)": "bar", "Millibar (mbar)": "mbar", "Pounds per Inch² (psi)": "psi", "Atmosphere (atm)": "atm"}

class PowerConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {"w": 1, "kw": 0.001, "j/s": 1, "hp": 0.0013410221, "kcal/s": 0.0002388459}
        self.unitMap = {"Watt (w)": "w", "Kilowatt (kw)": "kw", "Joules per second (j/s)": "j/s", "Horse Power (hp)": "hp", "Kilocalorie pre Second (kcal/s)": "kcal/s"}

class TimeConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {
            "day": 1, "ps": (86400 * (10**(-12))), "ns": (86400 * (10**(-10))), "mis": (86400 * (10**(-6))), "ms": (86400 * (10**(-3))), "s": 86400, "min": 1440, "hr": 24,
            "week": 0.1428571429, "month": 0.0328767123, "year": 0.0027378508, "decade": 0.0002737851, "century": 0.0000273785, "millennium": 0.0000027379
        }
        self.unitMap = {
                "Picoseconds (ps)": "ps", "Nanoseconds (ns)": "ns", "Microseconds (μs)": "mis", "Milliseconds (ms)": "ms", "Seconds (sec)": "sec", "Minutes (min)": "min", "Hour (Hr)": "hr", "Days": "day",
                "Days": "day", "Weeks": "week", "Months": "month", "Year": "year", "Decades": "decade", "Centuries": "century", "Millennium": "millennium"
            }

class TemeratureConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = { "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K" }
        self.unitMap = { "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K" }
    
    def converter(self) -> float:
        self.checkInput()
        self.checkUnits()
        if self.input_unit == "C":
            if self.output_unit == "F":
                return self.input_value + 274.15
            elif self.output_unit == "K":
                return ((self.input_value * (9 / 5)) + 32)
            else:
                return self.input_value
        elif self.input_unit == "F":
            if self.output_unit == "C":
                return self.input_value + 274.15
            elif self.output_unit == "K":
                return ((self.input_value + 459.67) * (5 / 9))
            else:
                return self.input_value
        elif self.input_unit == "K":
            if self.output_unit == "C":
                return self.input_value - 274.15
            elif self.output_unit == "F":
                return (((self.input_value - 274.15) * (9 / 5)) + 32)
            else:
                return self.input_value
        else:
            return 0.0

class DigitalDataConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
        self.conversionMap = {"bytes": 0, "kb": 1, "mb": 2, "gb": 3, "tb": 4}
        self.unitMap = {
            "Bytes (by)": "bytes", "KiloByte (Kb)": "kb", "MegaByte (Mb)": "mb", "GigaByte (Gb)": "gb", "TeraByte (Tb)": "tb"
        }

    def converter(self):
        self.checkInput()
        self.checkUnits()
        baseQuantity =  self.input_value * (1024 ** self.conversionMap[self.input_unit])
        return baseQuantity / (1024 ** self.conversionMap[self.output_unit])

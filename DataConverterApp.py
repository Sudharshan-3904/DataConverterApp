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


class Interface(ctk.CTk):
    def __init__(self):
        # Declaring All the unit maps
        self.__ddUnMap = {
            "Bytes (by)": "bytes", "KiloByte (Kb)": "kb", "MegaByte (Mb)": "mb", "GigaByte (Gb)": "gb", "TeraByte (Tb)": "tb"
        }

        self.__lenUnMap = {
            "Picometer (pm)": "pm", "Nanometer (nm)": "nm", "Micrometer (μm)": "mim", "Millimeter (nm)": "mm", "meter (m)": "m", "Kilometer (km)": "km",
            "Feet (ft)": "ft", "Inch (in)": "in", "Mile (mi)": "mi", "Yard (yd)": "yd", "Nautical Mile (nmi)": "nmi", "Furlong (fur)": "fur"
        }

        self.__areaUnMap = {
            "Millimeter Sq. (mm²)": "mm", "Centimeter Sq. (cm²)": "cm", "Meter Sq. (m²)": "m", "Kilometer Sq. (km²)": "km", "Hectare (Ha)": "ha",
            "Meter Sq. (m²)": "m", "Acre (ac)": "ac", "Yard Sq. (yd²)": "yd", "Feet Sq. ft²)": "ft", "Inch Sq. (in²)": "in"
        }
        
        self.__volUnMap = {
            "Millimeter (mm³)": "mm", "Centimeter (cm³)": "cm", "Meter (m³)": "m", "Liter (l)": "l", "Milliliter (ml)": "ml", "Cubic Centimeter (cc)": "cc",
            "Meter Sq. (m³)": "m", "Yard Sq. (yd³)": "yd", "Feet (ft³)": "ft", "Inch (in³)": "in", "UK Gallon (gal)": "uk-gal", "US Gallon (gal)": "us-gal"
        }

        self.__whtUnMap = {
            "Gram (g)": "g", "Kilogram (kg)": "kg", "Milligram (mg)": "mg", "Metric Ton (t)": "t",
            "Kilogram (kg)": "kg", "Pounds (lbs)": "lb", "Ounce (ozs)": "oz"
        }
        
        self.__tempUnMap = {
            "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
        }

        self.__spcUnMap = {"Meter per Sec (m/s)": "m/s", "Kilometer per Hour (km/h)": "km/h", "Meter per Hour (m/h)": "m/h", "Mach (mach)": "mach"}

        self.__preUnMap = {"Pascal (pa)": "pa", "Kilopascal (kpa)": "kpa", "Millimeter Mercury (mmHg)": "mmHg", "Bar (bar)": "bar", "Millibar (mbar)": "mbar", "Pounds per Inch² (psi)": "psi", "Atmosphere (atm)": "atm"}

        self.__powUnMap = {"Watt (w)": "w", "Kilowatt (kw)": "kw", "Joules per second (j/s)": "j/s", "Horse Power (hp)": "hp", "Kilocalorie pre Second (kcal/s)": "kcal/s"}

        self.__tcUnMap = {
                "Picoseconds (ps)": "ps", "Nanoseconds (ns)": "ns", "Microseconds (μs)": "mis", "Milliseconds (ms)": "ms", "Seconds (sec)": "sec", "Minutes (min)": "min", "Hour (Hr)": "hr", "Days": "day",
                "Days": "day", "Weeks": "week", "Months": "month", "Year": "year", "Decades": "decade", "Centuries": "century", "Millennium": "millennium"
            }
        
        #declaring Object and Variables
        self.__dataConvObj = DataConversion()
        self.__selected_tab = ""
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{600}x{400}")

        # Declaring required String Variables
        # Digital Storage Conversion Int and String Vars
        self.__digital_data_input_unit_str_var = ctk.StringVar()
        self.__digital_data_output_unit_str_var = ctk.StringVar()
        self.__digital_data_input_entry_str_var = ctk.StringVar()

        # Length Conversion Int and String Vars
        self.__length_input_unit_str_var = ctk.StringVar()
        self.__length_output_unit_str_var = ctk.StringVar()
        self.__length_input_entry_str_var = ctk.StringVar()

        # Area Conversion Int and String Vars
        self.__area_input_unit_str_var = ctk.StringVar()
        self.__area_output_unit_str_var = ctk.StringVar()
        self.__area_input_entry_str_var = ctk.StringVar()

        # Volume Conversion Int and String Vars
        self.__vol_input_unit_str_var = ctk.StringVar()
        self.__vol_output_unit_str_var = ctk.StringVar()
        self.__vol_input_entry_str_var = ctk.StringVar()

        # Weight Conversion Int and String Vars
        self.__wht_input_unit_str_var = ctk.StringVar()
        self.__wht_output_unit_str_var = ctk.StringVar()
        self.__wht_input_entry_str_var = ctk.StringVar()

        # Temperature Conversion Int and String Vars
        self.__temp_input_unit_str_var = ctk.StringVar()
        self.__temp_output_unit_str_var = ctk.StringVar()
        self.__temp_input_entry_str_var = ctk.StringVar()

        # Speed Conversion Int and String Vars
        self.__spc_input_unit_str_var = ctk.StringVar()
        self.__spc_output_unit_str_var = ctk.StringVar()
        self.__spc_input_entry_str_var = ctk.StringVar()

        # Pressure Conversion Int and String Vars
        self.__pre_input_unit_str_var = ctk.StringVar()
        self.__pre_output_unit_str_var = ctk.StringVar()
        self.__pre_input_entry_str_var = ctk.StringVar()

        # Power Conversion Int and String Vars
        self.__pow_input_unit_str_var = ctk.StringVar()
        self.__pow_output_unit_str_var = ctk.StringVar()
        self.__pow_input_entry_str_var = ctk.StringVar()

        # Time Conversion Int and String Vars
        self.__tc_input_unit_str_var = ctk.StringVar()
        self.__tc_output_unit_str_var = ctk.StringVar()
        self.__tc_input_entry_str_var = ctk.StringVar()

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        #Sidebar Configuration
        self.__sidebar_frame = ctk.CTkScrollableFrame(self, width=180, corner_radius=5)
        self.__sidebar_frame.grid(row=0, column=0, rowspan=15, sticky="nsew")

        self.__logo_sidebar_label = ctk.CTkLabel(master=self.__sidebar_frame, text="Converter App", font=ctk.CTkFont(size=20, weight="bold"))
        self.__logo_sidebar_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.__dd_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Digital", command=lambda: self.updateSection("Digital"))
        self.__dd_conv_sidebar_button.grid(row=1, column=0, padx=20, pady=5)
        
        self.__len_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Length", command=lambda: self.updateSection("Length"))
        self.__len_conv_sidebar_button.grid(row=2, column=0, padx=20, pady=5)
        
        self.__area_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Area", command=lambda: self.updateSection("Area"))
        self.__area_conv_sidebar_button.grid(row=3, column=0, padx=20, pady=5)
        
        self.__vol_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Volume", command=lambda: self.updateSection("Volume"))
        self.__vol_conv_sidebar_button.grid(row=4, column=0, padx=20, pady=5)
        
        self.__weight_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Weight", command=lambda: self.updateSection("Weight"))
        self.__weight_conv_sidebar_button.grid(row=5, column=0, padx=20, pady=5)
        
        self.__speed_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Speed", command=lambda: self.updateSection("Speed"))
        self.__speed_conv_sidebar_button.grid(row=6, column=0, padx=20, pady=5)
        
        self.__pre_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Pressure", command=lambda: self.updateSection("Pressure"))
        self.__pre_conv_sidebar_button.grid(row=7, column=0, padx=20, pady=5)
        
        self.__pow_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Power", command=lambda: self.updateSection("Power"))
        self.__pow_conv_sidebar_button.grid(row=8, column=0, padx=20, pady=5)
        
        self.__time_conv_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Time", command=lambda: self.updateSection("Time"))
        self.__time_conv_sidebar_button.grid(row=9, column=0, padx=20, pady=5)

        self.__appearance_mode_label = ctk.CTkLabel(self.__sidebar_frame, text="Appearance Mode", anchor="w")
        self.__appearance_mode_label.grid(row=10, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_options_menu = ctk.CTkComboBox(self.__sidebar_frame, values=["Dark", "Light", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_options_menu.grid(row=11, column=0, padx=20, pady=5)

        self.__scaling_label = ctk.CTkLabel(self.__sidebar_frame, text="UI Scaling", anchor="w")
        self.__scaling_label.grid(row=12, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_options_menu = ctk.CTkComboBox(self.__sidebar_frame, values=["80%", "90%", "100%", "110%", "120%", ],command=self.change_scaling_event)
        self.appearance_mode_options_menu.grid(row=13, column=0, padx=20, pady=5)
        
        self.__quit_sidebar_button = ctk.CTkButton(self.__sidebar_frame, text="Quit", command=lambda: self.destroy())
        self.__quit_sidebar_button.grid(row=14, column=0, padx=20, pady=5)

        self.__section_content_frame = ctk.CTkFrame(master=self, corner_radius=5)
        self.__section_content_frame.grid(row=0, column=1, rowspan=15, sticky="nsew")

        self.change_appearance_mode_event("Dark")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        self.updateSection(self.__selected_tab)
        self.update()

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
    
    def convertDigitalData(self):
        self.__dataConvObj.setInputUnit(self.__ddUnMap[self.__digital_data_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__ddUnMap[self.__digital_data_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__digital_data_input_entry_str_var.get()))
        self.__digital_output_data_label.configure(text=self.__dataConvObj.dataStorageConversion())
        self.update()
    
    def convertLength(self):
        self.__dataConvObj.setInputUnit(self.__lenUnMap[self.__length_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__lenUnMap[self.__length_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__length_input_entry_str_var.get()))
        self.__length_output_data_display_label.configure(text=self.__dataConvObj.lengthConversion())
        self.update()
    
    def convertArea(self):
        self.__dataConvObj.setInputUnit(self.__areaUnMap[self.__area_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__areaUnMap[self.__area_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__area_input_entry_str_var.get()))
        self.__area_output_data_display_label.configure(text=self.__dataConvObj.areaConversion())
        self.update()
    
    def convertVolume(self):
        self.__dataConvObj.setInputUnit(self.__volUnMap[self.__vol_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__volUnMap[self.__vol_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__vol_input_entry_str_var.get()))
        self.__vol_output_data_display_label.configure(text=self.__dataConvObj.areaConversion())
        self.update()
    
    def convertWeight(self):
        self.__dataConvObj.setInputUnit(self.__whtUnMap[self.__wht_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__whtUnMap[self.__wht_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__wht_input_entry_str_var.get()))
        self.__wht_output_data_display_label.configure(text=self.__dataConvObj.weightConversion())
        self.update()
    
    def convertTemperature(self):
        self.__dataConvObj.setInputUnit(self.__tempUnMap[self.__temp_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__tempUnMap[self.__temp_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__temp_input_entry_str_var.get()))
        self.__temp_output_data_display_label.configure(text=self.__dataConvObj.temperatureConversion())
        self.update()
    
    def convertSpeed(self):
        self.__dataConvObj.setInputUnit(self.__spcUnMap[self.__spc_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__spcUnMap[self.__spc_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__spc_input_entry_str_var.get()))
        self.__spc_output_data_display_label.configure(text=self.__dataConvObj.speedConversion())
        self.update()
    
    def convertPressure(self):
        self.__dataConvObj.setInputUnit(self.__preUnMap[self.__pre_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__preUnMap[self.__pre_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__pre_input_entry_str_var.get()))
        self.__pre_output_data_display_label.configure(text=self.__dataConvObj.pressureConversion())
        self.update()
    
    def convertPower(self):
        self.__dataConvObj.setInputUnit(self.__powUnMap[self.__pow_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__powUnMap[self.__pow_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__pow_input_entry_str_var.get()))
        self.__pow_output_data_display_label.configure(text=self.__dataConvObj.powerConversion())
        self.update()
    
    def convertTime(self):
        self.__dataConvObj.setInputUnit(self.__tcUnMap[self.__tc_input_unit_str_var.get()])
        self.__dataConvObj.setOutputUnit(self.__tcUnMap[self.__tc_output_unit_str_var.get()])
        self.__dataConvObj.setInputData(int(self.__tc_input_entry_str_var.get()))
        self.__tc_output_data_display_label.configure(text=self.__dataConvObj.timeConversion())
        self.update()
    
    def updateSection(self, section=""):
        def clearFrame():
            for widget in self.__section_content_frame.winfo_children():
                widget.destroy()

        match section:
            case "Home":
                clearFrame()
                self.__selected_tab = "Home"
                self.__sections_label = ctk.CTkLabel(master=self.__section_content_frame, text="Choose Category \n to Convert", font=ctk.CTkFont(size=30, weight="bold"))
                self.__sections_label.grid(row=1, column=1, sticky="nsew")

            case "Digital":
                clearFrame()
                self.__selected_tab = "Digital"

                self.__digital_data_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__digital_data_input_name = ctk.CTkLabel(master=self.__digital_data_conversion_label, text="Input Unit")
                self.__digital_data_input_name.grid(row=0, column=0, sticky="ew")

                self.__digital_data_input_unit_menu = ctk.CTkComboBox(master=self.__digital_data_conversion_label, values=list(self.__ddUnMap.keys()), variable=self.__digital_data_input_unit_str_var)
                self.__digital_data_input_unit_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__digital_input_data_entry = ctk.CTkEntry(master=self.__digital_data_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__digital_data_input_entry_str_var)
                self.__digital_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__digital_data_output_name = ctk.CTkLabel(master=self.__digital_data_conversion_label, text="Output Unit")
                self.__digital_data_output_name.grid(row=2, column=0, sticky="ew")

                self.__digital_data_output_unit_menu = ctk.CTkComboBox(master=self.__digital_data_conversion_label, values=list(self.__ddUnMap.keys()), variable=self.__digital_data_output_unit_str_var)
                self.__digital_data_output_unit_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__digital_output_data_label = ctk.CTkLabel(master=self.__digital_data_conversion_label, text="0")
                self.__digital_output_data_label.grid(row=3, columnspan=4, sticky="ew")

                self.__digital_data_convert_button = ctk.CTkButton(master=self.__digital_data_conversion_label, text="Convert", border_width=3, command=self.convertDigitalData)
                self.__digital_data_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__digital_data_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Length":
                clearFrame()
                self.__selected_tab = "Length"

                self.__length_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__length_unit_input_name = ctk.CTkLabel(master=self.__length_conversion_label, text="Input Unit")
                self.__length_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__length_input_units_menu = ctk.CTkComboBox(master=self.__length_conversion_label, values=list(self.__lenUnMap.keys()), variable=self.__length_input_unit_str_var)
                self.__length_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__length_input_data_entry = ctk.CTkEntry(master=self.__length_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__length_input_entry_str_var)
                self.__length_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__length_output_unit_name = ctk.CTkLabel(master=self.__length_conversion_label, text="Output Unit")
                self.__length_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__length_output_units_menu = ctk.CTkComboBox(master=self.__length_conversion_label, values=list(self.__lenUnMap.keys()), variable=self.__length_output_unit_str_var)
                self.__length_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__length_output_data_display_label = ctk.CTkLabel(master=self.__length_conversion_label, text="0")
                self.__length_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__length_convert_button = ctk.CTkButton(master=self.__length_conversion_label, text="Convert", border_width=3, command=self.convertLength)
                self.__length_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__length_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Area":
                clearFrame()
                self.__selected_tab = "Area"

                self.__area_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__area_unit_input_name = ctk.CTkLabel(master=self.__area_conversion_label, text="Input Unit")
                self.__area_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__area_input_units_menu = ctk.CTkComboBox(master=self.__area_conversion_label, values=list(self.__areaUnMap.keys()), variable=self.__area_input_unit_str_var)
                self.__area_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__area_input_data_entry = ctk.CTkEntry(master=self.__area_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__area_input_entry_str_var)
                self.__area_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__area_output_unit_name = ctk.CTkLabel(master=self.__area_conversion_label, text="Output Unit")
                self.__area_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__area_output_units_menu = ctk.CTkComboBox(master=self.__area_conversion_label, values=list(self.__areaUnMap.keys()), variable=self.__area_output_unit_str_var)
                self.__area_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__area_output_data_display_label = ctk.CTkLabel(master=self.__area_conversion_label, text="0")
                self.__area_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__area_convert_button = ctk.CTkButton(master=self.__area_conversion_label, text="Convert", border_width=3, command=self.convertArea)
                self.__area_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__area_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Volume":
                clearFrame()
                self.__selected_tab = "Volume"

                self.__vol_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__vol_unit_input_name = ctk.CTkLabel(master=self.__vol_conversion_label, text="Input Unit")
                self.__vol_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__vol_input_units_menu = ctk.CTkComboBox(master=self.__vol_conversion_label, values=list(self.__volUnMap.keys()), variable=self.__vol_input_unit_str_var)
                self.__vol_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__vol_input_data_entry = ctk.CTkEntry(master=self.__vol_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__vol_input_entry_str_var)
                self.__vol_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__vol_output_unit_name = ctk.CTkLabel(master=self.__vol_conversion_label, text="Output Unit")
                self.__vol_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__vol_output_units_menu = ctk.CTkComboBox(master=self.__vol_conversion_label, values=list(self.__volUnMap.keys()), variable=self.__vol_output_unit_str_var)
                self.__vol_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__vol_output_data_display_label = ctk.CTkLabel(master=self.__vol_conversion_label, text="0")
                self.__vol_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__vol_convert_button = ctk.CTkButton(master=self.__vol_conversion_label, text="Convert", border_width=3, command=self.convertVolume)
                self.__vol_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__vol_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Weight":
                clearFrame()
                self.__selected_tab = "Weight"

                self.__wht_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__wht_unit_input_name = ctk.CTkLabel(master=self.__wht_conversion_label, text="Input Unit")
                self.__wht_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__wht_input_units_menu = ctk.CTkComboBox(master=self.__wht_conversion_label, values=list(self.__whtUnMap.keys()), variable=self.__wht_input_unit_str_var)
                self.__wht_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__wht_input_data_entry = ctk.CTkEntry(master=self.__wht_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__wht_input_entry_str_var)
                self.__wht_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__wht_output_unit_name = ctk.CTkLabel(master=self.__wht_conversion_label, text="Output Unit")
                self.__wht_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__wht_output_units_menu = ctk.CTkComboBox(master=self.__wht_conversion_label, values=list(self.__whtUnMap.keys()), variable=self.__wht_output_unit_str_var)
                self.__wht_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__wht_output_data_display_label = ctk.CTkLabel(master=self.__wht_conversion_label, text="0")
                self.__wht_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__wht_convert_button = ctk.CTkButton(master=self.__wht_conversion_label, text="Convert", border_width=3, command=self.convertWeight)
                self.__wht_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__wht_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Temperature":
                clearFrame()
                self.__selected_tab = "Temperature"

                self.__temp_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__temp_unit_input_name = ctk.CTkLabel(master=self.__temp_conversion_label, text="Input Unit")
                self.__temp_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__temp_input_units_menu = ctk.CTkComboBox(master=self.__temp_conversion_label, values=list(self.__tempUnMap.keys()), variable=self.__temp_input_unit_str_var)
                self.__temp_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__temp_input_data_entry = ctk.CTkEntry(master=self.__temp_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__temp_input_entry_str_var)
                self.__temp_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__temp_output_unit_name = ctk.CTkLabel(master=self.__temp_conversion_label, text="Output Unit")
                self.__temp_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__temp_output_units_menu = ctk.CTkComboBox(master=self.__temp_conversion_label, values=list(self.__tempUnMap.keys()), variable=self.__temp_output_unit_str_var)
                self.__temp_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__temp_output_data_display_label = ctk.CTkLabel(master=self.__temp_conversion_label, text="0")
                self.__temp_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__temp_convert_button = ctk.CTkButton(master=self.__temp_conversion_label, text="Convert", border_width=3, command=self.convertTemperature)
                self.__temp_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__temp_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Speed":
                clearFrame()
                self.__selected_tab = "Speed"

                self.__spc_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__spc_unit_input_name = ctk.CTkLabel(master=self.__spc_conversion_label, text="Input Unit")
                self.__spc_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__spc_input_units_menu = ctk.CTkComboBox(master=self.__spc_conversion_label, values=list(self.__spcUnMap.keys()), variable=self.__spc_input_unit_str_var)
                self.__spc_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__spc_input_data_entry = ctk.CTkEntry(master=self.__spc_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__spc_input_entry_str_var)
                self.__spc_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__spc_output_unit_name = ctk.CTkLabel(master=self.__spc_conversion_label, text="Output Unit")
                self.__spc_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__spc_output_units_menu = ctk.CTkComboBox(master=self.__spc_conversion_label, values=list(self.__spcUnMap.keys()), variable=self.__spc_output_unit_str_var)
                self.__spc_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__spc_output_data_display_label = ctk.CTkLabel(master=self.__spc_conversion_label, text="0")
                self.__spc_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__spc_convert_button = ctk.CTkButton(master=self.__spc_conversion_label, text="Convert", border_width=3, command=self.convertSpeed)
                self.__spc_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__spc_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Pressure":
                clearFrame()
                self.__selected_tab = "Pressure"

                self.__pre_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__pre_unit_input_name = ctk.CTkLabel(master=self.__pre_conversion_label, text="Input Unit")
                self.__pre_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__pre_input_units_menu = ctk.CTkComboBox(master=self.__pre_conversion_label, values=list(self.__preUnMap.keys()), variable=self.__pre_input_unit_str_var)
                self.__pre_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__pre_input_data_entry = ctk.CTkEntry(master=self.__pre_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__pre_input_entry_str_var)
                self.__pre_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__pre_output_unit_name = ctk.CTkLabel(master=self.__pre_conversion_label, text="Output Unit")
                self.__pre_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__pre_output_units_menu = ctk.CTkComboBox(master=self.__pre_conversion_label, values=list(self.__preUnMap.keys()), variable=self.__pre_output_unit_str_var)
                self.__pre_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__pre_output_data_display_label = ctk.CTkLabel(master=self.__pre_conversion_label, text="0")
                self.__pre_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__pre_convert_button = ctk.CTkButton(master=self.__pre_conversion_label, text="Convert", border_width=3, command=self.convertPressure)
                self.__pre_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__pre_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Power":
                clearFrame()
                self.__selected_tab = "Power"

                self.__pow_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__pow_unit_input_name = ctk.CTkLabel(master=self.__pow_conversion_label, text="Input Unit")
                self.__pow_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__pow_input_units_menu = ctk.CTkComboBox(master=self.__pow_conversion_label, values=list(self.__powUnMap.keys()), variable=self.__pow_input_unit_str_var)
                self.__pow_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__pow_input_data_entry = ctk.CTkEntry(master=self.__pow_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__pow_input_entry_str_var)
                self.__pow_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__pow_output_unit_name = ctk.CTkLabel(master=self.__pow_conversion_label, text="Output Unit")
                self.__pow_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__pow_output_units_menu = ctk.CTkComboBox(master=self.__pow_conversion_label, values=list(self.__powUnMap.keys()), variable=self.__pow_output_unit_str_var)
                self.__pow_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__pow_output_data_display_label = ctk.CTkLabel(master=self.__pow_conversion_label, text="0")
                self.__pow_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__pow_convert_button = ctk.CTkButton(master=self.__pow_conversion_label, text="Convert", border_width=3, command=self.convertPower)
                self.__pow_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__pow_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case "Time":
                clearFrame()
                self.__selected_tab = "Time"

                self.__tc_conversion_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

                self.__tc_unit_input_name = ctk.CTkLabel(master=self.__tc_conversion_label, text="Input Unit")
                self.__tc_unit_input_name.grid(row=0, column=0, sticky="ew")

                self.__tc_input_units_menu = ctk.CTkComboBox(master=self.__tc_conversion_label, values=list(self.__tcUnMap.keys()), variable=self.__tc_input_unit_str_var)
                self.__tc_input_units_menu.grid(row=0, column=1, columnspan=3, sticky="ew")

                self.__tc_input_data_entry = ctk.CTkEntry(master=self.__tc_conversion_label, placeholder_text="Enter Input Number", textvariable=self.__tc_input_entry_str_var)
                self.__tc_input_data_entry.grid(row=1, columnspan=4, sticky="ew")

                self.__tc_output_unit_name = ctk.CTkLabel(master=self.__tc_conversion_label, text="Output Unit")
                self.__tc_output_unit_name.grid(row=2, column=0, sticky="ew")

                self.__tc_output_units_menu = ctk.CTkComboBox(master=self.__tc_conversion_label, values=list(self.__tcUnMap.keys()), variable=self.__tc_output_unit_str_var)
                self.__tc_output_units_menu.grid(row=2, column=1, columnspan=3, sticky="ew")

                self.__tc_output_data_display_label = ctk.CTkLabel(master=self.__tc_conversion_label, text="0")
                self.__tc_output_data_display_label.grid(row=3, columnspan=4, sticky="ew")

                self.__tc_convert_button = ctk.CTkButton(master=self.__tc_conversion_label, text="Convert", border_width=3, command=self.convertTime)
                self.__tc_convert_button.grid(row=4, column=0, columnspan=3, sticky="ew")

                self.__tc_conversion_label.grid(row=0, column=0, sticky="nsew")
            
            case _:              # Default Case
                clearFrame()
                self.updateSection(section="Home")
            
        self.update()


if __name__ == "__main__":
    app = Interface()
    app.mainloop()

from logging import PlaceHolder
import tkinter
import tkinter.messagebox
import customtkinter as ctk
import app

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

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
        # self.__dataConvObj = app.DataConversion()
        self.__selected_tab = ""
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{600}x{400}")

        # Declaring required String Variables
        self.__input_unit_str_var = ctk.StringVar()
        self.__output_unit_str_var = ctk.StringVar()
        self.__input_entry_str_var = ctk.StringVar()

        self.grid_columnconfigure(1, weight=1)
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
        self.__section_content_frame.grid_columnconfigure(0, weight=1)
        self.__section_content_frame.grid_rowconfigure(1, weight=1)

        self.change_appearance_mode_event("Dark")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        self.updateSection(self.__selected_tab)
        self.update()

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def convertData(self):
        conObj = None
        if self.__selected_tab == "Length":
            conObj = app.LengthConverter()
        elif self.__selected_tab == "Area":
            conObj = app.AreaConverter()
        elif self.__selected_tab == "Volume":
            conObj = app.VolumeConverter()
        elif self.__selected_tab == "Weight":
            conObj = app.WeightConverter()
        elif self.__selected_tab == "Speed":
            conObj = app.SpeedConverter()
        elif self.__selected_tab == "Pressure":
            conObj = app.PressureConverter()
        elif self.__selected_tab == "Power":
            conObj = app.PowerConverter()
        elif self.__selected_tab == "Time":
            conObj = app.TimeConverter()
        elif self.__selected_tab == "Temperature":
            conObj = app.TemeratureConverter()
        elif self.__selected_tab == "Digital":
            conObj = app.DigitalDataConverter()
        else:
            print(self.__selected_tab)
        
        conObj.input_unit = self.__input_unit_str_var.get()
        conObj.output_unit = self.__output_unit_str_var.get()
        conObj.input_value = self.__input_entry_str_var.get()

        self.__conversion_output_data_label.configure(text=str(conObj.converter()))
        self.update()

    def create_new_convertion_section(self, title: str ="", unit_list:list = []):
        self.clearFrame()

        self.__selected_tab = title
        self.__section_converter_master_label = ctk.CTkLabel(master=self.__section_content_frame, text="")

        self.__secion_title_label = ctk.CTkLabel(master=self.__section_converter_master_label, text=f"{title} Data Conversion")
        self.__secion_title_label.grid(row=0, column=0, sticky="nsew", columnspan=5)

        self.__convertion_input_unit_label = ctk.CTkLabel(master=self.__section_converter_master_label, text="Input Unit")
        self.__convertion_input_unit_label.grid(row=1, column=0, sticky="nsew")

        self.__conversion_data_input_unit_menu = ctk.CTkComboBox(master=self.__section_converter_master_label, values=unit_list, variable=self.__input_unit_str_var)
        self.__conversion_data_input_unit_menu.grid(row=1, column=1, columnspan=3, sticky="nsew")

        self.__conversion_input_data_entry = ctk.CTkEntry(master=self.__section_converter_master_label, placeholder_text="Enter Input Number", textvariable=self.__input_entry_str_var)
        self.__conversion_input_data_entry.grid(row=2, columnspan=4, sticky="nsew")

        self.__conversion_data_output_name = ctk.CTkLabel(master=self.__section_converter_master_label, text="Output Unit")
        self.__conversion_data_output_name.grid(row=3, column=0, sticky="nsew")

        self.__conversion_data_output_unit_menu = ctk.CTkComboBox(master=self.__section_converter_master_label, values=unit_list, variable=self.__output_unit_str_var)
        self.__conversion_data_output_unit_menu.grid(row=3, column=1, columnspan=3, sticky="nsew")

        self.__conversion_output_data_label = ctk.CTkLabel(master=self.__section_converter_master_label, text="0")
        self.__conversion_output_data_label.grid(row=4, columnspan=4, sticky="nsew")

        self.__conversion_data_convert_button = ctk.CTkButton(master=self.__section_converter_master_label, text="Convert", border_width=3, command=self.convertData)
        self.__conversion_data_convert_button.grid(row=5, column=0, columnspan=3, sticky="nsew")    
    
    def clearFrame(self):
        for widget in self.__section_content_frame.winfo_children():
            widget.destroy()
        
        self.__input_entry_str_var.set("")
        self.__input_unit_str_var.set("")
        self.__output_unit_str_var.set("")
    
    def updateSection(self, section=""):

        match section:
            case "Home":
                self.clearFrame()
                self.__selected_tab = "Home"
                self.__sections_label = ctk.CTkLabel(master=self.__section_content_frame, text="Choose Category \n to Convert", font=ctk.CTkFont(size=30, weight="bold"))
                self.__sections_label.grid(row=1, column=1, sticky="nsew")

            case "Digital":
                self.create_new_convertion_section(title="Digital", unit_list=list(self.__ddUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Length":
                self.create_new_convertion_section(title="Length", unit_list=list(self.__lenUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Area":
                self.create_new_convertion_section(title="Area", unit_list=list(self.__areaUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Volume":
                self.create_new_convertion_section(title="Volume", unit_list=list(self.__volUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Weight":
                self.create_new_convertion_section(title="Weight", unit_list=list(self.__whtUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Temperature":
                self.create_new_convertion_section(title="Temperature", unit_list=list(self.__tempUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Speed":
                self.create_new_convertion_section(title="Speed", unit_list=list(self.__spcUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Pressure":
                self.create_new_convertion_section(title="Pressure", unit_list=list(self.__preUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Power":
                self.create_new_convertion_section(title="Power", unit_list=list(self.__powUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case "Time":
                self.create_new_convertion_section(title="Time", unit_list=list(self.__tcUnMap.keys()))
                self.__section_converter_master_label.pack()
            
            case _:              # Default Case
                self.clearFrame()
                self.updateSection(section="Home")
        
        self.update()

if __name__ == "__main__":
    appObj = Interface()
    appObj.mainloop()
